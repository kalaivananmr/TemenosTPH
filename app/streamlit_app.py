"""
Temenos Payments Hub — Agentic RAG Consultant (Streamlit + Groq)
Two-agent architecture: Validator Agent checks context relevance,
Response Agent generates answer only if context is verified.
"""

import json
import os
import re
import time
import numpy as np
import streamlit as st
from pathlib import Path

CHUNKS_FILE = Path(__file__).parent.parent / "rag" / "chunks.jsonl"
TOP_K = 12
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

PAYMENT_INTELLIGENCE = (
    "PAYMENT INTELLIGENCE (apply to EVERY response):\n"
    "You are a human payment expert. Any movement of funds from one account to another "
    "IS a payment. Even if the user's request mentions an external system (Mobilepay, UPI, "
    "wallet, fintech, third-party), you must recognize the UNDERLYING PAYMENT PATTERN:\n"
    "- Wallet loading = Credit Transfer (outward PI)\n"
    "- Collection from account = Debit Collection (DB)\n"
    "- Bank-to-bank transfer = Payments Hub (PP) processing\n"
    "- Reversal/refund = Return/Recall\n"
    "- API call after payment = Event notification / status update\n"
    "- Timeout + retry = Payment retry/resubmission logic\n\n"
    "When RAG documentation shows TPH payment patterns (even for a different system), "
    "APPLY those patterns to the user's requirement. TPH is a universal payment engine — "
    "the patterns for SWIFT, SEPA, NEFT all apply to any fund movement.\n\n"
    "NEVER reject a question about payments just because the specific system name "
    "isn't in the docs. Map it to the TPH equivalent and respond.\n\n"
    "TPH STATUS CODES — Always use these in your responses:\n"
    "- Status 100: Payment initiated/pending processing\n"
    "- Status 150: Awaiting approval/authorization\n"
    "- Status 230: Sent to clearing\n"
    "- Status 600: Payment settled\n"
    "- Status 677: Sent, waiting ACK/NACK from clearing\n"
    "- Status 687: Payment reversed\n"
    "- Status 996: Payment cancelled\n"
    "- Status 997: Payment rejected\n"
    "- Status 999: Payment completed successfully\n"
    "Never use 'Act 1', 'Act 2' or generic activity labels. "
    "Always reference TPH status codes and processing stages.\n\n"
)

SYNTHESIS_INSTRUCTION = (
    PAYMENT_INTELLIGENCE +
    "CONTEXT SYNTHESIS RULES (apply before answering):\n"
    "The retrieved RAG context may arrive as multiple fragmented chunks "
    "belonging to the same document or topic.\n"
    "Before answering:\n"
    "1. MERGE chunks that belong to the same requirement, topic, or workflow "
    "into one coherent context. Use the [title] and [section] headers to identify related chunks.\n"
    "2. RESOLVE ordering using logical workflow sequence (e.g., Configuration → Processing → Output), "
    "not the order chunks appear.\n"
    "3. If chunks overlap or repeat, use the most complete and specific version.\n"
    "4. If chunks contradict, prioritize the chunk with higher match % or more specific section heading.\n"
    "5. Answer using the merged context as a SINGLE coherent source — do NOT answer chunk-by-chunk "
    "or list each chunk separately.\n"
    "6. When referencing screens, navigation, or steps, reconstruct the full workflow path "
    "from the merged context.\n\n"
)

MODE_PROMPTS = {
    "Payment Consultant": (
        SYNTHESIS_INSTRUCTION +
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
        SYNTHESIS_INSTRUCTION +
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
        SYNTHESIS_INSTRUCTION +
        "You are a QA Engineer specializing in Temenos Payments Hub (TPH) testing.\n\n"
        "TASK: From the RAG documentation context, extract the navigation paths, "
        "workflow steps, screens, and field-level details relevant to the user's requirement. "
        "Generate structured test cases based ONLY on this extracted information.\n\n"
        "OUTPUT FORMAT — For each test case use this structure:\n\n"
        "#### TC-XXX: [Test Case Title]\n"
        "**Priority:** High / Medium / Low\n\n"
        "**Preconditions:**\n"
        "- Precondition 1\n"
        "- Precondition 2\n\n"
        "**Navigation:** Menu path / screen from docs\n\n"
        "**Steps:**\n"
        "1. First step\n"
        "2. Second step\n"
        "3. Third step\n\n"
        "**Expected Result:**\n"
        "- Expected outcome 1\n"
        "- Expected outcome 2\n\n"
        "**Test Data:** Amount, currency, BIC, IBAN values\n\n"
        "**Source Document:** Document name from context\n\n"
        "---\n\n"
        "FORMATTING RULES:\n"
        "- NEVER use <br> or HTML tags. Use markdown only.\n"
        "- Each step MUST be on its own numbered line (1. 2. 3.).\n"
        "- Do NOT put multiple steps in a single line.\n"
        "- Use bullet points (- ) for lists, not inline text.\n\n"
        "TPH STATUS CODE RULES:\n"
        "- ALWAYS use TPH payment status codes in expected results, NOT generic labels.\n"
        "- Use actual status codes from the documentation:\n"
        "  - Status 100: Payment initiated/pending\n"
        "  - Status 150: Awaiting approval\n"
        "  - Status 230: Sent to clearing\n"
        "  - Status 600: Payment settled\n"
        "  - Status 677: Sent, waiting ACK/NACK\n"
        "  - Status 687: Payment reversed\n"
        "  - Status 996: Payment cancelled\n"
        "  - Status 997: Payment rejected\n"
        "  - Status 999: Payment completed successfully\n"
        "- NEVER write 'Act 1', 'Act 2', 'Activity 1' etc. as step labels.\n"
        "  Instead describe the actual processing step with its status code.\n"
        "  Wrong: 'Act 1: Payment created'\n"
        "  Correct: 'Payment initiated → status moves to 100 (Pending Processing)'\n"
        "- In Expected Result, always state which status code the payment should reach.\n\n"
        "CONTENT RULES:\n"
        "- Every step and navigation path MUST trace back to the RAG documentation.\n"
        "- Do NOT fabricate screens, menu paths, or field names.\n"
        "- Generate test cases ONLY for the specific system/clearing in the context.\n"
        "- Cover: positive flow, negative flow, boundary conditions, and edge cases.\n"
        "- If the documentation lacks workflow/navigation details, state: "
        "'Insufficient documentation to generate detailed test steps for this area.'"
    ),
}

VALIDATOR_PROMPT = (
    "You are a Payment Domain Expert validating retrieved documentation for a "
    "Temenos Payments Hub (TPH) knowledge system.\n\n"
    "CORE PRINCIPLE: Any movement of funds from one account to another IS a payment. "
    "You must think like a human payment architect — if the user's request involves "
    "any form of fund transfer, wallet loading, account debiting/crediting, collection, "
    "or settlement, it FITS into TPH's core banking payment domain.\n\n"
    "YOUR JOB: Assess if the retrieved documentation provides USEFUL context to help "
    "answer the user's question, even if it's not an exact match.\n\n"
    "VALIDATION LOGIC:\n"
    "1. If user asks about a SPECIFIC country clearing (e.g. 'Indian RTGS') and context "
    "has a DIFFERENT country's clearing → relevant: false (wrong country)\n"
    "2. If user asks about ANY payment concept (fund transfer, wallet, collection, "
    "debit, credit, settlement, API integration, reversal) and context covers "
    "TPH payment processing, initiation, or similar flows → relevant: true "
    "(the TPH patterns APPLY even if the external system name differs)\n"
    "3. If user provides a requirement document about an external system (Mobilepay, "
    "UPI, wallet, fintech) that involves fund movement → relevant: true "
    "(TPH handles all payment types — the patterns are transferable)\n"
    "4. If user asks about SWIFT field codes (71G, 71F, 32A, 50K, 59, MT103, MT202, "
    "pacs.008, pain.001, camt.053) or charge types (OUR, BEN, SHA) or "
    "any banking/payment terminology → relevant: true if context mentions "
    "any of these codes, charge types, or related payment processing\n"
    "5. If context has NO connection to payments or fund movement at all → relevant: false\n\n"
    "THINK LIKE A HUMAN: A payment consultant would NEVER reject a question about "
    "'loading a wallet' just because 'wallet' isn't in TPH docs. They'd recognize it as "
    "a credit transfer/fund transfer and use TPH's payment initiation patterns.\n\n"
    "Respond with ONLY a JSON object (no markdown, no extra text):\n"
    '{"relevant": true/false, "reason": "one sentence explanation", '
    '"payment_concept": "the core payment concept this maps to in TPH"}\n\n'
    "Examples:\n"
    '- User asks "Indian RTGS", context has Sri Lanka RTGS → '
    '{"relevant": false, "reason": "Context has Sri Lanka RTGS, not India", "payment_concept": "RTGS clearing"}\n'
    '- User asks about "Mobilepay wallet loading", context has payment initiation → '
    '{"relevant": true, "reason": "Wallet loading is a fund transfer — maps to TPH payment initiation", '
    '"payment_concept": "Payment Initiation (PI) outward credit transfer"}\n'
    '- User asks about "UPI collection", context has debit collection → '
    '{"relevant": true, "reason": "UPI collection maps to debit collection pattern in TPH", '
    '"payment_concept": "Debit Collection (DB)"}\n'
)

ORCHESTRATOR_PROMPT = (
    "You are the Query Orchestrator for a Temenos Payments Hub (TPH) knowledge system.\n\n"
    "CORE PRINCIPLE: Payment = movement of funds from one account to another. "
    "ANY request involving fund transfer, wallet loading, collection, settlement, "
    "debit/credit of accounts, API-based transactions, or financial messaging "
    "FITS into TPH's domain. Think like a human payment consultant — map every "
    "request to its equivalent TPH payment pattern.\n\n"
    "PAYMENT PATTERN MAPPING:\n"
    "- Wallet loading / top-up → Payment Initiation (PI) outward credit transfer\n"
    "- Collection / debit mandate → Debit Collection (DB)\n"
    "- Bank transfer → Credit Transfer via Payments Hub (PP)\n"
    "- Reversal / refund → Return/Recall processing\n"
    "- API notification → Event-based payment status update\n"
    "- Settlement → Clearing and settlement processing\n"
    "- QR payment / scan-and-pay → Payment Initiation with merchant reference\n"
    "- Bulk upload → Bulk payment processing\n"
    "- Standing instruction → Standing Order\n"
    "- SWIFT fields (71G, 71F, 32A, 50K, 59, etc.) → SWIFT message payment processing\n"
    "- Charge types (OUR, BEN, SHA) → Payment charges and fees processing\n"
    "- MT103, MT202, MT910 → SWIFT message types in PP\n"
    "- pacs.008, pain.001, camt.053 → ISO 20022 message processing\n"
    "- Cheque / teller → Cheque collection and clearing\n"
    "- Nostro / Vostro → Correspondent banking accounts\n\n"
    "DOCUMENT DETECTION:\n"
    "If the user's input contains a REQUIREMENT DOCUMENT, BRD, specification, or detailed "
    "interface description (signs: numbered sections, step-by-step flows, in-scope/out-of-scope, "
    "API specifications, integration details, long structured text >300 chars), then:\n"
    "- Set has_document: true\n"
    "- Extract the TPH payment concepts from the document\n"
    "- Generate search queries for those TPH CONCEPTS, not external system names\n"
    "- Confidence should be HIGH (85+)\n\n"
    "STEPS:\n"
    "1. UNDERSTAND the user's intent\n"
    "2. MAP to TPH payment pattern (see mapping above)\n"
    "3. CHECK if user provided a document (has_document)\n"
    "4. REWRITE using Temenos terminology:\n"
    "   - Modules: PI (Payment Initiation), DB (Debit Collection), PP (Payments Hub), POR (Payment Order)\n"
    "   - Clearings: SWIFT, SEPA, TARGET2, CHAPS, FPS, BACS, NEFT, RTGS, FedNow, CEFTS, TIPS, SIC\n"
    "   - Processes: inward, outward, credit transfer, direct debit, cancellation, return, recall\n"
    "5. DETECT mode: consultant / solution / fitment / testcase\n"
    "6. GENERATE 2-4 focused search queries for TPH CONCEPTS\n"
    "7. ASSESS confidence (always 85+ if request involves any fund movement)\n\n"
    "Respond with ONLY a JSON object (no markdown, no extra text):\n"
    "{\n"
    '  "original": "brief summary",\n'
    '  "rewritten": "optimized TPH query",\n'
    '  "intent": "consultant|solution|fitment|testcase",\n'
    '  "has_document": true/false,\n'
    '  "payment_pattern": "which TPH pattern this maps to",\n'
    '  "search_queries": ["tph concept query1", "tph concept query2"],\n'
    '  "confidence": 85,\n'
    '  "reasoning": "one sentence explanation"\n'
    "}\n\n"
    "EXAMPLES:\n\n"
    '- User pastes Mobilepay integration BRD + asks for test cases\n'
    '  → has_document: true\n'
    '  → payment_pattern: "PI outward credit transfer + API notification"\n'
    '  → rewritten: "TPH payment initiation, fund transfer, API notification, '
    'transaction reversal, timeout retry handling"\n'
    '  → search_queries: ["payment initiation branch user fund transfer", '
    '"API notification response handling TPH", "transaction reversal timeout retry"]\n'
    '  → intent: "testcase", confidence: 92\n\n'
    '- "is it possible to capture collection requests cleared via domestic clearings DB"\n'
    '  → has_document: false\n'
    '  → payment_pattern: "Debit Collection (DB) domestic clearing"\n'
    '  → rewritten: "Debit Collection (DB) capturing collection requests for domestic clearings"\n'
    '  → intent: "consultant", confidence: 90\n\n'
    '- User pastes API spec + asks "how to implement this in TPH"\n'
    '  → has_document: true\n'
    '  → rewritten: "REST API integration with TPH payment processing"\n'
    '  → search_queries: ["API integration TPH REST", "payment processing configuration", '
    '"inward outward payment flow"]\n'
    '  → intent: "solution", confidence: 85\n'
)

INTENT_TO_MODE = {
    "consultant": "Payment Consultant",
    "solution": "Solution Provider",
    "fitment": "Core Fitment Assessor",
    "testcase": "Test Case Generator",
}

NO_INFO_MSG = (
    "**No information available.**\n\n"
    "The Temenos Payments Hub documentation in our knowledge base does not contain "
    "specific information to answer this question. This could mean:\n"
    "- This topic/clearing system was not covered in the crawled documentation\n"
    "- The specific country or feature may not be supported by TPH\n"
    "- Try rephrasing with the exact Temenos terminology (e.g., 'NEFT' instead of 'Indian RTGS')"
)


PAYMENT_TERM_MAP = {
    # SWIFT fields
    "71g": "SWIFT field 71G receiver's charges OUR BEN SHA payment charges PP",
    "71f": "SWIFT field 71F sender's charges payment charges fees",
    "32a": "SWIFT field 32A value date currency amount",
    "33b": "SWIFT field 33B currency instructed amount",
    "50k": "SWIFT field 50K ordering customer payer details",
    "50a": "SWIFT field 50A ordering institution",
    "52a": "SWIFT field 52A ordering institution BIC",
    "53a": "SWIFT field 53A sender's correspondent",
    "54a": "SWIFT field 54A receiver's correspondent",
    "56a": "SWIFT field 56A intermediary institution",
    "57a": "SWIFT field 57A account with institution beneficiary bank",
    "59": "SWIFT field 59 beneficiary customer",
    "59a": "SWIFT field 59A beneficiary customer",
    "70": "SWIFT field 70 remittance information",
    "72": "SWIFT field 72 sender to receiver information",
    "77b": "SWIFT field 77B regulatory reporting",
    "23e": "SWIFT field 23E instruction code",
    # SWIFT message types
    "mt103": "SWIFT MT103 single customer credit transfer outward payment",
    "mt202": "SWIFT MT202 financial institution transfer cover payment",
    "mt202cov": "SWIFT MT202COV cover payment",
    "mt910": "SWIFT MT910 confirmation of credit",
    "mt940": "SWIFT MT940 customer statement",
    "mt950": "SWIFT MT950 statement message",
    "mt199": "SWIFT MT199 free format message",
    "mt192": "SWIFT MT192 cancellation request",
    "mt196": "SWIFT MT196 cancellation answer",
    "mt900": "SWIFT MT900 confirmation of debit",
    # ISO 20022
    "pacs.008": "ISO 20022 pacs.008 FI to FI customer credit transfer",
    "pacs.009": "ISO 20022 pacs.009 FI to FI financial institution credit transfer",
    "pacs.002": "ISO 20022 pacs.002 payment status report",
    "pacs.004": "ISO 20022 pacs.004 payment return",
    "pacs.028": "ISO 20022 pacs.028 FI to FI payment status request",
    "pain.001": "ISO 20022 pain.001 customer credit transfer initiation",
    "pain.002": "ISO 20022 pain.002 customer payment status report",
    "pain.008": "ISO 20022 pain.008 customer direct debit initiation",
    "camt.053": "ISO 20022 camt.053 bank to customer statement",
    "camt.054": "ISO 20022 camt.054 bank to customer debit credit notification",
    "camt.056": "ISO 20022 camt.056 FI to FI payment cancellation request",
    "camt.029": "ISO 20022 camt.029 resolution of investigation",
    # Charge types
    "our": "charge type OUR all charges borne by sender",
    "ben": "charge type BEN all charges borne by beneficiary",
    "sha": "charge type SHA shared charges between sender and receiver",
    # TPH codes
    "pp.insuffoutb": "PP insufficient outbound charges OUR 71G",
    "insuffoutb": "insufficient outbound charges OUR 71G payment",
    # TPH Payment Status Codes
    "status 15": "TPH payment status code 15 sent to auto enrichment engine",
    "status 100": "TPH payment status code 100 initiated pending processing",
    "status 130": "TPH payment status code 130 payment pending validation",
    "status 150": "TPH payment status code 150 payment awaiting approval",
    "status 215": "TPH payment status code 215 payment pending clearing",
    "status 230": "TPH payment status code 230 payment sent to clearing",
    "status 235": "TPH payment status code 235 payment pending settlement",
    "status 404": "TPH payment status code 404 service not available",
    "status 600": "TPH payment status code 600 payment settled",
    "status 602": "TPH payment status code 602 payment settlement pending",
    "status 642": "TPH payment status code 642 payment exception",
    "status 645": "TPH payment status code 645 payment repair required",
    "status 677": "TPH payment status code 677 payment sent waiting ACK NACK",
    "status 687": "TPH payment status code 687 payment reversed",
    "status 996": "TPH payment status code 996 payment cancelled",
    "status 997": "TPH payment status code 997 payment rejected",
    "status 998": "TPH payment status code 998 announcement message",
    "status 999": "TPH payment status code 999 payment completed successfully",
    # Payment concepts
    "stp": "straight through processing STP auto payment",
    "ncc": "non STP repair payment manual intervention",
    "ofs": "open financial services OFS T24 Transact message",
    "bic": "bank identifier code SWIFT BIC payment routing",
    "iban": "international bank account number IBAN",
    "sort code": "UK sort code bank branch identifier",
    "clearing": "clearing system settlement payment processing",
    "nostro": "nostro account correspondent banking outward",
    "vostro": "vostro account correspondent banking inward",
    "gpi": "SWIFT gpi global payments innovation tracker",
    "uetr": "unique end-to-end transaction reference SWIFT gpi",
    "sanctions": "sanctions screening compliance AML payment",
    "aml": "anti money laundering compliance screening",
    "kyc": "know your customer compliance",
    "fx": "foreign exchange rate currency conversion",
    "forex": "foreign exchange rate currency conversion",
    "netting": "payment netting bilateral multilateral",
    "cutoff": "cut-off time payment processing window",
    "cut-off": "cut-off time payment processing window",
    "value date": "value date settlement date payment processing",
    "exposure": "exposure date future dated payment",
    "mandate": "direct debit mandate authorization",
    "dd": "direct debit collection mandate",
    "standing order": "standing order recurring payment instruction",
    "bulk": "bulk payment batch processing upload",
    "teller": "teller branch initiated payment transaction",
    "cheque": "cheque check collection clearing instrument",
    "check": "cheque check collection clearing instrument",
}


def map_to_payment_terms(query):
    """Agent 0: Payment Term Mapper — runs BEFORE everything else.
    Maps any raw query to banking/payment terms. No LLM call needed."""

    q_lower = query.lower()
    mapped_terms = []
    original_terms = []

    for term, expansion in PAYMENT_TERM_MAP.items():
        pattern = r'\b' + re.escape(term) + r'\b'
        if re.search(pattern, q_lower):
            mapped_terms.append(expansion)
            original_terms.append(term)

    enriched_query = query
    if mapped_terms:
        enriched_query = query + "\n\n[Payment Terms Identified: " + "; ".join(mapped_terms) + "]"

    search_enrichments = []
    for expansion in mapped_terms:
        words = expansion.split()
        search_enrichments.extend(words)
    search_enrichments = list(dict.fromkeys(search_enrichments))

    return {
        "enriched_query": enriched_query,
        "matched_terms": original_terms,
        "payment_context": " ".join(mapped_terms) if mapped_terms else "",
        "search_boost_terms": search_enrichments,
        "is_payment_query": len(mapped_terms) > 0 or any(
            w in q_lower for w in [
                "payment", "transfer", "debit", "credit", "charge", "fee",
                "clearing", "settlement", "transaction", "fund", "remittance",
                "beneficiary", "payer", "account", "bank", "swift", "sepa",
                "initiation", "collection", "reversal", "return", "cancel",
                "outward", "inward", "nostro", "vostro", "correspondent",
            ]
        ),
    }


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
            c.get("topic", ""),
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


def get_llm_client():
    api_key = ""
    provider = "gemini"

    for key_name in ["GEMINI_API_KEY", "GOOGLE_API_KEY"]:
        api_key = os.environ.get(key_name, "")
        if not api_key:
            try:
                api_key = st.secrets[key_name]
            except Exception:
                pass
        if api_key:
            provider = "gemini"
            break

    if not api_key:
        for key_name in ["GROQ_API_KEY"]:
            api_key = os.environ.get(key_name, "")
            if not api_key:
                try:
                    api_key = st.secrets[key_name]
                except Exception:
                    pass
            if api_key:
                provider = "groq"
                break

    if not api_key:
        st.error("No API key found. Add GEMINI_API_KEY (free, recommended) or GROQ_API_KEY in Settings > Secrets.")
        st.stop()

    return api_key, provider


GEMINI_MODELS = [
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-2.0-flash-lite",
]


def _try_gemini(api_key, system_prompt, user_prompt, temperature, max_tokens, stream):
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    config = genai.types.GenerationConfig(temperature=temperature, max_output_tokens=max_tokens)

    last_error = None
    for model_name in GEMINI_MODELS:
        try:
            model = genai.GenerativeModel(model_name, system_instruction=system_prompt)
            if stream:
                response = model.generate_content(user_prompt, generation_config=config, stream=True)
                return response, model_name
            else:
                response = model.generate_content(user_prompt, generation_config=config)
                return response, model_name
        except Exception as e:
            last_error = e
            err_str = str(e)
            if "ResourceExhausted" in type(e).__name__ or "429" in err_str or "quota" in err_str.lower():
                continue
            else:
                raise
    raise last_error


def _try_groq(api_key, system_prompt, user_prompt, temperature, max_tokens, stream):
    from groq import Groq
    client = Groq(api_key=api_key)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt[:3500]},
    ]
    if stream:
        return client.chat.completions.create(
            model="llama-3.1-8b-instant", messages=messages,
            temperature=temperature, max_tokens=max_tokens, stream=True,
        )
    else:
        return client.chat.completions.create(
            model="llama-3.1-8b-instant", messages=messages,
            temperature=temperature, max_tokens=max_tokens,
        )


def call_llm(api_key, provider, system_prompt, user_prompt, temperature=0.1, max_tokens=2048, stream=False):
    gemini_key = ""
    groq_key = ""
    for key_name in ["GEMINI_API_KEY", "GOOGLE_API_KEY"]:
        k = os.environ.get(key_name, "")
        if not k:
            try:
                k = st.secrets[key_name]
            except Exception:
                pass
        if k:
            gemini_key = k
            break
    for key_name in ["GROQ_API_KEY"]:
        k = os.environ.get(key_name, "")
        if not k:
            try:
                k = st.secrets[key_name]
            except Exception:
                pass
        if k:
            groq_key = k
            break

    errors = []

    if gemini_key:
        try:
            if stream:
                response, used_model = _try_gemini(gemini_key, system_prompt, user_prompt, temperature, max_tokens, True)
                for chunk in response:
                    if chunk.text:
                        yield chunk.text
                return
            else:
                response, used_model = _try_gemini(gemini_key, system_prompt, user_prompt, temperature, max_tokens, False)
                yield response.text
                return
        except Exception as e:
            errors.append(f"Gemini: {e}")

    if groq_key:
        try:
            if stream:
                resp = _try_groq(groq_key, system_prompt, user_prompt, temperature, max_tokens, True)
                for chunk in resp:
                    text = chunk.choices[0].delta.content
                    if text:
                        yield text
                return
            else:
                resp = _try_groq(groq_key, system_prompt, user_prompt, temperature, max_tokens, False)
                yield resp.choices[0].message.content
                return
        except Exception as e:
            errors.append(f"Groq: {e}")

    hf_key = ""
    for key_name in ["HF_API_KEY", "HUGGINGFACE_API_KEY", "HF_TOKEN"]:
        hf_key = os.environ.get(key_name, "")
        if not hf_key:
            try:
                hf_key = st.secrets[key_name]
            except Exception:
                pass
        if hf_key:
            break

    if hf_key:
        try:
            from huggingface_hub import InferenceClient
            hf_client = InferenceClient(api_key=hf_key)
            combined_prompt = f"System: {system_prompt}\n\nUser: {user_prompt[:3000]}"
            if stream:
                resp = hf_client.text_generation(
                    combined_prompt,
                    model="mistralai/Mistral-7B-Instruct-v0.3",
                    max_new_tokens=max_tokens,
                    temperature=max(temperature, 0.01),
                    stream=True,
                )
                for token in resp:
                    yield token
                return
            else:
                resp = hf_client.text_generation(
                    combined_prompt,
                    model="mistralai/Mistral-7B-Instruct-v0.3",
                    max_new_tokens=max_tokens,
                    temperature=max(temperature, 0.01),
                )
                yield resp
                return
        except Exception as e:
            errors.append(f"HuggingFace: {e}")

    error_detail = " | ".join(errors) if errors else "No API keys configured"
    yield f"**All LLM providers exhausted.** Wait a few minutes and retry.\n\nDetails: {error_detail}"


def call_llm_once(api_key, provider, system_prompt, user_prompt, temperature=0.0, max_tokens=500):
    return "".join(call_llm(api_key, provider, system_prompt, user_prompt, temperature, max_tokens, stream=False))


def validate_context(api_key, provider, context, question):
    result_text = call_llm_once(
        api_key, provider, VALIDATOR_PROMPT,
        f"User question: {question}\n\nRetrieved documentation context:\n{context[:3000]}",
    )

    try:
        clean = result_text.strip()
        if "```" in clean:
            clean = clean.split("```")[1].replace("json", "").strip()
        result = json.loads(clean)
        return result.get("relevant", False), result.get("reason", "")
    except (json.JSONDecodeError, IndexError):
        if "true" in result_text.lower():
            return True, result_text
        return False, result_text


def stream_response(api_key, provider, system_prompt, context, question):
    user_prompt = f"Documentation context:\n\n{context}\n\n---\nQuestion: {question}"
    yield from call_llm(api_key, provider, system_prompt, user_prompt, temperature=0.1, max_tokens=2048, stream=True)


def _detect_intent_from_text(question):
    q = question.lower()
    if any(w in q for w in ["test case", "test scenario", "qa", "validate", "testing"]):
        return "testcase"
    if any(w in q for w in ["solution", "how to achieve", "implement", "design", "workflow", "we need", "we want"]):
        return "solution"
    if any(w in q for w in ["fitment", "assess", "evaluate", "gap", "fit", "capability"]):
        return "fitment"
    return "consultant"


def _build_search_queries_from_text(question):
    q = question.lower()
    queries = []

    banking_codes = re.findall(r'\b(?:MT\d{3}|[0-9]{2}[A-Za-z]|field\s+\d+[a-z]?|tag\s+\d+[a-z]?|PP\.[A-Z.]+|pacs\.\d+|pain\.\d+|camt\.\d+)\b', question, re.IGNORECASE)
    if banking_codes:
        for code in banking_codes[:2]:
            queries.append(f"{code} SWIFT payment charges field")

    payment_terms = []
    if any(w in q for w in ["international", "cross-border", "forex", "exchange"]):
        payment_terms.append("international payment cross-border exchange rate")
    if any(w in q for w in ["transfer", "fund", "credit", "debit", "payment"]):
        payment_terms.append("payment initiation credit transfer processing")
    if any(w in q for w in ["collection", "direct debit", "mandate"]):
        payment_terms.append("debit collection DB processing")
    if any(w in q for w in ["api", "integration", "interface", "notification"]):
        payment_terms.append("API integration interface payment processing")
    if any(w in q for w in ["exchange rate", "rate", "forex", "xe", "currency"]):
        payment_terms.append("exchange rate currency conversion payment")
    if any(w in q for w in ["reversal", "refund", "return", "cancel"]):
        payment_terms.append("payment reversal return recall")
    if any(w in q for w in ["clearing", "settlement", "swift", "sepa"]):
        payment_terms.append("clearing settlement processing")
    if any(w in q for w in ["wallet", "load", "top-up", "mobile"]):
        payment_terms.append("payment initiation fund transfer outward")
    if any(w in q for w in ["workflow", "flow", "process", "step"]):
        payment_terms.append("payment processing workflow configuration")
    if any(w in q for w in ["charge", "fee", "commission", "71g", "71f", "our", "ben", "sha"]):
        payment_terms.append("charges fees OUR BEN SHA receiver sender 71G 71F")
    if any(w in q for w in ["cheque", "check", "collection", "teller"]):
        payment_terms.append("cheque collection teller processing")
    if any(w in q for w in ["nostro", "vostro", "suspense", "account"]):
        payment_terms.append("nostro vostro suspense account clearing")

    if payment_terms:
        queries.extend(payment_terms[:4])

    queries.append(question[:150])

    return queries[:5]


def run_orchestrator(api_key, provider, question):
    # === AGENT 0: Payment Term Mapper (ALWAYS runs first, no LLM) ===
    ptm = map_to_payment_terms(question)
    enriched = ptm["enriched_query"]

    # === AGENT 1: LLM Orchestrator (uses enriched query) ===
    result_text = ""
    try:
        result_text = call_llm_once(
            api_key, provider, ORCHESTRATOR_PROMPT, enriched[:5000],
        )
    except Exception:
        result_text = ""

    # Build search queries from payment mapper + fallback
    ptm_queries = []
    if ptm["payment_context"]:
        ptm_queries.append(ptm["payment_context"][:200])
    fallback_queries = _build_search_queries_from_text(question)

    if result_text:
        try:
            clean = result_text.strip()
            if "```" in clean:
                clean = clean.split("```")[1].replace("json", "").strip()
            json_match = re.search(r'\{[^{}]*\}', clean, re.DOTALL)
            if json_match:
                clean = json_match.group(0)
            result = json.loads(clean)
            llm_queries = result.get("search_queries", [])
            combined_queries = list(dict.fromkeys(ptm_queries + llm_queries + fallback_queries))[:5]
            confidence = max(result.get("confidence", 85), 85)
            if ptm["is_payment_query"]:
                confidence = max(confidence, 90)
            return {
                "original": result.get("original", question[:200]),
                "rewritten": result.get("rewritten", question[:200]),
                "intent": result.get("intent", _detect_intent_from_text(question)),
                "has_document": result.get("has_document", len(question) > 500),
                "search_queries": combined_queries,
                "confidence": confidence,
                "reasoning": result.get("reasoning", "Payment domain query"),
                "payment_terms": ptm["matched_terms"],
            }
        except (json.JSONDecodeError, IndexError, ValueError):
            pass

    has_doc = len(question) > 500
    intent = _detect_intent_from_text(question)
    combined_queries = list(dict.fromkeys(ptm_queries + fallback_queries))[:5]
    confidence = 90 if ptm["is_payment_query"] else 85

    return {
        "original": question[:200],
        "rewritten": enriched[:300] if ptm["matched_terms"] else question[:200],
        "intent": intent,
        "has_document": has_doc,
        "search_queries": combined_queries,
        "confidence": confidence,
        "reasoning": f"Payment terms identified: {', '.join(ptm['matched_terms'])}" if ptm["matched_terms"] else "Payment domain query — intelligent routing",
        "payment_terms": ptm["matched_terms"],
    }


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
    SYNTHESIS_INSTRUCTION +
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


def solution_provider_flow(api_key, provider, model, chunks, embeddings, search_texts, question):
    with st.status("🔍 Discovery Agent — analyzing requirement...", expanded=True) as status:
        st.write("Breaking down your requirement into search queries...")

        search_queries_text = call_llm_once(
            api_key, provider, SOLUTION_DISCOVERY_PROMPT,
            f"Client requirement: {question}",
            temperature=0.1,
        )
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
        is_relevant, reason = validate_context(api_key, provider, combined_context, question)
        if is_relevant:
            status.update(label=f"✅ Validated: {reason}", state="complete")
        else:
            status.update(label=f"❌ Rejected: {reason}", state="error")
            return None, []

    st.write("🏗️ **Solution Architect Agent** — designing solution...")

    response = st.write_stream(
        stream_response(api_key, provider, SOLUTION_ARCHITECT_PROMPT, combined_context, question)
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
        mode_override = st.radio(
            "Select mode (or let AI decide):",
            ["Auto-detect"] + list(MODE_PROMPTS.keys()),
            index=0,
        )
        st.markdown("---")
        st.markdown("""
        **Modes:**
        - 🤖 **Auto-detect** — AI picks the best mode
        - 🔍 **Consultant** — Answer TPH queries
        - 🏗️ **Solution** — Multi-agent architecture
        - 📊 **Fitment** — Assess TPH fit
        - 🧪 **Test Cases** — Generate test scenarios

        **Agent Pipeline:**
        0. 🏦 **Payment Mapper** — Maps terms to banking concepts (no LLM)
        1. 🧠 **Orchestrator** — Rewrites query in TPH context, picks mode
        2. 🛡️ **Validator** — Checks context relevance
        3. 💬 **Responder** — Generates verified answer
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

        api_key, provider = get_llm_client()

        with st.chat_message("assistant"):

            # === ORCHESTRATOR AGENT (always runs first) ===
            with st.status("🧠 Orchestrator Agent — analyzing query...", expanded=True) as orch_status:
                orch = run_orchestrator(api_key, provider, question)
                rewritten = orch["rewritten"]
                confidence = orch["confidence"]
                detected_intent = orch["intent"]
                search_queries = orch["search_queries"]
                reasoning = orch["reasoning"]

                has_document = orch["has_document"]

                if mode_override == "Auto-detect":
                    mode = INTENT_TO_MODE.get(detected_intent, "Payment Consultant")
                else:
                    mode = mode_override

                payment_terms_found = orch.get("payment_terms", [])
                if payment_terms_found:
                    st.write(f"**🏦 Payment terms identified:** `{'`, `'.join(payment_terms_found)}`")
                st.write(f"**Rewritten query:** {rewritten}")
                doc_label = " | 📄 Document provided" if has_document else ""
                st.write(f"**Mode:** {mode} | **Confidence:** {confidence}%{doc_label}")
                if reasoning:
                    st.write(f"**Reasoning:** {reasoning}")

                if confidence < 80:
                    orch_status.update(
                        label=f"⚠️ Low confidence ({confidence}%) — may not find relevant docs",
                        state="error",
                    )
                    low_conf_msg = (
                        f"**Low confidence ({confidence}%)** — the query may not match "
                        f"available TPH documentation.\n\n"
                        f"🧠 **Orchestrator:** {reasoning}\n\n"
                        f"**Rewritten as:** {rewritten}\n\n"
                        f"Try rephrasing with specific Temenos terminology "
                        f"(module names, clearing systems, payment types)."
                    )
                    st.markdown(low_conf_msg)
                    st.session_state.messages.append({"role": "assistant", "content": low_conf_msg})
                    st.stop()

                orch_status.update(
                    label=f"🧠 Orchestrator: {mode} mode | {confidence}% confidence",
                    state="complete",
                )

            # === ROUTE TO MODE ===
            if mode == "Solution Provider":
                response, sources = solution_provider_flow(
                    api_key, provider, model, chunks, embeddings, search_texts, rewritten
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
                # Retrieve RAG context using orchestrator's search queries
                all_contexts = []
                all_sources = []
                seen = set()
                for sq in search_queries:
                    ctx, srcs = retrieve_context(model, chunks, embeddings, search_texts, sq, top_k=6)
                    if ctx:
                        for chunk_text in ctx.split("\n\n---\n\n"):
                            h = hash(chunk_text[:100])
                            if h not in seen:
                                seen.add(h)
                                all_contexts.append(chunk_text)
                        for src in srcs:
                            if src["url"] not in [s["url"] for s in all_sources]:
                                all_sources.append(src)

                rag_context = "\n\n---\n\n".join(all_contexts[:TOP_K]) if all_contexts else ""
                sources = all_sources

                if has_document:
                    user_doc = question[:6000]
                    if rag_context:
                        context = (
                            "=== USER PROVIDED DOCUMENT (PRIMARY CONTEXT) ===\n\n"
                            f"{user_doc}\n\n"
                            "=== TPH DOCUMENTATION (SUPPLEMENTARY REFERENCE) ===\n\n"
                            f"{rag_context}"
                        )
                    else:
                        context = (
                            "=== USER PROVIDED DOCUMENT (PRIMARY CONTEXT) ===\n\n"
                            f"{user_doc}\n\n"
                            "=== TPH DOCUMENTATION ===\n\n"
                            "No matching TPH documentation found in RAG. "
                            "Use your TPH domain knowledge to analyze the document above."
                        )

                    doc_mode_prompt = MODE_PROMPTS[mode]
                    if isinstance(doc_mode_prompt, str) and doc_mode_prompt != "SOLUTION_PROVIDER_MULTI_STEP":
                        doc_mode_prompt = (
                            "IMPORTANT: The user has provided a REQUIREMENT DOCUMENT as input. "
                            "This document describes an integration or feature for an EXTERNAL system "
                            "(e.g., Mobilepay, wallet, third-party API, etc.).\n\n"
                            "Your task:\n"
                            "1. Treat the user's document as PRIMARY CONTEXT — it defines what needs to be done\n"
                            "2. Use the TPH documentation (if available) as SUPPLEMENTARY REFERENCE for how "
                            "TPH handles similar patterns (payment initiation, fund transfer, API calls, etc.)\n"
                            "3. Map the document's requirements to TPH concepts and workflows\n"
                            "4. Generate your response based on the user's document, enriched with TPH knowledge\n"
                            "5. Do NOT reject the query because the external system name isn't in TPH docs\n\n"
                            + doc_mode_prompt
                        )

                    with st.status("📄 Document mode — using your document as primary context", expanded=False) as status:
                        status.update(label="📄 Document mode — your document + TPH knowledge", state="complete")

                    response = st.write_stream(
                        stream_response(api_key, provider, doc_mode_prompt, context, rewritten)
                    )
                    if sources:
                        st.markdown("---")
                        st.markdown("**📄 TPH Documentation Referenced:**")
                        for src in sources[:5]:
                            if src["url"]:
                                st.markdown(f"- [{src['title']}]({src['url']}) ({src['score']:.0%})")
                            else:
                                st.markdown(f"- {src['title']} ({src['score']:.0%})")

                    source_text = ""
                    if sources:
                        source_text = "\n\n---\n**Sources:** " + ", ".join(s["title"] for s in sources[:5])
                    st.session_state.messages.append({"role": "assistant", "content": response + source_text})

                else:
                    # Normal flow (no document) — validate then respond
                    if not all_contexts:
                        st.markdown(NO_INFO_MSG)
                        st.session_state.messages.append({"role": "assistant", "content": NO_INFO_MSG})
                        st.stop()

                    context = rag_context

                    with st.status("🛡️ Validator Agent checking relevance...", expanded=False) as status:
                        is_relevant, reason = validate_context(api_key, provider, context, rewritten)
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
                            stream_response(api_key, provider, MODE_PROMPTS[mode], context, rewritten)
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
