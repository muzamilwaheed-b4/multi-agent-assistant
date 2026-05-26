import os
from langchain_groq import ChatGroq
from memory.vector_store import search
from dotenv import load_dotenv

load_dotenv()


def get_llm(temperature: float = 0.1) -> ChatGroq:
    return ChatGroq(
        model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=temperature,
    )


def run_debug(code: str, error: str = "") -> str:
    llm = get_llm(0.1)
    context = search(error or code[:200], k=3)
    context_text = "\n".join(context) if context else ""
    error_text = error if error else "Check for potential bugs"
    prompt = (
        "You are an Expert Debugger. Debug this code:\n\n"
        f"{code}\n\n"
        f"Error: {error_text}\n"
        f"Context: {context_text}\n\n"
        "Provide: 1) Root cause 2) Fixed code 3) Explanation of changes"
    )
    result = llm.invoke(prompt)
    return result.content
