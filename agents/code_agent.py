import os
from langchain_groq import ChatGroq
from memory.vector_store import search, add_documents
from dotenv import load_dotenv

load_dotenv()


def get_llm(temperature: float = 0.2) -> ChatGroq:
    return ChatGroq(
        model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=temperature,
    )


def run_code_generation(requirement: str, language: str = "Python") -> str:
    llm = get_llm(0.2)
    context = search(requirement, k=3)
    context_text = "\n".join(context) if context else "No prior context."
    prompt = f"""You are an Expert Software Engineer. Generate {language} code for:
{requirement}

Context: {context_text}

Provide complete, production-ready code with comments, error handling, type hints, and example usage."""
    result = llm.invoke(prompt)
    add_documents([result.content], metadatas=[{"type": "code", "language": language}])
    return result.content
