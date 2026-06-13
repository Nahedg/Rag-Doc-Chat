# RAG Doc Chat

> **A RAG-based document chatbot — upload PDFs, ask questions, get answers with source references.**

---

**RAG Doc Chat** is an AI-powered document chatbot built on Retrieval-Augmented Generation (RAG).

### Features
- Upload and process PDF documents
- Semantic search over document content
- Answers with direct source attribution
- Lightweight web interface

### Tech Stack
| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| AI / RAG | LangChain, OpenAI / local LLM |
| Vector Database | ChromaDB |
| Frontend | HTML, CSS, JavaScript |

---

## Project Structure *(planned)*

```
rag-doc-chat/
├── backend/
│   ├── main.py          # FastAPI app
│   ├── ingest.py        # PDF processing & embedding
│   └── retriever.py     # RAG chain
├── frontend/
│   └── index.html       # Chat UI
├── data/                # Uploaded PDFs (local, not tracked)
├── requirements.txt
└── README.md
```

---

## Status

🚧 **In development** — implementation starting soon.

---

## License

MIT
