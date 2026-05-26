from fastapi import APIRouter, HTTPException
from api.schemas import ResearchRequest, CodeRequest, DebugRequest, SummarizeRequest, CrewRequest
from agents.research_agent import run_research
from agents.code_agent import run_code_generation
from agents.debug_agent import run_debug
from agents.summarize_agent import run_summarize
from agents.crew_orchestrator import run_research_and_code_crew, run_full_pipeline
from memory.vector_store import add_documents, search

router = APIRouter()


@router.post("/research")
def research(req: ResearchRequest):
    try:
        result = run_research(req.topic)
        return {"topic": req.topic, "result": result, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate-code")
def generate_code(req: CodeRequest):
    try:
        code = run_code_generation(req.requirement, req.language)
        return {"requirement": req.requirement, "code": code, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/debug")
def debug(req: DebugRequest):
    try:
        analysis = run_debug(req.code, req.error)
        return {"analysis": analysis, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/summarize")
def summarize(req: SummarizeRequest):
    try:
        summary = run_summarize(req.text, req.style)
        return {"summary": summary, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/search")
def vector_search(query: str, k: int = 5):
    try:
        results = search(query, k=k)
        return {"results": results, "count": len(results)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/crew/research-and-code")
def crew_research_and_code(req: CrewRequest):
    try:
        result = run_research_and_code_crew(req.topic, req.code_requirement)
        return {"result": result, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/crew/full-pipeline")
def crew_full_pipeline(req: CrewRequest):
    try:
        result = run_full_pipeline(req.topic)
        return {"result": result, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
