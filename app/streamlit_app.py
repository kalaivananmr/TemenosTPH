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
    "possible", "using", "different", "used", "like", "want", "new",
    "based", "through", "between", "within", "after", "before",
    "specific", "available", "required", "related", "existing",
    "able", "allow", "allows", "process", "system", "support",
    "way", "type", "types", "set", "setting", "settings",
    "please", "help", "know", "understand", "check", "look",
    "want", "need", "try", "run", "start", "stop", "enable",
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
        "You are a Senior Temenos Payments & Banking Consultant with deep domain expertise.\n\n"
        "TASK: Search the provided RAG documentation context and answer the user's query "
        "professionally, accurately, and using proper banking and Temenos domain terminology "
        "(PI, PP, DB, POR, ISO 20022, pacs, pain, camt, etc.).\n\n"
        "RULES:\n"
        "- Stay grounded in the RAG context ONLY. Do NOT use outside knowledge.\n"
        "- Cite the source document/section for every claim.\n"
        "- If the RAG context does not contain the answer, say: "
        "'This information is not available in the current documentation.'\n"
        "- Do NOT guess, infer, or fabricate information.\n"
        "- Structure your response clearly with headings where appropriate."
    ),
    "Solution Provider": "SOLUTION_PROVIDER_MULTI_STEP",
    "Core Fitment Assessor": (
        "You are a Banking Fitment Analyst specializing in Temenos Payments Hub (TPH).\n\n"
        "TASK: For each requirement provided by the user, search the RAG documentation context "
        "and assess the fitment percentage based strictly on documented TPH capabilities.\n\n"
        "OUTPUT FORMAT — Produce a markdown table:\n"
        "| Requirement | Fitment % | Justification | Gap (if any) |\n"
        "|---|---|---|---|\n\n"
        "SCORING RULES:\n"
        "- 100% = Fully supported with documented evidence\n"
        "- 75% = Supported but requires configuration (cite what config)\n"
        "- 50% = Partially supported, customization needed (describe what)\n"
        "- 25% = Minimal support, significant development needed\n"
        "- 0% = Not found in documentation at all\n\n"
        "RULES:\n"
        "- Base ALL scoring strictly on RAG evidence. Do NOT assume capabilities.\n"
        "- Every Justification cell must cite the source document.\n"
        "- If a requirement has no matching documentation, score it 0% and state "
        "'No documentation found for this capability.'\n"
        "- After the table, provide an overall fitment summary with total weighted %."
    ),
    "Test Case Generator": (
        "You are a QA Engineer specializing in Temenos Payments Hub (TPH) testing.\n\n"
        "TASK: From the RAG documentation context, extract the navigation paths, "
        "workflow steps, screens, and field-level details relevant to the user's requirement. "
        "Generate structured test cases based ONLY on this extracted information.\n\n"
        "OUTPUT FORMAT — For each test case:\n"
        "| Field | Value |\n"
        "|---|---|\n"
        "| Test ID | TC-XXX |\n"
        "| Scenario | Clear description |\n"
        "| Preconditions | Setup required from docs |\n"
        "| Navigation | Menu path / screen from docs |\n"
        "| Steps | Numbered steps traced from RAG workflow |\n"
        "| Expected Result | Outcome based on documented behavior |\n"
        "| Priority | High / Medium / Low |\n"
        "| Test Data | Specific values (amounts, currencies, BICs, IBANs) |\n"
        "| Source Document | Which doc this traces to |\n\n"
        "RULES:\n"
        "- Every step and navigation path MUST trace back to the RAG documentation.\n"
        "- Do NOT fabricate screens, menu paths, or field names.\n"
        "- Generate test cases ONLY for the specific system/clearing in the context.\n"
        "- Cover: positive flow, negative flow, boundary conditions, and edge cases.\n"
        "- If the documentation lacks workflow/navigation details, state: "
        "'Insufficient documentation to generate detailed test steps for this area.'"
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
        pattern = r'\b' + re.escape(phrase) + r'\b'
        if re.search(pattern, query_lower):
            query_lower = re.sub(pattern, f"{phrase} {replacement}", query_lower)

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
        if len(key_terms) <= 3:
            min_match = MIN_KEYWORD_MATCH
        elif len(key_terms) <= 6:
            min_match = 0.5
        else:
            min_match = 0.4
        results = [r for r in results if r[3] >= min_match]
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


SOLUTION_DISCOVERY_PROMPT = (
    "You are a Temenos Payments Hub (TPH) payment architect analyzing a client requirement.\n\n"
    "Your task: Based on the user's requirement, generate 3-5 specific search queries "
    "to find ALL relevant TPH capabilities, modules, clearing systems, and configurations "
    "that could be part of the solution.\n\n"
    "Think about:\n"
    "- Which payment order types are involved (PI, DB, PP)?\n"
    "- Which clearing/settlement systems are needed?\n"
    "- What configuration or setup is required?\n"
    "- What processing flows (inward, outward, returns) apply?\n"
    "- What integration points exist?\n\n"
    "Respond with ONLY a JSON array of search queries, no other text:\n"
    '["query 1", "query 2", "query 3"]\n'
)

SOLUTION_ARCHITECT_PROMPT = (
    "You are a Senior TPH Solution Architect with deep expertise in Temenos Payments Hub "
    "and banking payment systems.\n\n"
    "You have been given a client requirement AND relevant TPH documentation gathered "
    "by your research team. Your job is to design a complete, implementable solution.\n\n"
    "APPROACH:\n"
    "1. ANALYZE — Break the requirement into functional components\n"
    "2. SEARCH RAG FIRST — For each component, check if TPH documentation covers it\n"
    "3. RAG-BASED SOLUTION — If found in docs, propose the documented approach with citations\n"
    "4. ARCHITECT'S RECOMMENDATION — If NOT found in docs, use your own TPH expertise "
    "to propose how this could be achieved in TPH. Clearly mark these as "
    "'Architect recommendation (not in current docs)'\n"
    "5. ASK — If the requirement is ambiguous, ask clarifying questions\n\n"
    "IMPORTANT: This is the ONLY mode that may go beyond RAG documentation. "
    "When you do, you MUST clearly label it.\n\n"
    "RESPONSE FORMAT:\n\n"
    "### Requirement Analysis\n"
    "Break down what the client needs into discrete components.\n\n"
    "### Proposed Solution\n"
    "For each component:\n"
    "- **Component**: What this solves\n"
    "- **TPH Module**: Module/application name\n"
    "- **Payment Type**: PI, DB, PP, etc.\n"
    "- **Clearing System**: SWIFT, SEPA, FPS, TARGET2, etc.\n"
    "- **Configuration**: Key parameters or setup\n"
    "- **Processing Flow**: Inward/Outward/Return\n"
    "- **Source**: 📄 *From documentation: [doc name]* OR 🏗️ *Architect recommendation*\n\n"
    "### End-to-End Flow\n"
    "Numbered step-by-step flow from initiation to settlement.\n\n"
    "### Technical Feasibility\n"
    "- What is natively supported (with doc references)\n"
    "- What requires configuration\n"
    "- What requires customization/development\n"
    "- What may not be feasible in TPH\n\n"
    "### Gaps & Risks\n"
    "- Documentation gaps\n"
    "- Integration risks\n"
    "- Performance considerations\n\n"
    "### Clarifying Questions\n"
    "Questions you need answered to refine the solution. Ask about:\n"
    "- Volumes, currencies, cut-off times\n"
    "- Existing infrastructure and integrations\n"
    "- Regulatory requirements\n"
    "- SLA expectations\n"
)


def solution_provider_flow(client, model, chunks, embeddings, search_texts, question):
    with st.status("🔍 Discovery Agent — analyzing requirement...", expanded=True) as status:
        st.write("Breaking down your requirement into search queries...")

        discovery_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SOLUTION_DISCOVERY_PROMPT},
                {"role": "user", "content": f"Client requirement: {question}"},
            ],
            temperature=0.1,
            max_tokens=500,
        )

        search_queries_text = discovery_response.choices[0].message.content.strip()
        try:
            if "```" in search_queries_text:
                search_queries_text = search_queries_text.split("```")[1].replace("json", "").strip()
            search_queries = json.loads(search_queries_text)
        except (json.JSONDecodeError, IndexError):
            search_queries = [question]

        st.write(f"Searching documentation with {len(search_queries)} targeted queries...")
        for i, q in enumerate(search_queries):
            st.write(f"  {i+1}. {q}")

        status.update(label="🔍 Discovery Agent — gathering documentation...", state="running")

        all_contexts = []
        all_sources = []
        seen_chunks = set()

        for sq in search_queries:
            ctx, srcs = retrieve_context(model, chunks, embeddings, search_texts, sq, top_k=5)
            if ctx:
                for chunk_text in ctx.split("\n\n---\n\n"):
                    chunk_hash = hash(chunk_text[:100])
                    if chunk_hash not in seen_chunks:
                        seen_chunks.add(chunk_hash)
                        all_contexts.append(chunk_text)
                for src in srcs:
                    if src["url"] not in [s["url"] for s in all_sources]:
                        all_sources.append(src)

        if not all_contexts:
            status.update(label="❌ No relevant documentation found", state="error")
            return None, []

        combined_context = "\n\n---\n\n".join(all_contexts[:15])

        status.update(
            label=f"✅ Discovery complete — found {len(all_contexts)} relevant sections from {len(all_sources)} documents",
            state="complete",
        )

    with st.status("🛡️ Validator Agent — verifying relevance...", expanded=False) as status:
        is_relevant, reason = validate_context(client, combined_context, question)
        if is_relevant:
            status.update(label=f"✅ Validated: {reason}", state="complete")
        else:
            status.update(label=f"❌ Rejected: {reason}", state="error")
            return None, []

    st.write("🏗️ **Solution Architect Agent** — designing solution...")

    response = st.write_stream(
        stream_groq_response(client, SOLUTION_ARCHITECT_PROMPT, combined_context, question)
    )

    return response, all_sources


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
        - 🏗️ **Solution** — Multi-agent architecture
        - 📊 **Fitment** — Assess TPH fit
        - 🧪 **Test Cases** — Generate test scenarios

        **Agents:**
        - 🛡️ **Validator** — Checks context relevance
        - 💬 **Responder** — Generates verified answer
        - 🔍 **Discovery** — Broad capability search *(Solution mode)*
        - 🏗️ **Architect** — Designs end-to-end solution *(Solution mode)*
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

        client = get_groq_client()

        if mode == "Solution Provider":
            with st.chat_message("assistant"):
                response, sources = solution_provider_flow(
                    client, model, chunks, embeddings, search_texts, question
                )
                if response is None:
                    st.markdown(NO_INFO_MSG)
                    st.session_state.messages.append({"role": "assistant", "content": NO_INFO_MSG})
                else:
                    if sources:
                        st.markdown("---")
                        st.markdown("**📄 Documentation Referenced:**")
                        for src in sources[:8]:
                            if src["url"]:
                                st.markdown(f"- [{src['title']}]({src['url']})")
                            else:
                                st.markdown(f"- {src['title']}")
                    source_text = ""
                    if sources:
                        source_text = "\n\n---\n**Sources:** " + ", ".join(s["title"] for s in sources[:8])
                    st.session_state.messages.append({"role": "assistant", "content": response + source_text})
        else:
            context, sources = retrieve_context(model, chunks, embeddings, search_texts, question)

            if context is None:
                with st.chat_message("assistant"):
                    st.markdown(NO_INFO_MSG)
                st.session_state.messages.append({"role": "assistant", "content": NO_INFO_MSG})
                return

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
