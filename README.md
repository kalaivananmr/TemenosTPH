# Temenos Payments Hub — Agentic RAG Consultant

AI-powered consultant for Temenos Payments Hub (TPH) documentation. Provides 4 operational modes powered by RAG (Retrieval-Augmented Generation) over 425+ scraped documentation pages.

## Modes

| Mode | Description |
|------|-------------|
| **Payment Consultant** | Answer any TPH query with citations |
| **Solution Provider** | Map business requirements to TPH modules |
| **Core Fitment Assessor** | Evaluate TPH fit against requirements |
| **Test Case Generator** | Generate structured test cases for payment flows |

## Architecture

```
User Query → Embedding Search → ChromaDB (7000+ chunks) → LLM → Response with Sources
```

## Quick Start — Cloud (Streamlit + Groq)

### 1. Get a free Groq API key
- Sign up at [console.groq.com](https://console.groq.com)
- Create an API key (free tier: 30 requests/min)

### 2. Deploy to Streamlit Cloud
- Fork this repo
- Go to [share.streamlit.io](https://share.streamlit.io)
- Deploy `app/streamlit_app.py`
- Add secret: `GROQ_API_KEY = "your-key-here"`

### 3. Done
The app auto-indexes `rag/chunks.jsonl` into ChromaDB on first run.

## Quick Start — Local (Ollama)

```bash
# Install dependencies
pip install -r requirements.txt

# Make sure Ollama is running
ollama serve

# Index documents (first time only)
cd rag
python temenos_rag_agent.py --ingest

# Start interactive chat
python temenos_rag_agent.py --chat

# Or with specific mode
python temenos_rag_agent.py --chat --mode testcase
python temenos_rag_agent.py --chat --mode fitment
python temenos_rag_agent.py --chat --mode solution
```

## Re-Crawling Documentation

If you need to re-scrape the Temenos docs:

### Markdown crawler (for RAG)
```bash
cd crawler
python temenos_crawler_v2.py --login    # login manually
python temenos_crawler_v2.py --crawl    # deep recursive crawl
python temenos_crawler_v2.py --rag      # build RAG chunks
python temenos_crawler_v2.py --compile  # compile single file
```

### HTML offline mirror (with CSS)
```bash
cd webscraping
pip install -r requirements.txt
playwright install chromium
python scraper.py --fresh               # login + scrape with CSS
```

## Project Structure

```
TemenosTPH/
├── app/                          # Streamlit cloud app
│   ├── streamlit_app.py          # Web UI (Groq + ChromaDB)
│   └── requirements.txt
├── crawler/                      # Documentation scraper
│   └── temenos_crawler_v2.py     # Deep recursive crawler
├── webscraping/                  # HTML offline mirror
│   ├── scraper.py                # Playwright scraper with CSS
│   ├── login.py                  # Session login helper
│   └── requirements.txt
├── rag/                          # RAG data + agent
│   ├── temenos_rag_agent.py      # Local Ollama RAG agent
│   ├── chunks.jsonl              # 7000+ doc chunks (13 MB)
│   ├── metadata.json             # Page index with hierarchy
│   └── nav.json                  # Navigation metadata
├── docs/                         # Scraped documentation (425 pages)
│   ├── *.md                      # Individual page markdowns
│   └── compiled/
│       └── FULL_PAYMENTS.md      # Single compiled file (7.5 MB)
├── openclaw/                     # OpenClaw agent skill
│   ├── SKILL.md                  # Consultant skill definition
│   └── scripts/
│       ├── ingest_temenos.py     # Ingest into OpenClaw RAG
│       └── query_temenos.py      # Query knowledge base
├── requirements.txt              # Local dependencies
├── .gitignore
└── README.md
```

## Data Source

All documentation scraped from `https://docs.temenos.com/docs/Solutions/Payments/` (requires authentication).

## Tech Stack

| Component | Local | Cloud |
|-----------|-------|-------|
| LLM | Ollama (phi3:mini / mistral) | Groq (llama-3.3-70b) |
| Vector DB | ChromaDB (local) | ChromaDB (embedded) |
| Embeddings | all-MiniLM-L6-v2 | all-MiniLM-L6-v2 |
| UI | Terminal CLI | Streamlit |
| Crawler | Playwright + BeautifulSoup | — |
