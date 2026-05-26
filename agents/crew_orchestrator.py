from agents.research_agent import run_research
from agents.code_agent import run_code_generation
from agents.summarize_agent import run_summarize


def run_research_and_code_crew(topic: str, code_requirement: str) -> dict:
    research_result = run_research(topic)
    code_result = run_code_generation(code_requirement or topic)
    return {"research": research_result, "code": code_result, "status": "success"}


def run_full_pipeline(topic: str) -> dict:
    research_result = run_research(topic)
    summary = run_summarize(research_result)
    return {"research": research_result, "summary": summary, "status": "success"}
