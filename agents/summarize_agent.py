import os
from langchain_groq import ChatGroq
from memory.vector_store import add_documents
from dotenv import load_dotenv

load_dotenv()


def get_llm(temperature: float = 0.3) -> ChatGroq:
    return ChatGroq(
        model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=temperature,
    )


def run_summarize(text: str, style: str = "bullet") -> str:
    llm = get_llm(0.3)
    prompt = f"""Summarize the following text in {style} format:

{text}

Capture: main points, key findings, and important details."""
    result = llm.invoke(prompt)
    add_documents([result.content], metadatas=[{"type": "summary"}])
    return result.content
