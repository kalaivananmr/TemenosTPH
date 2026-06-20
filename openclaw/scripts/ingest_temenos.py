#!/usr/bin/env python3
"""
Ingest Temenos scraped docs (markdown + HTML) into OpenClaw RAG ChromaDB.
"""

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "openclaw-rag-skill"))
from rag_system import RAGSystem

TEMENOS_BASE = Path(r"C:\Kalaivanan\TestcaseAI\Temenos")
MARKDOWN_DIR = TEMENOS_BASE / "temenos_docs"
RAG_CHUNKS_FILE = TEMENOS_BASE / "temenos_rag" / "chunks.jsonl"
NAV_FILE = TEMENOS_BASE / "temenos_nav.json"
HTML_DIR = Path(r"C:\Kalaivanan\TestcaseAI\webscraping\offline")

COLLECTION = "temenos_payments_kb"
CHUNK_SIZE = 2000
CHUNK_OVERLAP = 200


def chunk_text(text, max_chars=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    if len(text) <= max_chars:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chars
        if end < len(text):
            para_break = text.rfind("\n\n", start + max_chars // 2, end)
            if para_break > start:
                end = para_break
            else:
                for sep in [". ", ".\n", "? ", "!\n"]:
                    sent_break = text.rfind(sep, start + max_chars // 2, end)
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


def extract_text_from_html(html_content):
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, "lxml")
        for tag in soup(["script", "style", "nav", "header", "footer", "noscript"]):
            tag.decompose()
        for sel in [".sidenav", "#nav", ".breadcrumbs", ".search-bar", ".MCBreadcrumbsBox"]:
            for el in soup.select(sel):
                el.decompose()
        content = soup.find("main") or soup.find("article") or soup.find(id="mc-main-content") or soup.body
        if content:
            text = content.get_text(separator="\n", strip=True)
        else:
            text = soup.get_text(separator="\n", strip=True)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()
    except Exception as e:
        print(f"    HTML parse error: {e}")
        return None


def load_nav_metadata():
    if NAV_FILE.exists():
        try:
            with open(NAV_FILE, encoding="utf-8") as f:
                data = json.load(f)
                return {item["slug"]: item for item in data}
        except Exception:
            pass
    return {}


def ingest_markdown(rag):
    if not MARKDOWN_DIR.exists():
        print(f"  Markdown dir not found: {MARKDOWN_DIR}")
        return 0

    md_files = sorted(MARKDOWN_DIR.glob("*.md"))
    if not md_files:
        print("  No markdown files found")
        return 0

    nav_lookup = load_nav_metadata()
    total = 0

    print(f"  Found {len(md_files)} markdown files\n")

    for md_file in md_files:
        slug = md_file.stem
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  Skip {md_file.name}: {e}")
            continue

        title = slug.replace("__", " > ").replace("_", " ").title()
        source_url = ""
        for line in content.split("\n")[:5]:
            if line.startswith("# "):
                title = line[2:].strip()
            if line.startswith("> Source:"):
                source_url = line.replace("> Source:", "").strip()

        body_start = content.find("---\n\n")
        body = content[body_start + 5:] if body_start > 0 else content
        body = body.strip()

        if len(body) < 30:
            continue

        nav = nav_lookup.get(slug, {})
        breadcrumbs = " > ".join(nav.get("breadcrumbs", []))
        sections = nav.get("sections", [])

        chunks = chunk_text(body)

        for i, chunk in enumerate(chunks):
            doc_id = hashlib.sha256(f"md:{slug}:{i}".encode()).hexdigest()[:16]
            metadata = {
                "type": "markdown",
                "source": f"temenos:{slug}",
                "title": title,
                "breadcrumbs": breadcrumbs,
                "sections": ", ".join(sections[:5]),
                "source_url": source_url,
                "chunk_index": i,
                "total_chunks": len(chunks),
                "ingested_at": datetime.now().isoformat(),
            }
            rag.add_document(chunk, metadata, doc_id=doc_id)
            total += 1

        print(f"  {md_file.name} -> {len(chunks)} chunks")

    return total


def ingest_html(rag):
    if not HTML_DIR.exists():
        print(f"  HTML dir not found: {HTML_DIR}")
        print("  Run the webscraping/scraper.py first to create offline HTML pages")
        return 0

    html_files = sorted(HTML_DIR.rglob("*.html"))
    html_files = [f for f in html_files if "_assets" not in str(f)]

    if not html_files:
        print("  No HTML files found")
        return 0

    total = 0
    print(f"  Found {len(html_files)} HTML files\n")

    for html_file in html_files:
        try:
            content = html_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  Skip {html_file.name}: {e}")
            continue

        text = extract_text_from_html(content)
        if not text or len(text) < 50:
            continue

        rel_path = html_file.relative_to(HTML_DIR)
        slug = str(rel_path).replace("\\", "/").replace("/", "__").replace(".html", "").replace(".htm", "")

        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(content, "lxml")
            title = soup.title.text.strip() if soup.title else slug
            title = re.sub(r'\s*[-|]\s*Temenos.*$', '', title).strip()
        except Exception:
            title = slug

        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            doc_id = hashlib.sha256(f"html:{slug}:{i}".encode()).hexdigest()[:16]
            metadata = {
                "type": "html",
                "source": f"temenos-html:{slug}",
                "title": title,
                "file_path": str(rel_path),
                "chunk_index": i,
                "total_chunks": len(chunks),
                "ingested_at": datetime.now().isoformat(),
            }
            rag.add_document(chunk, metadata, doc_id=doc_id)
            total += 1

        print(f"  {rel_path} -> {len(chunks)} chunks")

    return total


def ingest_existing_rag_chunks(rag):
    if not RAG_CHUNKS_FILE.exists():
        print(f"  Chunks file not found: {RAG_CHUNKS_FILE}")
        return 0

    total = 0
    print(f"  Loading pre-built chunks from {RAG_CHUNKS_FILE}\n")

    with open(RAG_CHUNKS_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            chunk = json.loads(line)
            doc_id = f"rag_{chunk['id']}"
            metadata = {
                "type": "rag-chunk",
                "source": f"temenos-rag:{chunk.get('doc_id', '')}",
                "title": chunk.get("title", ""),
                "section": chunk.get("section", ""),
                "breadcrumbs": chunk.get("breadcrumbs", ""),
                "source_url": chunk.get("source_url", ""),
                "chunk_index": chunk.get("chunk_index", 0),
                "total_chunks": chunk.get("total_chunks", 1),
                "ingested_at": datetime.now().isoformat(),
            }
            rag.add_document(chunk["content"], metadata, doc_id=doc_id)
            total += 1

    print(f"  Loaded {total} pre-built RAG chunks")
    return total


def show_stats(rag):
    stats = rag.get_stats()
    print(f"\n  Collection: {stats['collection_name']}")
    print(f"  Total documents: {stats['total_documents']}")
    print(f"  Storage: {stats['persist_directory']}")

    all_docs = rag.collection.get(limit=stats['total_documents'], include=["metadatas"])
    type_counts = {}
    for meta in all_docs["metadatas"]:
        t = meta.get("type", "unknown")
        type_counts[t] = type_counts.get(t, 0) + 1

    if type_counts:
        print(f"\n  By type:")
        for t, c in sorted(type_counts.items()):
            print(f"    {t}: {c}")


def main():
    parser = argparse.ArgumentParser(description="Ingest Temenos docs into OpenClaw RAG")
    parser.add_argument("--markdown", action="store_true", help="Ingest markdown docs from temenos_docs/")
    parser.add_argument("--html", action="store_true", help="Ingest scraped HTML from webscraping/offline/")
    parser.add_argument("--chunks", action="store_true", help="Ingest pre-built RAG chunks from chunks.jsonl")
    parser.add_argument("--all", action="store_true", help="Ingest all sources")
    parser.add_argument("--reset", action="store_true", help="Reset collection before ingesting")
    parser.add_argument("--stats", action="store_true", help="Show collection statistics")
    args = parser.parse_args()

    if not any([args.markdown, args.html, args.chunks, args.all, args.stats, args.reset]):
        parser.print_help()
        print("\n  QUICK START:")
        print("  python scripts/ingest_temenos.py --all          # Ingest everything")
        print("  python scripts/ingest_temenos.py --stats        # Check what's indexed")
        print("  python scripts/ingest_temenos.py --reset --all  # Fresh re-ingest")
        return

    rag = RAGSystem(collection_name=COLLECTION)

    if args.reset:
        print("  Resetting collection...")
        rag.reset_collection()

    if args.stats and not any([args.markdown, args.html, args.chunks, args.all]):
        show_stats(rag)
        return

    total = 0

    if args.markdown or args.all:
        print("\n=== Ingesting Markdown Docs ===")
        total += ingest_markdown(rag)

    if args.chunks or args.all:
        print("\n=== Ingesting Pre-built RAG Chunks ===")
        total += ingest_existing_rag_chunks(rag)

    if args.html or args.all:
        print("\n=== Ingesting HTML Pages ===")
        total += ingest_html(rag)

    print(f"\n{'=' * 50}")
    print(f"  Total chunks ingested: {total}")
    show_stats(rag)


if __name__ == "__main__":
    main()
