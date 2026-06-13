from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# 1. Load PDF
loader = PyPDFLoader("data/Documentation.pdf")
pages = loader.load()
print(f"Pages loaded: {len(pages)}")

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(pages)
print(f"Chunks created: {len(chunks)}")

# 3. Create embeddings and store in ChromaDB (via Ollama)
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="chroma_db")
print("Done – ChromaDB saved in: chroma_db/")
