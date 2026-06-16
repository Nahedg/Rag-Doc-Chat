import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

app = FastAPI()

# Allow frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(PROJECT_DIR, "data")
CHROMA_DIR = os.path.join(PROJECT_DIR, "chroma_db")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Serve frontend
app.mount("/static", StaticFiles(directory=os.path.join(PROJECT_DIR, "frontend")), name="static")

@app.get("/")
def root():
    return FileResponse(os.path.join(PROJECT_DIR, "frontend", "index.html"))

embeddings = OllamaEmbeddings(model="nomic-embed-text")

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    # Save PDF to data/
    pdf_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(pdf_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Load, split and store in ChromaDB
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
    chunks = splitter.split_documents(pages)
    Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_DIR)

    return {"message": f"'{file.filename}' uploaded and processed.", "chunks": len(chunks)}


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
async def chat(request: ChatRequest):
    if not os.path.exists(CHROMA_DIR):
        raise HTTPException(status_code=400, detail="No document uploaded yet. Please upload a PDF first.")
    vectorstore = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 8, "fetch_k": 30}
    )
    llm = OllamaLLM(model="llama3.1")
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )
    result = chain.invoke(request.question)
    return {"answer": result["result"]}
