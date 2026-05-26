import os
import chromadb
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FakeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
chroma_client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)


def get_vector_store(collection_name: str = "agent_memory") -> Chroma:
    embeddings = FakeEmbeddings(size=768)
    return Chroma(client=chroma_client, collection_name=collection_name, embedding_function=embeddings)


def add_documents(texts: list, metadatas: list = None, collection_name: str = "agent_memory"):
    try:
        vs = get_vector_store(collection_name)
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.create_documents(texts, metadatas=metadatas)
        vs.add_documents(chunks)
        return len(chunks)
    except Exception as e:
        print(f"Memory warning: {e}")
        return 0


def search(query: str, k: int = 5, collection_name: str = "agent_memory") -> list:
    try:
        vs = get_vector_store(collection_name)
        results = vs.similarity_search(query, k=k)
        return [doc.page_content for doc in results]
    except Exception:
        return []
