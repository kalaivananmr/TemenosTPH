"""
==============================================================
  Temenos Docs Crawler v2 — Deep Recursive + RAG-Ready
  Target : https://docs.temenos.com/docs/Solutions/Payments/
  Method : Playwright (real browser) + manual SSO login
  Output :
    ./temenos_docs/             - one .md per page
    ./temenos_rag/chunks.jsonl  - chunked docs for vector DB
    ./temenos_rag/metadata.json - page index with hierarchy
    ./temenos_docs_compiled/FULL_PAYMENTS.md  - single skill file

USAGE
-----
  Step 1:  python temenos_crawler_v2.py --login
  Step 2:  python temenos_crawler_v2.py --crawl
  Step 3:  python temenos_crawler_v2.py --rag
  Step 4:  python temenos_crawler_v2.py --compile
  Or all:  python temenos_crawler_v2.py --all
==============================================================
"""

import asyncio
import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse

from markdownify import markdownify as md_convert

# ─────────────────────── CONFIG ──────────────────────────────
START_URL      = "https://docs.temenos.com/docs/Solutions/Payments/Content/payments.html"
BASE_DOMAIN    = "docs.temenos.com"
ALLOWED_PREFIXES = [
    "/docs/Solutions/Payments/",
    "/docs/Solutions/T24_Transact/",
]
SEED_URLS      = [
    START_URL,
    # Payment Initiation (PI)
    "https://docs.temenos.com/docs/Solutions/Payments/Orders/PI/Payment_Initiation_(PI)/Misc/Introduction_PI.htm",
    # Debit Collection (DB)
    "https://docs.temenos.com/docs/Solutions/Payments/Orders/DB/Debit_Collection_Initiation_(DB)/Misc/Debit_Collection_Application.htm",
    # Payment Packages
    "https://docs.temenos.com/docs/Solutions/Payments/Packages/Payment_Packages/Packages/Misc/Overview.htm",
    # Payments Hub (PP)
    "https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Misc/Introduction.htm",
    # T24 Transact System Tables
    "https://docs.temenos.com/docs/Solutions/T24_Transact/Framework/ST/System_Tables/Misc/Introduction.htm",
]
SESSION_FILE   = "temenos_session.json"
OUTPUT_DIR     = Path("temenos_docs")
RAG_DIR        = Path("temenos_rag")
COMPILED_DIR   = Path("temenos_docs_compiled")
COMPILED_FILE  = COMPILED_DIR / "FULL_PAYMENTS.md"
VISITED_LOG    = Path("temenos_visited.txt")
NAV_LOG        = Path("temenos_nav.json")
DELAY_SECONDS  = 1.5
MAX_RETRIES    = 3
CHUNK_SIZE     = 1500
CHUNK_OVERLAP  = 200
MAX_PAGES      = 5000
LOGIN_FAIL_LIMIT = 10
IGNORED_FRAGMENTS = {
    "mc-main-content", "myScrollspy", "main-content", "content",
    "top", "header", "footer", "nav", "sidebar", "search",
    "skip-nav", "skip-to-content", "wrapper", "page-top",
    "navbar", "navigation", "menu", "toc",
}
# ─────────────────────────────────────────────────────────────


def normalize_url(url):
    parsed = urlparse(url)
    clean_path = parsed.path.rstrip("/")
    fragment = parsed.fragment.strip()
    if fragment.lower() in IGNORED_FRAGMENTS:
        fragment = ""
    return urlunparse((parsed.scheme, parsed.netloc, clean_path, "", "", fragment))


def base_url(url):
    """Return URL without fragment."""
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", ""))


def get_fragment(url):
    return urlparse(url).fragment.strip()


def is_allowed_url(url):
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc != BASE_DOMAIN:
        return False
    path = parsed.path
    if not any(path.startswith(prefix) for prefix in ALLOWED_PREFIXES):
        return False
    if path.endswith((".html", ".htm")):
        return True
    if not os.path.splitext(path)[1]:
        return True
    return False


# ═══════════════════════════════════════════════════════════════
#  STEP 1 — MANUAL LOGIN
# ═══════════════════════════════════════════════════════════════
async def do_login():
    from playwright.async_api import async_playwright
    print("\n" + "=" * 60)
    print("  STEP 1 -- MANUAL LOGIN")
    print("=" * 60)
    print("  A Chrome browser will open.")
    print("  Log in to docs.temenos.com normally.")
    print("  Once you can SEE the Payments page content,")
    print("  come back here and press ENTER.")
    print("=" * 60 + "\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(START_URL)
        input("  Press ENTER after you have logged in and see page content: ")
        cookies = await context.cookies()
        storage = await page.evaluate("() => JSON.stringify(window.localStorage)")
        session = {"cookies": cookies, "localStorage": storage}
        with open(SESSION_FILE, "w") as f:
            json.dump(session, f, indent=2)
        print(f"\n  Session saved -> '{SESSION_FILE}'")
        print("  Run:  python temenos_crawler_v2.py --crawl\n")
        await browser.close()


# ═══════════════════════════════════════════════════════════════
#  HELPER — restore session
# ═══════════════════════════════════════════════════════════════
async def restore_session(context, page):
    if not os.path.exists(SESSION_FILE):
        raise FileNotFoundError("Run --login first to save your session.")
    with open(SESSION_FILE) as f:
        session = json.load(f)
    await context.add_cookies(session["cookies"])
    await page.goto("https://docs.temenos.com")
    if session.get("localStorage"):
        try:
            items = json.loads(session["localStorage"])
            for k, v in items.items():
                await page.evaluate(
                    f"window.localStorage.setItem({json.dumps(k)}, {json.dumps(v)})"
                )
        except Exception:
            pass


# ═══════════════════════════════════════════════════════════════
#  HELPER — expand all sidebar/nav tree nodes
# ═══════════════════════════════════════════════════════════════
async def expand_nav_tree(page):
    """Click all expandable tree nodes in the sidebar to reveal hidden links."""
    expand_selectors = [
        ".tree-node-collapsed",
        ".nav-toggle",
        "[class*='expand']",
        "[class*='toggle']",
        "[class*='collapse'] > a",
        "[aria-expanded='false']",
        ".toc-toggle",
        ".MCToggler",
        "span.mc-icon",
        ".sidenav-toggle",
        "[data-mc-target-name]",
    ]

    max_rounds = 10
    for _ in range(max_rounds):
        clicked = 0
        for selector in expand_selectors:
            try:
                elements = await page.query_selector_all(selector)
                for el in elements[:100]:
                    try:
                        is_visible = await el.is_visible()
                        if is_visible:
                            await el.click(timeout=2000)
                            clicked += 1
                            await asyncio.sleep(0.1)
                    except Exception:
                        pass
            except Exception:
                pass

        if clicked == 0:
            break
        await asyncio.sleep(0.5)


# ═══════════════════════════════════════════════════════════════
#  HELPER — extract ALL links from page (nav + content + frames)
# ═══════════════════════════════════════════════════════════════
async def extract_all_links(page):
    """Extract links from sidebar nav, page content, and iframes.
    Preserves #fragment links as separate targets."""
    current_url = page.url

    raw_links = await page.evaluate("""
        () => {
            const links = new Set();

            // All anchor tags — use getAttribute to preserve fragments
            document.querySelectorAll('a[href]').forEach(a => {
                // a.href gives absolute URL with fragment
                links.add(a.href);
                // Also grab raw href for relative fragment-only links
                const raw = a.getAttribute('href');
                if (raw) links.add(raw);
            });

            // Area maps
            document.querySelectorAll('area[href]').forEach(a => {
                links.add(a.href);
                const raw = a.getAttribute('href');
                if (raw) links.add(raw);
            });

            // Links from onclick handlers that contain URLs
            document.querySelectorAll('[onclick]').forEach(el => {
                const onclick = el.getAttribute('onclick') || '';
                const match = onclick.match(/['"]([^'"]*\\.html?(?:#[^'"]*)?)['"]/);
                if (match) links.add(match[1]);
                const locMatch = onclick.match(/location\\.href\s*=\s*['"]([^'"]+)['"]/);
                if (locMatch) links.add(locMatch[1]);
                const hashMatch = onclick.match(/location\\.hash\s*=\s*['"]#?([^'"]+)['"]/);
                if (hashMatch) links.add('#' + hashMatch[1]);
            });

            // data-href attributes
            document.querySelectorAll('[data-href]').forEach(el => {
                links.add(el.getAttribute('data-href'));
            });

            // MadCap/Flare-specific link sources
            document.querySelectorAll('[data-mc-target-name]').forEach(el => {
                const name = el.getAttribute('data-mc-target-name');
                if (name) links.add(name);
            });

            // Tab/accordion controls that switch content via hash
            document.querySelectorAll('[data-toggle][href], [data-target]').forEach(el => {
                const href = el.getAttribute('href') || el.getAttribute('data-target');
                if (href) links.add(href);
            });

            return Array.from(links);
        }
    """)

    # Also try to get links from iframes
    try:
        frames = page.frames
        for frame in frames:
            if frame == page.main_frame:
                continue
            try:
                frame_links = await frame.evaluate("""
                    () => Array.from(document.querySelectorAll('a[href]'))
                               .map(a => a.href)
                """)
                raw_links.extend(frame_links)
            except Exception:
                pass
    except Exception:
        pass

    found = set()
    for link in raw_links:
        if not link:
            continue
        # Resolve relative URLs (including fragment-only like "#section")
        absolute = urljoin(current_url, link)
        normalized = normalize_url(absolute)
        if is_allowed_url(normalized):
            found.add(normalized)

    return found


# ═══════════════════════════════════════════════════════════════
#  HELPER — extract breadcrumbs from page
# ═══════════════════════════════════════════════════════════════
async def extract_breadcrumbs(page):
    try:
        crumbs = await page.evaluate("""
            () => {
                const selectors = [
                    '.breadcrumb', '.breadcrumbs', '[class*="breadcrumb"]',
                    'ol.breadcrumb', '.MCBreadcrumbsBox', '[aria-label="breadcrumb"]'
                ];
                for (const sel of selectors) {
                    const el = document.querySelector(sel);
                    if (el) {
                        return Array.from(el.querySelectorAll('a, span, li'))
                                    .map(e => e.textContent.trim())
                                    .filter(t => t.length > 0 && t !== '>' && t !== '/');
                    }
                }
                return [];
            }
        """)
        return crumbs
    except Exception:
        return []


# ═══════════════════════════════════════════════════════════════
#  HELPER — extract section headings from page
# ═══════════════════════════════════════════════════════════════
async def extract_sections(page):
    try:
        sections = await page.evaluate("""
            () => {
                const headings = document.querySelectorAll('h1, h2, h3, h4');
                return Array.from(headings).map(h => ({
                    level: parseInt(h.tagName.charAt(1)),
                    text: h.textContent.trim()
                }));
            }
        """)
        return sections
    except Exception:
        return []


# ═══════════════════════════════════════════════════════════════
#  HELPER — page -> clean markdown
# ═══════════════════════════════════════════════════════════════
async def page_to_markdown(page, url):
    try:
        await page.wait_for_load_state("networkidle", timeout=15000)
    except Exception:
        pass

    fragment = get_fragment(url)

    content_html = await page.evaluate("""
        (fragment) => {
            // If there's a fragment, try to get that specific section first
            if (fragment) {
                // Try finding the element by id or name matching the fragment
                let target = document.getElementById(fragment) ||
                             document.querySelector('[name="' + fragment + '"]') ||
                             document.querySelector('[data-mc-target-name="' + fragment + '"]');
                if (target) {
                    // Walk up to find a meaningful container
                    let container = target;
                    while (container && container.innerText &&
                           container.innerText.trim().length < 100 &&
                           container.parentElement &&
                           container.parentElement !== document.body) {
                        container = container.parentElement;
                    }
                    if (container && container.innerText.trim().length > 50) {
                        return container.innerHTML;
                    }
                }

                // Try visible/active content panel (JS-driven tab/accordion navigation)
                const activePanels = document.querySelectorAll(
                    '.active-content, .tab-pane.active, [class*="active"][class*="content"],' +
                    '.MCDropDown.open, [style*="display: block"][class*="content"]'
                );
                for (const panel of activePanels) {
                    if (panel.innerText.trim().length > 50) {
                        return panel.innerHTML;
                    }
                }
            }

            // Standard content selectors
            const selectors = [
                'article', 'main', '.content', '#content',
                '.topic-content', '.body-content', '[role="main"]',
                '.MCBodyText', '.TopicBody', '.helpBody',
                '#mc-main-content', '.mc-body'
            ];
            for (const sel of selectors) {
                const el = document.querySelector(sel);
                if (el && el.innerText.trim().length > 50) return el.innerHTML;
            }
            // Fallback: remove nav/header/footer and use body
            ['nav', '.sidenav', '#nav', 'header', 'footer',
             '.MCBreadcrumbsBox', '.search-bar'].forEach(sel => {
                const el = document.querySelector(sel);
                if (el) el.remove();
            });
            return document.body.innerHTML;
        }
    """, fragment)

    title = await page.title()
    title = re.sub(r'\s*[-|]\s*Temenos.*$', '', title).strip()
    if not title:
        title = urlparse(url).path.split("/")[-1].replace(".html", "").replace("-", " ").title()
    if fragment:
        frag_label = fragment.replace("-", " ").replace("_", " ").title()
        title = f"{title} - {frag_label}"

    markdown_text = md_convert(
        content_html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style", "nav", "header", "footer", "form", "iframe"]
    )
    markdown_text = re.sub(r'\n{4,}', '\n\n\n', markdown_text).strip()
    markdown_text = re.sub(r'!\[.*?\]\(.*?\)', '', markdown_text)
    markdown_text = re.sub(r'\[([^\]]*)\]\(javascript:[^)]*\)', r'\1', markdown_text)
    markdown_text = re.sub(r'[ \t]+$', '', markdown_text, flags=re.MULTILINE)

    return title, f"# {title}\n\n> Source: {url}\n\n---\n\n{markdown_text}"


# ═══════════════════════════════════════════════════════════════
#  HELPER — safe slug from URL
# ═══════════════════════════════════════════════════════════════
def url_to_slug(url):
    parsed = urlparse(url)
    path = parsed.path
    for prefix in [
        "/docs/Solutions/Payments/Content/",
        "/docs/Solutions/Payments/",
        "/docs/Solutions/T24_Transact/",
        "/docs/Solutions/",
    ]:
        if path.startswith(prefix):
            path = path[len(prefix):]
            break
    path = path.replace("/", "__").replace(".html", "").replace(".htm", "")
    path = re.sub(r'[^\w\-_]', '_', path)
    fragment = parsed.fragment.strip()
    if fragment:
        clean_frag = re.sub(r'[^\w\-_]', '_', fragment)
        path = f"{path}__FRAG__{clean_frag}"
    return path or "index"


def _write_crawl_report(visited, all_seen, saved, failed):
    from datetime import datetime
    report_path = Path("temenos_crawl_report.txt")
    with open(report_path, "w", encoding="utf-8") as rpt:
        rpt.write("TEMENOS DOCS CRAWL REPORT\n")
        rpt.write(f"Date: {datetime.now().isoformat()}\n")
        rpt.write(f"Pages saved  : {saved}\n")
        rpt.write(f"Pages failed : {failed}\n")
        rpt.write(f"Total seen   : {len(all_seen)}\n")
        rpt.write("=" * 80 + "\n\n")

        rpt.write("SCRAPED LINKS (successfully downloaded):\n")
        rpt.write("-" * 80 + "\n")
        for i, v in enumerate(sorted(visited), 1):
            rpt.write(f"  {i:4d}. {v}\n")

        skipped = all_seen - visited
        if skipped:
            rpt.write(f"\nSKIPPED / FAILED LINKS:\n")
            rpt.write("-" * 80 + "\n")
            for i, s in enumerate(sorted(skipped), 1):
                rpt.write(f"  {i:4d}. {s}\n")


# ═══════════════════════════════════════════════════════════════
#  STEP 2 — DEEP RECURSIVE CRAWL
# ═══════════════════════════════════════════════════════════════
async def do_crawl():
    from playwright.async_api import async_playwright

    OUTPUT_DIR.mkdir(exist_ok=True)

    visited = set()
    if VISITED_LOG.exists():
        visited = set(VISITED_LOG.read_text().splitlines())
        print(f"  Resuming -- {len(visited)} pages already done.")

    nav_data = []
    if NAV_LOG.exists():
        try:
            with open(NAV_LOG) as f:
                nav_data = json.load(f)
        except json.JSONDecodeError:
            print("  temenos_nav.json is corrupted — rebuilding from scratch.")
            nav_data = []
    nav_slugs = {item["slug"] for item in nav_data}

    print("\n" + "=" * 60)
    print("  STEP 2 -- DEEP RECURSIVE CRAWL")
    print("=" * 60)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        )
        page = await context.new_page()

        print("  Restoring login session...")
        await restore_session(context, page)
        await page.goto(START_URL)
        await page.wait_for_load_state("networkidle", timeout=20000)

        if "login" in page.url.lower() or "account" in page.url.lower():
            print("\n  Session expired. Run --login again.\n")
            await browser.close()
            return

        print("  Session valid — starting deep crawl...\n")

        # Phase 1: Visit each seed URL, expand nav tree, collect links
        print("  Phase 1: Expanding navigation trees across seed pages...")
        nav_links = set()
        for seed in SEED_URLS:
            try:
                await page.goto(seed, wait_until="domcontentloaded", timeout=30000)
                await page.wait_for_load_state("networkidle", timeout=15000)
                await expand_nav_tree(page)
                links = await extract_all_links(page)
                nav_links.update(links)
                print(f"    {seed.split('/')[-1]}: +{len(links)} links")
            except Exception as e:
                print(f"    Could not seed from {seed}: {e}")
        print(f"  Total {len(nav_links)} unique links from nav trees\n")

        # Phase 2: BFS crawl starting from seed URLs + nav links
        queue = list(SEED_URLS)
        for link in sorted(nav_links):
            if link not in queue:
                queue.append(link)

        all_seen = set(visited) | set(queue)
        saved = len(visited)
        failed = 0
        login_fails = 0

        while queue and saved < MAX_PAGES:
            url = queue.pop(0)
            if url in visited:
                continue

            slug = url_to_slug(url)
            md_path = OUTPUT_DIR / f"{slug}.md"

            fragment = get_fragment(url)
            target_base = base_url(url)
            current_base = base_url(page.url)

            success = False
            for attempt in range(1, MAX_RETRIES + 1):
                try:
                    print(f"  [{saved + 1}] {url}")

                    if fragment and current_base == target_base:
                        await page.evaluate(f"window.location.hash = '{fragment}'")
                        await asyncio.sleep(1.5)
                        try:
                            await page.wait_for_load_state("networkidle", timeout=8000)
                        except Exception:
                            pass
                    else:
                        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                        await page.wait_for_load_state("networkidle", timeout=15000)

                    current_base = base_url(page.url)

                    if "login" in page.url.lower():
                        login_fails += 1
                        if login_fails >= LOGIN_FAIL_LIMIT:
                            print(f"\n  SESSION EXPIRED after {saved} pages.")
                            print("  Saving progress. Re-run --login then --crawl to resume.\n")
                            await browser.close()
                            # Write partial report before exit
                            _write_crawl_report(visited, all_seen, saved, failed)
                            return
                        print(f"       Redirected to login -- skipping ({login_fails}/{LOGIN_FAIL_LIMIT})")
                        break

                    login_fails = 0

                    body_len = await page.evaluate("() => document.body.innerText.trim().length")
                    if body_len < 30:
                        print("       Empty page -- skipping")
                        break

                    title, markdown = await page_to_markdown(page, url)
                    breadcrumbs = await extract_breadcrumbs(page)
                    sections = await extract_sections(page)

                    md_path.write_text(markdown, encoding="utf-8")

                    if slug not in nav_slugs:
                        nav_data.append({
                            "title": title,
                            "slug": slug,
                            "url": url,
                            "breadcrumbs": breadcrumbs,
                            "sections": [s["text"] for s in sections],
                        })
                        nav_slugs.add(slug)
                        with open(NAV_LOG, "w") as f:
                            json.dump(nav_data, f, indent=2, ensure_ascii=False)

                    with open(VISITED_LOG, "a") as vf:
                        vf.write(url + "\n")
                    visited.add(url)
                    saved += 1
                    success = True

                    # Discover new links from this page's content
                    page_links = await extract_all_links(page)
                    new_count = 0
                    for link in sorted(page_links):
                        if link not in all_seen:
                            queue.append(link)
                            all_seen.add(link)
                            new_count += 1
                    if new_count > 0:
                        print(f"       +{new_count} new links discovered")
                    break

                except Exception as e:
                    print(f"       Attempt {attempt}/{MAX_RETRIES}: {e}")
                    if attempt < MAX_RETRIES:
                        await asyncio.sleep(3)

            if not success and attempt == MAX_RETRIES:
                failed += 1
                print(f"       FAILED: {url}")

            await asyncio.sleep(DELAY_SECONDS)

        await browser.close()

    _write_crawl_report(visited, all_seen, saved, failed)

    print("\n" + "=" * 60)
    print(f"  CRAWL DONE")
    print(f"     Pages saved  : {saved}")
    print(f"     Pages failed : {failed}")
    print(f"     Total seen   : {len(all_seen)}")
    print(f"     Report       : temenos_crawl_report.txt")
    print(f"  Run:  python temenos_crawler_v2.py --rag")
    print("=" * 60 + "\n")


# ═══════════════════════════════════════════════════════════════
#  TEXT CHUNKING FOR RAG
# ═══════════════════════════════════════════════════════════════
def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Split text into overlapping chunks, preferring to break at paragraph
    or sentence boundaries."""
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size

        if end < len(text):
            # Try to break at paragraph boundary
            para_break = text.rfind("\n\n", start + chunk_size // 2, end)
            if para_break > start:
                end = para_break

            else:
                # Try sentence boundary
                for sep in [". ", ".\n", "? ", "!\n"]:
                    sent_break = text.rfind(sep, start + chunk_size // 2, end)
                    if sent_break > start:
                        end = sent_break + len(sep)
                        break

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        start = end - overlap
        if start >= len(text):
            break

    return chunks


def extract_heading_context(text, position):
    """Find the most recent heading before a given position in the text."""
    before = text[:position]
    headings = list(re.finditer(r'^(#{1,4})\s+(.+)$', before, re.MULTILINE))
    if headings:
        last = headings[-1]
        return last.group(2).strip()
    return ""


# ═══════════════════════════════════════════════════════════════
#  STEP 3 — BUILD RAG CHUNKS (JSONL + metadata)
# ═══════════════════════════════════════════════════════════════
def do_rag():
    RAG_DIR.mkdir(exist_ok=True)

    md_files = sorted(OUTPUT_DIR.glob("*.md"))
    if not md_files:
        print("  No .md files. Run --crawl first.")
        return

    nav_lookup = {}
    if NAV_LOG.exists():
        try:
            with open(NAV_LOG) as f:
                for item in json.load(f):
                    nav_lookup[item["slug"]] = item
        except (json.JSONDecodeError, KeyError):
            print("  temenos_nav.json is corrupted or missing — proceeding without nav metadata.")
            nav_lookup = {}

    print("\n" + "=" * 60)
    print("  STEP 3 -- BUILDING RAG CHUNKS")
    print("=" * 60)

    chunks_path = RAG_DIR / "chunks.jsonl"
    metadata_path = RAG_DIR / "metadata.json"

    all_metadata = []
    total_chunks = 0

    with open(chunks_path, "w", encoding="utf-8") as out:
        for md_file in md_files:
            try:
                raw = md_file.read_text(encoding="utf-8")
            except Exception as e:
                print(f"  Could not read {md_file.name}: {e}")
                continue

            slug = md_file.stem

            # Parse header from our markdown format
            title = slug.replace("__", " > ").replace("_", " ").title()
            source_url = ""
            lines = raw.split("\n")
            for line in lines[:5]:
                if line.startswith("# "):
                    title = line[2:].strip()
                if line.startswith("> Source:"):
                    source_url = line.replace("> Source:", "").strip()

            # Strip the header (title + source + ---) before chunking
            content_start = raw.find("---\n\n")
            if content_start > 0:
                body = raw[content_start + 5:]
            else:
                body = raw

            body = body.strip()
            if not body or len(body) < 20:
                continue

            nav_info = nav_lookup.get(slug, {})
            breadcrumbs = nav_info.get("breadcrumbs", [])
            sections = nav_info.get("sections", [])

            breadcrumb_str = " > ".join(breadcrumbs) if breadcrumbs else ""

            chunks = chunk_text(body)
            page_chunk_ids = []

            for i, chunk in enumerate(chunks):
                section_heading = extract_heading_context(body, body.find(chunk[:50]))
                chunk_id = hashlib.sha256(f"{slug}:{i}".encode()).hexdigest()[:16]

                doc = {
                    "id": chunk_id,
                    "doc_id": slug,
                    "chunk_index": i,
                    "total_chunks": len(chunks),
                    "title": title,
                    "section": section_heading,
                    "breadcrumbs": breadcrumb_str,
                    "source_url": source_url,
                    "content": chunk,
                    "metadata": {
                        "domain": "temenos_payments",
                        "doc_type": "product_documentation",
                        "sections": sections[:10],
                    }
                }

                out.write(json.dumps(doc, ensure_ascii=False) + "\n")
                page_chunk_ids.append(chunk_id)
                total_chunks += 1

            all_metadata.append({
                "doc_id": slug,
                "title": title,
                "url": source_url,
                "breadcrumbs": breadcrumbs,
                "sections": sections,
                "num_chunks": len(chunks),
                "chunk_ids": page_chunk_ids,
            })

            print(f"  {md_file.name} -> {len(chunks)} chunks")

    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_documents": len(all_metadata),
            "total_chunks": total_chunks,
            "chunk_size": CHUNK_SIZE,
            "chunk_overlap": CHUNK_OVERLAP,
            "source": "https://docs.temenos.com/docs/Solutions/Payments/",
            "documents": all_metadata,
        }, f, indent=2, ensure_ascii=False)

    size_mb = chunks_path.stat().st_size / (1024 * 1024)
    print(f"\n  RAG BUILD DONE")
    print(f"     Documents   : {len(all_metadata)}")
    print(f"     Chunks      : {total_chunks}")
    print(f"     JSONL file  : {chunks_path} ({size_mb:.2f} MB)")
    print(f"     Metadata    : {metadata_path}")
    print("=" * 60 + "\n")


# ═══════════════════════════════════════════════════════════════
#  STEP 4 — COMPILE TO SKILL MD
# ═══════════════════════════════════════════════════════════════
def do_compile():
    COMPILED_DIR.mkdir(exist_ok=True)
    md_files = sorted(OUTPUT_DIR.glob("*.md"))
    if not md_files:
        print("  No .md files. Run --crawl first.")
        return

    print("\n" + "=" * 60)
    print("  STEP 4 -- COMPILING CLAUDE SKILL FILE")
    print("=" * 60)

    header = """---
skill_name: temenos-payments-hub-docs
description: >
  Complete Temenos Payments Hub documentation for TPH, covering
  all payment types, SWIFT, SEPA, Instant Payments, configuration,
  processing flows, ISO 20022, and technical setup.
version: 2.0
source: https://docs.temenos.com/docs/Solutions/Payments/
---

# Temenos Payments Hub -- Full Documentation

"""
    parts = [header]
    total = 0
    for f in md_files:
        try:
            parts.append(f.read_text(encoding="utf-8"))
            parts.append("\n\n---\n\n")
            total += 1
            print(f"  {f.name}")
        except Exception as e:
            print(f"  {f.name}: {e}")

    COMPILED_FILE.write_text("\n".join(parts), encoding="utf-8")
    size_mb = COMPILED_FILE.stat().st_size / (1024 * 1024)
    print(f"\n  Skill file: {COMPILED_FILE}  ({size_mb:.1f} MB)")
    print("=" * 60 + "\n")


# ═══════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════
def main():
    parser = argparse.ArgumentParser(description="Temenos Docs Deep Crawler v2 (RAG-ready)")
    parser.add_argument("--login",   action="store_true", help="Step 1: Manual browser login")
    parser.add_argument("--crawl",   action="store_true", help="Step 2: Deep recursive crawl")
    parser.add_argument("--rag",     action="store_true", help="Step 3: Build RAG chunks (JSONL)")
    parser.add_argument("--compile", action="store_true", help="Step 4: Build Claude skill MD file")
    parser.add_argument("--all",     action="store_true", help="Run steps 2+3+4 (login first)")
    args = parser.parse_args()

    if args.login:
        asyncio.run(do_login())
    elif args.crawl:
        asyncio.run(do_crawl())
    elif args.rag:
        do_rag()
    elif args.compile:
        do_compile()
    elif args.all:
        asyncio.run(do_crawl())
        do_rag()
        do_compile()
    else:
        parser.print_help()
        print("\n  QUICK START:")
        print("  1.  python temenos_crawler_v2.py --login")
        print("  2.  python temenos_crawler_v2.py --crawl")
        print("  3.  python temenos_crawler_v2.py --rag")
        print("  4.  python temenos_crawler_v2.py --compile\n")


if __name__ == "__main__":
    main()
