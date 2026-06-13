from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

# Load ChromaDB
vectorstore = Chroma(persist_directory="chroma_db", embedding_function=OllamaEmbeddings(model="nomic-embed-text"))
print("ChromaDB loaded successfully")

# Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
print("Retriever created successfully")

# RAG chain with Ollama LLM
llm = OllamaLLM(model="llama3.2")
chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

question = input("Your question: ")
answer = chain.invoke(question)
print("\nAnswer:", answer["result"])