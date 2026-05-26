from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
import uvicorn

app = FastAPI(
    title="Multi-Agent AI Research & Coding Assistant",
    description="4 specialized AI agents: Research, Code Generation, Debugging, Summarization",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Multi-Agent AI Assistant is running! Visit /docs"}


@app.get("/health")
def health():
    return {"status": "healthy", "agents": ["research", "code", "debug", "summarize"]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
