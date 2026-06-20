"""
Temenos Payments Hub — Agentic RAG Consultant (Streamlit + Groq)
Uses in-memory vector search (no ChromaDB) for maximum compatibility.
"""

import json
import os
import re
import numpy as np
import streamlit as st
from pathlib import Path

CHUNKS_FILE = Path(__file__).parent.parent / "rag" / "chunks.jsonl"
TOP_K = 8

STOP_WORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "shall", "can", "need", "must", "to", "of",
    "in", "for", "on", "with", "at", "by", "from", "as", "into", "about",
    "it", "its", "this", "that", "these", "those", "what", "which", "how",
    "when", "where", "who", "whom", "why", "and", "or", "but", "not", "no",
    "all", "each", "any", "both", "few", "more", "most", "some", "such",
    "than", "too", "very", "just", "also", "me", "my", "we", "our", "you",
    "your", "i", "provide", "generate", "create", "give", "show", "list",
    "explain", "describe", "tell", "write", "make", "find", "get", "use",
    "test", "cases", "case", "work", "works", "working", "does",
}

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


def extract_key_terms(query):
    words = re.findall(r'[a-zA-Z0-9_\-/]+', query)
    terms = []
    for w in words:
        if w.lower() not in STOP_WORDS and len(w) >= 2:
            terms.append(w.lower())
    return terms


@st.cache_resource
def load_knowledge_base():
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("all-MiniLM-L6-v2")

    chunks = []
    with open(CHUNKS_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))

    texts = [c["content"] for c in chunks]
    embeddings = model.encode(texts, show_progress_bar=False, batch_size=128)
    embeddings = np.array(embeddings, dtype=np.float32)

    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms[norms == 0] = 1
    embeddings = embeddings / norms

    search_texts = []
    for c in chunks:
        combined = " ".join([
            c.get("content", ""),
            c.get("title", ""),
            c.get("section", ""),
            c.get("breadcrumbs", ""),
        ]).lower()
        search_texts.append(combined)

    return model, chunks, embeddings, search_texts


def retrieve_context(model, chunks, embeddings, search_texts, query, top_k=TOP_K):
    key_terms = extract_key_terms(query)

    query_emb = model.encode([query])
    query_emb = np.array(query_emb, dtype=np.float32)
    query_norm = np.linalg.norm(query_emb)
    if query_norm > 0:
        query_emb = query_emb / query_norm

    semantic_scores = np.dot(embeddings, query_emb.T).flatten()

    keyword_scores = np.zeros(len(chunks), dtype=np.float32)
    if key_terms:
        for i, text in enumerate(search_texts):
            matches = sum(1 for term in key_terms if term in text)
            keyword_scores[i] = matches / len(key_terms)

    if key_terms:
        final_scores = semantic_scores * 0.5 + keyword_scores * 0.5
    else:
        final_scores = semantic_scores

    candidate_count = top_k * 4
    top_indices = np.argsort(final_scores)[::-1][:candidate_count]

    results = []
    for idx in top_indices:
        if final_scores[idx] < 0.3:
            continue
        results.append((idx, final_scores[idx], semantic_scores[idx], keyword_scores[idx]))

    if key_terms:
        results.sort(key=lambda r: (r[3] > 0, r[1]), reverse=True)

    results = results[:top_k]

    contexts = []
    sources = []
    for idx, score, sem_score, kw_score in results:
        chunk = chunks[idx]
        title = chunk.get("title", "")
        section = chunk.get("section", "")
        url = chunk.get("source_url", "")
        header = f"[{title}"
        if section:
            header += f" > {section}"
        header += f"] (relevance: {score:.0%})"
        contexts.append(f"{header}\n{chunk['content']}")
        if url:
            sources.append({"title": title, "url": url, "score": float(score)})

    if not contexts:
        return None, []
    return "\n\n---\n\n".join(contexts), sources


def get_groq_client():
    from groq import Groq
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        try:
            api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            api_key = ""
    if not api_key:
        st.error("GROQ_API_KEY not set. Add it in Streamlit Cloud: Settings > Secrets.")
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
        st.markdown("""
        **Modes:**
        - 🔍 **Consultant** — Answer TPH queries
        - 🏗️ **Solution** — Map requirements to TPH
        - 📊 **Fitment** — Assess TPH fit
        - 🧪 **Test Cases** — Generate test scenarios
        """)

    with st.spinner("Loading knowledge base (first time takes ~1 min)..."):
        model, chunks, embeddings, search_texts = load_knowledge_base()

    with st.sidebar:
        st.markdown(f"📚 **{len(chunks):,}** document chunks loaded")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if question := st.chat_input("Ask about Temenos Payments Hub..."):
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        context, sources = retrieve_context(model, chunks, embeddings, search_texts, question)

        if context is None:
            response = "No relevant documents found. Try rephrasing or asking about a different TPH topic."
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
                            st.markdown(f"- [{src['title']}]({src['url']}) ({src['score']:.0%})")
                        else:
                            st.markdown(f"- {src['title']} ({src['score']:.0%})")

            source_text = ""
            if sources:
                source_text = "\n\n---\n**Sources:** " + ", ".join(s["title"] for s in sources[:5])
            st.session_state.messages.append({"role": "assistant", "content": response + source_text})


if __name__ == "__main__":
    main()
