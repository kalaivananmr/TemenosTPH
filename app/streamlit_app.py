"""
Temenos Payments Hub — Agentic RAG Consultant (Streamlit + Groq)
Two-agent architecture: Validator Agent checks context relevance,
Response Agent generates answer only if context is verified.
"""

import json
import os
import re
import numpy as np
import streamlit as st
from pathlib import Path

CHUNKS_FILE = Path(__file__).parent.parent / "rag" / "chunks.jsonl"
TOP_K = 8
MIN_KEYWORD_MATCH = 0.7

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
    "temenos", "tph", "payments", "hub", "payment",
}

SYNONYMS = {
    "indian": "india", "american": "united states", "usa": "united states",
    "us": "united states", "british": "united kingdom", "uk": "united kingdom",
    "sri lankan": "sri lanka", "australian": "australia", "european": "europe",
    "argentinian": "argentina", "argentine": "argentina",
    "hong kong": "hongkong", "hk": "hongkong",
    "israeli": "israel", "african": "africa", "tunisian": "tunisia",
    "lebanese": "lebanon", "nordic": "nordic", "spanish": "iberpay",
    "swiss": "sic", "german": "equens",
    "ct": "credit transfer", "dd": "direct debit",
    "fps": "faster payments", "ips": "instant payments",
}

MODE_PROMPTS = {
    "Payment Consultant": (
        "You are a Temenos Payments Hub (TPH) expert consultant. "
        "Answer using ONLY the provided documentation context. "
        "Cite the source document/section. Be precise and technical. "
        "Use Temenos terminology (PI, PP, DB, POR, etc.). "
        "IMPORTANT: If the context does not contain specific information "
        "to answer the question, you MUST say so. Do NOT guess or infer."
    ),
    "Solution Provider": (
        "You are a Temenos Payments Hub solution architect. "
        "Map requirements to specific TPH modules and clearing options. "
        "Use ONLY the provided documentation context. "
        "IMPORTANT: If the context does not cover the specific clearing/country "
        "asked about, say the information is not available. Do NOT substitute "
        "information from a different clearing or country."
    ),
    "Core Fitment Assessor": (
        "You are a Temenos Payments Hub core fitment assessor. "
        "Produce a fitment table: Requirement | TPH Feature | Fit (Full/Partial/Gap). "
        "Use ONLY the provided documentation context. "
        "IMPORTANT: If a requirement cannot be assessed from the context, "
        "mark it as 'No documentation available' — do NOT guess."
    ),
    "Test Case Generator": (
        "You are a Temenos Payments Hub test case generator. "
        "Generate test cases with: ID, Title, Preconditions, Steps, "
        "Expected Result, Priority. Include test data. "
        "Use ONLY the provided documentation context. "
        "IMPORTANT: Generate test cases ONLY for the specific system/clearing "
        "mentioned in the context. If context is about NEFT, generate for NEFT only. "
        "Do NOT create test cases using information from a different clearing system."
    ),
}

VALIDATOR_PROMPT = (
    "You are a strict relevance validator for a Temenos Payments Hub documentation system. "
    "Your job is to check if the retrieved documentation context ACTUALLY contains "
    "information that directly answers the user's question.\n\n"
    "Rules:\n"
    "- If the user asks about a SPECIFIC country or clearing system (e.g. 'Indian RTGS', 'SEPA'), "
    "the context MUST contain information about THAT EXACT country/clearing. "
    "Documentation about a DIFFERENT country's RTGS or a different clearing is NOT relevant.\n"
    "- If the user asks about a specific feature, the context must describe that feature.\n"
    "- Partial or tangential matches are NOT acceptable.\n\n"
    "Respond with ONLY a JSON object (no markdown, no extra text):\n"
    '{"relevant": true/false, "reason": "one sentence explanation"}\n\n'
    "Examples:\n"
    '- User asks "Indian RTGS", context has Sri Lanka RTGS → {"relevant": false, "reason": "Context contains Sri Lanka RTGS, not Indian RTGS"}\n'
    '- User asks "SEPA credit transfer", context has SEPA credit transfer docs → {"relevant": true, "reason": "Context directly covers SEPA credit transfer"}\n'
    '- User asks "Indian NEFT", context has India NEFT clearing → {"relevant": true, "reason": "Context covers India NEFT clearing"}\n'
)

NO_INFO_MSG = (
    "**No information available.**\n\n"
    "The Temenos Payments Hub documentation in our knowledge base does not contain "
    "specific information to answer this question. This could mean:\n"
    "- This topic/clearing system was not covered in the crawled documentation\n"
    "- The specific country or feature may not be supported by TPH\n"
    "- Try rephrasing with the exact Temenos terminology (e.g., 'NEFT' instead of 'Indian RTGS')"
)


def extract_key_terms(query):
    query_lower = query.lower()
    for phrase, replacement in SYNONYMS.items():
        if phrase in query_lower:
            query_lower = query_lower.replace(phrase, f"{phrase} {replacement}")

    words = re.findall(r'[a-zA-Z0-9_\-/]+', query_lower)
    terms = []
    seen = set()
    for w in words:
        if w not in STOP_WORDS and len(w) >= 2 and w not in seen:
            terms.append(w)
            seen.add(w)
    return terms


def keyword_match_score(terms, text):
    if not terms:
        return 0.0
    score = 0.0
    for term in terms:
        if term in text:
            score += 1.0
        elif len(term) >= 4:
            if any(term in word or word in term for word in text.split()):
                score += 0.5
    return score / len(terms)


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
            c.get("doc_id", "").replace("__", " ").replace("_", " "),
            c.get("source_url", "").replace("/", " ").replace("_", " "),
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
            keyword_scores[i] = keyword_match_score(key_terms, text)

    if key_terms:
        final_scores = semantic_scores * 0.3 + keyword_scores * 0.7
    else:
        final_scores = semantic_scores

    candidate_count = top_k * 5
    top_indices = np.argsort(final_scores)[::-1][:candidate_count]

    results = []
    for idx in top_indices:
        if final_scores[idx] < 0.35:
            continue
        results.append((idx, final_scores[idx], semantic_scores[idx], keyword_scores[idx]))

    if key_terms:
        results = [r for r in results if r[3] >= MIN_KEYWORD_MATCH]
        results.sort(key=lambda r: (r[3], r[1]), reverse=True)

    results = results[:top_k]

    if not results:
        return None, []

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
        header += f"] (match: {kw_score:.0%})"
        contexts.append(f"{header}\n{chunk['content']}")
        if url and url not in [s["url"] for s in sources]:
            sources.append({"title": title, "url": url, "score": float(score)})

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


def validate_context(client, context, question):
    messages = [
        {"role": "system", "content": VALIDATOR_PROMPT},
        {"role": "user", "content": (
            f"User question: {question}\n\n"
            f"Retrieved documentation context:\n{context[:3000]}"
        )},
    ]
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.0,
        max_tokens=200,
    )
    result_text = response.choices[0].message.content.strip()

    try:
        clean = result_text
        if "```" in clean:
            clean = clean.split("```")[1].replace("json", "").strip()
        result = json.loads(clean)
        return result.get("relevant", False), result.get("reason", "")
    except (json.JSONDecodeError, IndexError):
        if "true" in result_text.lower():
            return True, result_text
        return False, result_text


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

        **Agents:**
        - 🛡️ **Validator** — Checks context relevance
        - 💬 **Responder** — Generates verified answer
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
            with st.chat_message("assistant"):
                st.markdown(NO_INFO_MSG)
            st.session_state.messages.append({"role": "assistant", "content": NO_INFO_MSG})
            return

        client = get_groq_client()

        with st.chat_message("assistant"):
            with st.status("🛡️ Validator Agent checking relevance...", expanded=False) as status:
                is_relevant, reason = validate_context(client, context, question)
                if is_relevant:
                    status.update(label=f"✅ Validated: {reason}", state="complete")
                else:
                    status.update(label=f"❌ Rejected: {reason}", state="error")

            if not is_relevant:
                rejection_msg = (
                    f"**No information available.**\n\n"
                    f"🛡️ **Validator Agent:** {reason}\n\n"
                    f"The retrieved documentation does not contain specific information "
                    f"to answer your question. Try rephrasing with exact Temenos terminology."
                )
                st.markdown(rejection_msg)
                st.session_state.messages.append({"role": "assistant", "content": rejection_msg})
            else:
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
