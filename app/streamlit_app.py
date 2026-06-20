"""
Temenos Payments Hub — Agentic RAG Consultant (Streamlit + Groq)
Cloud-deployable version using Groq API for fast inference.
"""

import json
import os
import sys
import streamlit as st
from pathlib import Path

CHUNKS_FILE = Path(__file__).parent.parent / "rag" / "chunks.jsonl"
CHROMA_DIR = Path(__file__).parent.parent / "rag" / "chroma_db"
COLLECTION_NAME = "temenos_payments"
EMBED_MODEL = "all-MiniLM-L6-v2"
TOP_K = 5
RELEVANCE_THRESHOLD = 1.2

MODE_PROMPTS = {
    "Payment Consultant": (
        "You are a Temenos Payments Hub (TPH) expert consultant. "
        "Answer using ONLY the provided documentation context. "
        "Cite the source document/section. Be precise and technical. "
        "Use Temenos terminology (PI, PP, DB, POR, etc.). "
        "If context lacks info, say so clearly."
    ),
    "Solution Provider": (
        "You are a Temenos Payments Hub solution architect. "
        "The user describes a business requirement. "
        "Map it to specific TPH modules, payment order types (PI, DB, PP), "
        "and clearing options (SWIFT, SEPA, FPS, TARGET2, etc.). "
        "Outline the end-to-end flow. Flag gaps needing customization. "
        "Use ONLY the provided documentation context."
    ),
    "Core Fitment Assessor": (
        "You are a Temenos Payments Hub core fitment assessor. "
        "Compare stated requirements against TPH capabilities from the documentation. "
        "Produce a fitment table: Requirement | TPH Feature | Fit (Full/Partial/Gap). "
        "For partial fits, explain customization needed. Rate overall fitment %. "
        "Use ONLY the provided documentation context."
    ),
    "Test Case Generator": (
        "You are a Temenos Payments Hub test case generator. "
        "Generate structured test cases with: ID, Title, Preconditions, Steps, "
        "Expected Result, Priority (High/Medium/Low). "
        "Cover positive, negative, boundary, and edge cases. "
        "Include test data (amounts, currencies, BICs, IBANs). "
        "Map to TPH modules. Use ONLY the provided documentation context."
    ),
}


@st.cache_resource
def load_collection():
    import chromadb
    from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

    embed_fn = SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    existing = [c.name for c in client.list_collections()]
    if COLLECTION_NAME not in existing:
        st.info("First run — indexing documents. This takes ~1 minute...")
        collection = client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=embed_fn,
            metadata={"hnsw:space": "cosine"},
        )
        chunks = []
        with open(CHUNKS_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    chunks.append(json.loads(line))

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
        return collection
    else:
        return client.get_collection(name=COLLECTION_NAME, embedding_function=embed_fn)


def retrieve_context(collection, query):
    results = collection.query(
        query_texts=[query],
        n_results=TOP_K,
        include=["documents", "metadatas", "distances"],
    )
    contexts = []
    sources = []
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
            sources.append({"title": title, "url": url})

    if not contexts:
        return None, []
    return "\n\n---\n\n".join(contexts), sources


def get_groq_client():
    from groq import Groq
    api_key = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", "")
    if not api_key:
        st.error("GROQ_API_KEY not set. Add it in Settings > Secrets on Streamlit Cloud.")
        st.stop()
    return Groq(api_key=api_key)


def stream_groq_response(client, system_prompt, context, question):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Documentation context:\n\n{context}\n\n---\nQuestion: {question}"},
    ]
    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.1,
        max_tokens=2048,
        stream=True,
    )
    for chunk in stream:
        text = chunk.choices[0].delta.content
        if text:
            yield text


def main():
    st.set_page_config(
        page_title="Temenos TPH Consultant",
        page_icon="🏦",
        layout="wide",
    )

    st.title("🏦 Temenos Payments Hub — AI Consultant")

    with st.sidebar:
        st.header("Mode")
        mode = st.radio(
            "Select consultant mode:",
            list(MODE_PROMPTS.keys()),
            index=0,
        )

        st.markdown("---")
        st.markdown(f"**Active mode:** {mode}")
        st.markdown("""
        **Modes:**
        - 🔍 **Consultant** — Answer TPH queries
        - 🏗️ **Solution** — Map requirements to TPH
        - 📊 **Fitment** — Assess TPH fit vs requirements
        - 🧪 **Test Cases** — Generate test scenarios
        """)

    collection = load_collection()

    with st.sidebar:
        st.markdown(f"📚 **{collection.count():,}** document chunks indexed")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if question := st.chat_input("Ask about Temenos Payments Hub..."):
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        context, sources = retrieve_context(collection, question)

        if context is None:
            response = "No relevant documents found for this query. Try rephrasing or asking about a different TPH topic."
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            client = get_groq_client()
            with st.chat_message("assistant"):
                response = st.write_stream(
                    stream_groq_response(client, MODE_PROMPTS[mode], context, question)
                )

                if sources:
                    st.markdown("---")
                    st.markdown("**📄 Sources:**")
                    for src in sources[:5]:
                        if src["url"]:
                            st.markdown(f"- [{src['title']}]({src['url']})")
                        else:
                            st.markdown(f"- {src['title']}")

            source_text = ""
            if sources:
                source_text = "\n\n---\n**Sources:** " + ", ".join(s["title"] for s in sources[:5])
            st.session_state.messages.append({"role": "assistant", "content": response + source_text})


if __name__ == "__main__":
    main()
