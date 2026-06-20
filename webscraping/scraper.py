from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
import os
import sys
import time
import json
import hashlib

DOMAIN = "https://docs.temenos.com"
BASE_PATH = "/docs/Solutions/Payments/"
START_URL = DOMAIN + BASE_PATH + "Content/payments.html"
SCOPE_PREFIX = DOMAIN + BASE_PATH
LOGIN_DOMAIN = "tcspsts.temenos.com"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(SCRIPT_DIR, "storage_state.json")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "offline")
ASSETS_DIR = os.path.join(OUTPUT_DIR, "_assets")
PROGRESS_FILE = os.path.join(SCRIPT_DIR, "scrape_progress.json")

MAX_SESSION_AGE_HOURS = 4


def is_login_redirect(url):
    return LOGIN_DOMAIN in urlparse(url).netloc


def is_session_file_stale():
    if not os.path.exists(STATE_FILE):
        return True
    age_hours = (time.time() - os.path.getmtime(STATE_FILE)) / 3600
    if age_hours > MAX_SESSION_AGE_HOURS:
        print(f"Session file is {age_hours:.1f} hours old (limit: {MAX_SESSION_AGE_HOURS}h)")
        return True
    return False


def check_cookie_expiry():
    if not os.path.exists(STATE_FILE):
        return True
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)
    now = time.time()
    auth_cookies = [c for c in state.get("cookies", [])
                    if c["name"] in (".AspNet.Cookies", "MSISAuth")]
    if not auth_cookies:
        print("No auth cookies found in session file")
        return True
    for c in state.get("cookies", []):
        exp = c.get("expires", -1)
        if exp > 0 and exp < now:
            print(f"Cookie '{c['name']}' expired at {time.ctime(exp)}")
            return True
    return False


def validate_session_live(context):
    test_page = context.new_page()
    try:
        test_page.goto(START_URL, wait_until="networkidle", timeout=30000)
        time.sleep(2)
        current_url = test_page.url
        if is_login_redirect(current_url):
            print(f"Session invalid — redirected to login: {current_url}")
            return False
        title = test_page.title()
        if "sign in" in title.lower() or "login" in title.lower() or "adfs" in title.lower():
            print(f"Session invalid — landed on login page: {title}")
            return False
        print(f"Session valid — loaded: {title}")
        return True
    except Exception as e:
        print(f"Session check failed: {e}")
        return False
    finally:
        test_page.close()


def do_login(browser):
    print("\n" + "=" * 60)
    print("SESSION EXPIRED — Manual login required")
    print("=" * 60)
    print("A browser window will open. Please log in.")
    print("After successful login (you see the docs page),")
    print("come back here and press ENTER.")
    print("=" * 60)

    context = browser.new_context()
    page = context.new_page()
    page.goto(DOMAIN + "/")

    input("\nPress ENTER after logging in... ")

    final_url = page.url
    if is_login_redirect(final_url):
        print("WARNING: Still on login page. Try logging in again.")
        input("Press ENTER when done... ")

    context.storage_state(path=STATE_FILE)
    print(f"New session saved to {STATE_FILE}")

    page.close()
    context.close()

    new_context = browser.new_context(storage_state=STATE_FILE)
    return new_context


def ensure_valid_session(browser, context):
    needs_login = False

    if is_session_file_stale():
        print("Session file is stale or missing")
        needs_login = True
    elif check_cookie_expiry():
        print("Cookies have expired")
        needs_login = True
    elif not validate_session_live(context):
        needs_login = True

    if needs_login:
        context.close()
        context = do_login(browser)
        if not validate_session_live(context):
            print("ERROR: Login failed. Exiting.")
            sys.exit(1)

    return context


def normalize_url(url):
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", parsed.query, ""))


def url_to_local_path(url):
    parsed = urlparse(url)
    path = parsed.path

    if path.startswith(BASE_PATH):
        path = path[len(BASE_PATH):]
    elif path.startswith("/"):
        path = path[1:]

    if not path or path.endswith("/"):
        path = path + "index.html"

    if "." not in os.path.basename(path):
        path = path + ".html"

    return os.path.join(OUTPUT_DIR, path.replace("/", os.sep))


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"Resuming: {len(data.get('visited', []))} pages already done")
            return set(data.get("visited", [])), data.get("failed", [])
    return set(), []


def save_progress(visited, failed):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump({"visited": list(visited), "failed": failed}, f, indent=2)


def download_asset(page, url, asset_cache):
    if url in asset_cache:
        return asset_cache[url]

    try:
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path) or "asset"
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        name, ext = os.path.splitext(filename)
        local_name = f"{name}_{url_hash}{ext}"
        local_path = os.path.join(ASSETS_DIR, local_name)

        if not os.path.exists(local_path):
            response = page.request.get(url)
            if response.ok:
                body = response.body()
                with open(local_path, "wb") as f:
                    f.write(body)
                print(f"    asset: {local_name} ({len(body)} bytes)")
            else:
                print(f"    asset skip (HTTP {response.status}): {url}")
                return None

        asset_cache[url] = local_path
        return local_path
    except Exception as e:
        print(f"    asset error: {url} -> {e}")
        return None


def relative_path(from_file, to_file):
    from_dir = os.path.dirname(from_file)
    return os.path.relpath(to_file, from_dir).replace(os.sep, "/")


def save_page_offline(page, url, html_path, asset_cache):
    html = page.content()
    soup = BeautifulSoup(html, "lxml")

    # Download and localize CSS stylesheets
    for link in soup.find_all("link", rel="stylesheet"):
        href = link.get("href")
        if href:
            abs_url = urljoin(url, href)
            local = download_asset(page, abs_url, asset_cache)
            if local:
                link["href"] = relative_path(html_path, local)

    # Download and localize images
    for img in soup.find_all("img"):
        src = img.get("src")
        if src and not src.startswith("data:"):
            abs_url = urljoin(url, src)
            local = download_asset(page, abs_url, asset_cache)
            if local:
                img["src"] = relative_path(html_path, local)

    # Download favicon / icon links
    for link in soup.find_all("link", rel=lambda r: r and "icon" in r):
        href = link.get("href")
        if href:
            abs_url = urljoin(url, href)
            local = download_asset(page, abs_url, asset_cache)
            if local:
                link["href"] = relative_path(html_path, local)

    # Rewrite internal navigation links to local paths
    for a in soup.find_all("a"):
        href = a.get("href")
        if not href or href.startswith(("#", "javascript:", "mailto:")):
            continue
        abs_href = normalize_url(urljoin(url, href))
        if abs_href.startswith(SCOPE_PREFIX):
            local_link = url_to_local_path(abs_href)
            a["href"] = relative_path(html_path, local_link)

    # Remove scripts that would fail offline (analytics, tracking)
    for script in soup.find_all("script"):
        src = script.get("src", "")
        if any(tracker in src for tracker in ["analytics", "google", "gtag", "tracking", "hotjar"]):
            script.decompose()

    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))


def crawl(browser, context, start_url):
    visited, failed = load_progress()
    asset_cache = {}
    queue = [normalize_url(start_url)]
    page = context.new_page()
    consecutive_auth_failures = 0

    while queue:
        url = queue.pop(0)

        if url in visited:
            continue

        visited.add(url)
        count = len(visited)

        print(f"\n[{count}] {url}")

        try:
            response = page.goto(url, wait_until="networkidle", timeout=60000)

            if response and not response.ok:
                print(f"  HTTP {response.status} — skipping")
                failed.append({"url": url, "error": f"HTTP {response.status}"})
                continue

            time.sleep(2)

            # Detect mid-crawl session expiry
            if is_login_redirect(page.url):
                print("  Session expired mid-crawl — re-authenticating...")
                save_progress(visited, failed)
                visited.discard(url)
                queue.insert(0, url)

                page.close()
                context.close()
                context = do_login(browser)
                page = context.new_page()

                consecutive_auth_failures += 1
                if consecutive_auth_failures >= 3:
                    print("ERROR: Login keeps failing. Exiting.")
                    break
                continue

            page_title = page.title().lower()
            if "sign in" in page_title or "login" in page_title:
                print("  Landed on login page — session may have expired")
                save_progress(visited, failed)
                visited.discard(url)
                queue.insert(0, url)

                page.close()
                context.close()
                context = do_login(browser)
                page = context.new_page()

                consecutive_auth_failures += 1
                if consecutive_auth_failures >= 3:
                    print("ERROR: Login keeps failing. Exiting.")
                    break
                continue

            consecutive_auth_failures = 0

            html_path = url_to_local_path(url)

            # Collect internal links before saving
            html = page.content()
            soup = BeautifulSoup(html, "lxml")

            for a in soup.find_all("a"):
                href = a.get("href")
                if not href or href.startswith(("#", "javascript:", "mailto:")):
                    continue
                abs_href = normalize_url(urljoin(url, href))
                if abs_href.startswith(SCOPE_PREFIX) and abs_href not in visited:
                    queue.append(abs_href)

            # Save the page with localized assets
            save_page_offline(page, url, html_path, asset_cache)
            print(f"  saved: {os.path.relpath(html_path, OUTPUT_DIR)}")

        except Exception as e:
            print(f"  ERROR: {e}")
            failed.append({"url": url, "error": str(e)})

        # Save progress every 10 pages
        if count % 10 == 0:
            save_progress(visited, failed)

    page.close()
    save_progress(visited, failed)
    return visited, failed


def main():
    fresh = "--fresh" in sys.argv

    if fresh:
        if os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)
            print("Cleared previous progress — starting fresh")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(ASSETS_DIR, exist_ok=True)

    print(f"Scraping: {SCOPE_PREFIX}")
    print(f"Output:   {OUTPUT_DIR}")
    print()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Load existing session or prompt login
        if os.path.exists(STATE_FILE) and not is_session_file_stale() and not check_cookie_expiry():
            context = browser.new_context(storage_state=STATE_FILE)
        else:
            context = do_login(browser)

        # Validate the session actually works against the live site
        context = ensure_valid_session(browser, context)

        visited, failed = crawl(browser, context, START_URL)

        context.close()
        browser.close()

    print("\n" + "=" * 60)
    print(f"Done: {len(visited)} pages scraped")
    if failed:
        print(f"Failed: {len(failed)} pages")
        for f in failed:
            print(f"  {f['url']}: {f['error']}")
    print(f"\nOffline site saved to: {OUTPUT_DIR}")
    print("Open offline/Content/payments.html in a browser to browse offline")


if __name__ == "__main__":
    main()
