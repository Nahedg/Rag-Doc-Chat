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
- Active document shown in the left sidebar (persisted after refresh)

### Tech Stack
| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| AI / RAG | LangChain, Ollama (llama3.1) |
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
ollama pull llama3.1          # LLM for answers (~4.7GB, better quality)
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
pip install langchain langchain-community langchain-ollama langchain-chroma pypdf chromadb fastapi uvicorn python-multipart aiofiles
```

---

### 3. Process a PDF

Place a PDF file in the `data/` folder, then run:

```bash
python backend/ingest.py
```

This loads the PDF, splits it into chunks, creates embeddings and stores everything in ChromaDB.

---

### 4. Start the Server

Make sure Ollama is running (`ollama serve`), then:

```bash
uvicorn backend.main:app --reload
```

Browser: `http://localhost:8000`  
API docs: `http://localhost:8000/docs`

### 5. Use the Frontend

Open `http://localhost:8000` and:

1. Upload one PDF file
2. Ask questions in the chat panel
3. Check the left sidebar for the currently active document

The active document name is stored in browser `localStorage`, so it remains visible after page refresh.

---

## RAG Configuration

The following settings are tuned for better retrieval accuracy:

| Setting | Value | Reason |
|---|---|---|
| `chunk_size` | 300 | Smaller chunks = more precise retrieval |
| `chunk_overlap` | 100 | Prevents important sentences from being cut off at chunk boundaries |
| `search_type` | `mmr` | Maximal Marginal Relevance: picks diverse chunks, avoids redundancy |
| `fetch_k` | 30 | Fetches 30 candidates from ChromaDB, then selects the best 8 |
| `k` | 8 | Passes 8 diverse chunks as context to the LLM |

---

## Inspect ChromaDB (optional)

The vector database can be viewed directly in VS Code:

1. Install extension: **SQLite Viewer** by `qwtel` (VS Code Marketplace)
2. Open file: `chroma_db/chroma.sqlite3`

---

## Dependencies

| Package | Purpose |
|---|---|
| `langchain` | RAG framework |
| `langchain-community` | Loaders & vectorstore integrations |
| `langchain-ollama` | Ollama LLM & embeddings integration |
| `langchain-chroma` | ChromaDB vectorstore integration |
| `pypdf` | PDF parsing |
| `chromadb` | Vector database |
| `fastapi` + `uvicorn` | Web server |
| `python-multipart` | Required for FastAPI file uploads (PDF) |
| `aiofiles` | Required to serve frontend static files with FastAPI |

---

## Status

🚧 **In development**

- [x] ingest.py – PDF → ChromaDB (Ollama)
- [x] retriever.py – RAG chain
- [x] main.py – FastAPI backend (`/upload` & `/chat`)
- [x] frontend – Chat UI with active document sidebar

---

## License

MIT
