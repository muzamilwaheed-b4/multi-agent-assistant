import os
from langchain_groq import ChatGroq
from memory.vector_store import search, add_documents
from dotenv import load_dotenv

load_dotenv()


def get_llm(temperature: float = 0.3) -> ChatGroq:
    return ChatGroq(
        model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=temperature,
    )


def run_research(topic: str) -> str:
    llm = get_llm(0.3)
    context = search(topic, k=3)
    context_text = "\n".join(context) if context else "No prior context."
    prompt = f"""You are a Senior Research Analyst. Research this topic thoroughly: {topic}

Context from knowledge base:
{context_text}

Provide a comprehensive summary with key findings, important points, and conclusions."""
    result = llm.invoke(prompt)
    add_documents([result.content], metadatas=[{"type": "research", "topic": topic}])
    return result.content
