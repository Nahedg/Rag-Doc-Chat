# RAG Doc Chat

> **A RAG-based document chatbot — upload PDFs, ask questions, get answers with source references.**

---

**RAG Doc Chat** is an AI-powered document chatbot built on Retrieval-Augmented Generation (RAG). It runs fully locally using Ollama – no API key required.

### Features
- Upload and process PDF documents
- Semantic search over document content
- Answers with direct source attribution
- Runs fully locally with Ollama (no API key needed)
- Lightweight web interface

### Tech Stack
| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| AI / RAG | LangChain, Ollama (llama3.2) |
| Embeddings | Ollama (nomic-embed-text) |
| Vector Database | ChromaDB |
| Frontend | HTML, CSS, JavaScript |

---

## Project Structure

```
Rag-Doc-Chat/
├── backend/
│   ├── ingest.py        # Load PDF, chunking, embeddings → ChromaDB
│   ├── retriever.py     # RAG chain: question → relevant chunks → answer
│   └── main.py          # FastAPI app (upload & chat endpoints)
├── frontend/
│   └── index.html       # Chat UI
├── data/                # PDFs (local, not tracked)
├── chroma_db/           # Vector database (local, not tracked)
├── venv/                # Virtual environment (not tracked)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup

### 1. Install Ollama

Download Ollama from [ollama.com](https://ollama.com) or via Homebrew:

```bash
brew install ollama
```

Pull the required models:

```bash
ollama pull llama3.2          # LLM for answers (~2GB)
ollama pull nomic-embed-text  # Embeddings model (~274MB)
```

Start Ollama:

```bash
ollama serve
```

---

### 2. Project Setup

```bash
git clone https://github.com/YOUR-USERNAME/Rag-Doc-Chat.git
cd Rag-Doc-Chat

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install langchain langchain-community langchain-ollama pypdf chromadb fastapi uvicorn
```

---

### 3. Process a PDF

Place a PDF file in the `data/` folder, then run:

```bash
python backend/ingest.py
```

This loads the PDF, splits it into chunks, creates embeddings and stores everything in ChromaDB.

---

### 4. Start the Server *(coming soon)*

```bash
uvicorn backend.main:app --reload
```

Browser: `http://localhost:8000`

---

## Inspect ChromaDB (optional)

The vector database can be viewed directly in VS Code:

1. Install extension: **SQLite Viewer** by `qwtel` (VS Code Marketplace)
2. Open file: `chroma_db/chroma.sqlite3`

Or via terminal:

```bash
chroma run --path chroma_db
# Browser: http://localhost:8000
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `langchain` | RAG framework |
| `langchain-community` | Loaders & vectorstore integrations |
| `langchain-ollama` | Ollama integration |
| `pypdf` | PDF parsing |
| `chromadb` | Vector database |
| `fastapi` + `uvicorn` | Web server |

---

## Status

🚧 **In development**

- [x] ingest.py – PDF → ChromaDB (Ollama)
- [ ] retriever.py – RAG chain
- [ ] main.py – FastAPI backend
- [ ] frontend – Chat UI

---

## License

MIT
