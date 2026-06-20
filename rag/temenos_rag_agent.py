"""
Temenos Payments Hub — Agentic RAG Consultant (Ollama)
======================================================
Interactive Q&A with 4 modes: consultant, solution, fitment, testcase.
Uses ChromaDB for retrieval + local Ollama LLM with streaming output.

USAGE
-----
  python temenos_rag_agent.py --ingest                    # load chunks into ChromaDB
  python temenos_rag_agent.py --chat                      # interactive Q&A (streaming)
  python temenos_rag_agent.py --query "your question"     # single question
  python temenos_rag_agent.py --chat --model mistral      # use different model
"""

import argparse
import json
import sys
from pathlib import Path

CHUNKS_FILE = Path("temenos_rag/chunks.jsonl")
CHROMA_DIR = Path("temenos_chroma_db")
COLLECTION_NAME = "temenos_payments"
EMBED_MODEL = "all-MiniLM-L6-v2"
OLLAMA_MODEL = "phi3:mini"
OLLAMA_BASE_URL = "http://localhost:11434"
NUM_CTX = 4096
TOP_K = 5
RELEVANCE_THRESHOLD = 1.2

MODE_PROMPTS = {
    "consultant": (
        "You are a Temenos Payments Hub (TPH) expert consultant. "
        "Answer using ONLY the provided documentation context. "
        "Cite the source document/section. Be precise and technical. "
        "Use Temenos terminology (PI, PP, DB, POR, etc.). "
        "If context lacks info, say so clearly."
    ),
    "solution": (
        "You are a Temenos Payments Hub solution architect. "
        "The user describes a business requirement. "
        "Map it to specific TPH modules, payment order types (PI, DB, PP), "
        "and clearing options (SWIFT, SEPA, FPS, TARGET2, etc.). "
        "Outline the end-to-end flow. Flag gaps needing customization. "
        "Use ONLY the provided documentation context."
    ),
    "fitment": (
        "You are a Temenos Payments Hub core fitment assessor. "
        "Compare stated requirements against TPH capabilities from the documentation. "
        "Produce a fitment table: Requirement | TPH Feature | Fit (Full/Partial/Gap). "
        "For partial fits, explain customization needed. Rate overall fitment %. "
        "Use ONLY the provided documentation context."
    ),
    "testcase": (
        "You are a Temenos Payments Hub test case generator. "
        "Generate structured test cases with: ID, Title, Preconditions, Steps, "
        "Expected Result, Priority (High/Medium/Low). "
        "Cover positive, negative, boundary, and edge cases. "
        "Include test data (amounts, currencies, BICs, IBANs). "
        "Map to TPH modules. Use ONLY the provided documentation context."
    ),
}


def load_chunks():
    if not CHUNKS_FILE.exists():
        print(f"  {CHUNKS_FILE} not found. Run: python temenos_crawler_v2.py --rag")
        sys.exit(1)
    chunks = []
    with open(CHUNKS_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))
    return chunks


def do_ingest():
    import chromadb
    from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

    print("\n  Loading chunks...")
    chunks = load_chunks()
    print(f"  Loaded {len(chunks)} chunks from {CHUNKS_FILE}")

    embed_fn = SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    existing = [c.name for c in client.list_collections()]
    if COLLECTION_NAME in existing:
        client.delete_collection(COLLECTION_NAME)
        print(f"  Cleared existing collection '{COLLECTION_NAME}'")

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embed_fn,
        metadata={"hnsw:space": "cosine"},
    )

    batch_size = 500
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        ids = [c["id"] for c in batch]
        documents = [c["content"] for c in batch]
        metadatas = [
            {
                "doc_id": c["doc_id"],
                "title": c["title"],
                "section": c.get("section", ""),
                "source_url": c.get("source_url", ""),
                "chunk_index": c["chunk_index"],
                "total_chunks": c["total_chunks"],
            }
            for c in batch
        ]
        collection.add(ids=ids, documents=documents, metadatas=metadatas)
        print(f"  Ingested {min(i + batch_size, len(chunks))}/{len(chunks)} chunks")

    print(f"\n  Ingestion complete. ChromaDB stored at: {CHROMA_DIR}/")
    print(f"  Collection: {COLLECTION_NAME} ({collection.count()} vectors)")


def get_retriever():
    import chromadb
    from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

    embed_fn = SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = client.get_collection(
        name=COLLECTION_NAME,
        embedding_function=embed_fn,
    )
    return collection


def retrieve_context(collection, query, top_k=TOP_K):
    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    contexts = []
    sources = set()
    distances = results.get("distances", [[]])[0]

    for i, doc in enumerate(results["documents"][0]):
        dist = distances[i] if i < len(distances) else 999
        if dist > RELEVANCE_THRESHOLD:
            continue
        meta = results["metadatas"][0][i]
        title = meta.get("title", "")
        section = meta.get("section", "")
        url = meta.get("source_url", "")
        header = f"[{title}"
        if section:
            header += f" > {section}"
        header += "]"
        contexts.append(f"{header}\n{doc}")
        if url:
            sources.add(url)

    if not contexts:
        return None, []
    return "\n\n---\n\n".join(contexts), sorted(sources)


def stream_response(llm, prompt_messages):
    sys.stdout.write("  Assistant: ")
    sys.stdout.flush()
    full = []
    for chunk in llm.stream(prompt_messages):
        text = chunk.content
        if text:
            sys.stdout.write(text)
            sys.stdout.flush()
            full.append(text)
    sys.stdout.write("\n")
    return "".join(full)


def do_query(question, mode="consultant"):
    from langchain_ollama import ChatOllama
    from langchain_core.messages import SystemMessage, HumanMessage

    collection = get_retriever()
    print(f"\n  Searching {collection.count()} chunks...\n")

    context, sources = retrieve_context(collection, question)

    if context is None:
        print("  No relevant documents found for this query.\n")
        return

    llm = ChatOllama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0.1,
        num_ctx=NUM_CTX,
    )

    messages = [
        SystemMessage(content=MODE_PROMPTS.get(mode, MODE_PROMPTS["consultant"])),
        HumanMessage(content=f"Documentation context:\n\n{context}\n\n---\nQuestion: {question}"),
    ]

    stream_response(llm, messages)

    if sources:
        print("\n  Sources:")
        for src in sources:
            print(f"    - {src}")
    print()


def do_chat(mode="consultant"):
    from langchain_ollama import ChatOllama
    from langchain_core.messages import SystemMessage, HumanMessage

    collection = get_retriever()

    llm = ChatOllama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0.1,
        num_ctx=NUM_CTX,
    )

    print("\n" + "=" * 60)
    print("  TEMENOS PAYMENTS HUB — RAG CONSULTANT")
    print("=" * 60)
    print(f"  Chunks : {collection.count()}")
    print(f"  Model  : {OLLAMA_MODEL} (local Ollama)")
    print(f"  Mode   : {mode}")
    print()
    print("  Commands:")
    print("    /mode consultant  — general Q&A (default)")
    print("    /mode solution    — solution architecture")
    print("    /mode fitment     — core fitment assessment")
    print("    /mode testcase    — test case generation")
    print("    quit              — exit")
    print("=" * 60 + "\n")

    current_mode = mode

    while True:
        try:
            question = input("  You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye!")
            break

        if not question:
            continue
        if question.lower() in ("quit", "exit", "q"):
            print("  Goodbye!")
            break

        if question.startswith("/mode "):
            new_mode = question.split("/mode ", 1)[1].strip().lower()
            if new_mode in MODE_PROMPTS:
                current_mode = new_mode
                print(f"  Switched to: {current_mode}\n")
            else:
                print(f"  Unknown mode. Available: {', '.join(MODE_PROMPTS.keys())}\n")
            continue

        context, sources = retrieve_context(collection, question)

        if context is None:
            print("  Assistant: No relevant documents found for this query.\n")
            continue

        print()
        messages = [
            SystemMessage(content=MODE_PROMPTS[current_mode]),
            HumanMessage(content=f"Documentation context:\n\n{context}\n\n---\nQuestion: {question}"),
        ]

        stream_response(llm, messages)

        if sources:
            print("\n  Sources:")
            for src in sources[:5]:
                print(f"    - {src}")
        print()


def main():
    global OLLAMA_MODEL, NUM_CTX

    parser = argparse.ArgumentParser(description="Temenos Payments Hub — RAG Consultant")
    parser.add_argument("--ingest", action="store_true", help="Load chunks into ChromaDB")
    parser.add_argument("--chat", action="store_true", help="Interactive Q&A (streaming)")
    parser.add_argument("--query", type=str, help="Single question")
    parser.add_argument("--model", type=str, default=OLLAMA_MODEL, help=f"Ollama model (default: {OLLAMA_MODEL})")
    parser.add_argument("--mode", type=str, default="consultant",
                        choices=["consultant", "solution", "fitment", "testcase"],
                        help="Consultant mode (default: consultant)")
    parser.add_argument("--ctx", type=int, default=NUM_CTX, help=f"Context window size (default: {NUM_CTX})")
    args = parser.parse_args()

    OLLAMA_MODEL = args.model
    NUM_CTX = args.ctx

    if args.ingest:
        do_ingest()
    elif args.chat:
        do_chat(mode=args.mode)
    elif args.query:
        do_query(args.query, mode=args.mode)
    else:
        parser.print_help()
        print("\n  QUICK START:")
        print("  1.  python temenos_rag_agent.py --ingest")
        print("  2.  python temenos_rag_agent.py --chat")
        print()
        print("  MODES:")
        print("  python temenos_rag_agent.py --chat --mode consultant   # general Q&A")
        print("  python temenos_rag_agent.py --chat --mode solution     # solution design")
        print("  python temenos_rag_agent.py --chat --mode fitment      # core fitment")
        print("  python temenos_rag_agent.py --chat --mode testcase     # test cases")
        print()
        print("  OPTIONS:")
        print("  --model mistral    # use different Ollama model")
        print("  --ctx 8192         # increase context window (slower)")
        print()


if __name__ == "__main__":
    main()
