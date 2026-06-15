from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Load PDF
loader = PyPDFLoader(os.path.join(PROJECT_DIR, "data", "Documentation.pdf"))
pages = loader.load()
print(f"Pages loaded: {len(pages)}")

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
chunks = splitter.split_documents(pages)
print(f"Chunks created: {len(chunks)}")

# 3. Create embeddings and store in ChromaDB (via Ollama)
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory=os.path.join(PROJECT_DIR, "chroma_db"))
print(f"Done – ChromaDB saved in: {PROJECT_DIR}/chroma_db/")
