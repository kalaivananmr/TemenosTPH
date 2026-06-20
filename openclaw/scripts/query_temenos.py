#!/usr/bin/env python3
"""
Query the Temenos knowledge base via OpenClaw RAG.
Used by the temenos-consultant skill to retrieve relevant documentation.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "openclaw-rag-skill"))
from rag_system import RAGSystem

COLLECTION = "temenos_payments_kb"


def query(question, doc_type=None, top_k=10, output_json=False):
    rag = RAGSystem(collection_name=COLLECTION)

    filters = None
    if doc_type:
        filters = {"type": doc_type}

    results = rag.search(query=question, n_results=top_k, filters=filters)

    if not results:
        if output_json:
            print(json.dumps({"results": [], "count": 0}))
        else:
            print("No relevant documents found.")
        return

    if output_json:
        output = {
            "count": len(results),
            "results": [
                {
                    "title": r["metadata"].get("title", ""),
                    "type": r["metadata"].get("type", ""),
                    "source": r["metadata"].get("source", ""),
                    "source_url": r["metadata"].get("source_url", ""),
                    "breadcrumbs": r["metadata"].get("breadcrumbs", ""),
                    "section": r["metadata"].get("section", ""),
                    "content": r["text"],
                }
                for r in results
            ],
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print(f"\nFound {len(results)} relevant chunks:\n")
        for i, r in enumerate(results, 1):
            meta = r["metadata"]
            title = meta.get("title", "Untitled")
            source = meta.get("source_url", "") or meta.get("source", "")
            doc_type_label = meta.get("type", "")
            section = meta.get("section", "")

            header = f"[{i}] {title}"
            if section:
                header += f" > {section}"
            header += f"  ({doc_type_label})"

            print(f"{header}")
            if source:
                print(f"    Source: {source}")
            print(f"    {r['text'][:300]}...")
            print()


def interactive_mode():
    rag = RAGSystem(collection_name=COLLECTION)
    count = rag.collection.count()

    print(f"\nTemenos Payments Knowledge Base")
    print(f"  {count} document chunks indexed")
    print(f"  Type 'quit' to exit\n")

    while True:
        try:
            q = input("  Query: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye!")
            break

        if not q or q.lower() in ("quit", "exit", "q"):
            break

        results = rag.search(query=q, n_results=8)

        if not results:
            print("  No results found.\n")
            continue

        print()
        for i, r in enumerate(results, 1):
            meta = r["metadata"]
            title = meta.get("title", "Untitled")
            print(f"  [{i}] {title} ({meta.get('type', '')})")
            print(f"      {r['text'][:200]}...")
            print()


def main():
    parser = argparse.ArgumentParser(description="Query Temenos knowledge base")
    parser.add_argument("question", nargs="?", help="Search query")
    parser.add_argument("--type", choices=["markdown", "html", "rag-chunk"], help="Filter by doc type")
    parser.add_argument("--top-k", type=int, default=10, help="Number of results (default: 10)")
    parser.add_argument("--json", action="store_true", help="Output as JSON (for agent use)")
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive search mode")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.question:
        query(args.question, doc_type=args.type, top_k=args.top_k, output_json=args.json)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
