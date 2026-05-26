# Multi-Agent AI Research & Coding Assistant

A production-ready multi-agent system with 4 specialized LLM agents built with LangChain, Groq, ChromaDB, and FastAPI.

## Tech Stack
- **LangChain** — LLM orchestration
- **Groq (LLaMA 3.1)** — Fast LLM inference
- **ChromaDB** — Vector memory
- **FastAPI** — REST API backend

## Agents
| Agent | Role |
|-------|------|
| 🔍 Research Agent | Deep topic research & analysis |
| 💻 Code Generation Agent | Production-ready code generation |
| 🐛 Debugging Agent | Bug detection & fixes |
| 📝 Summarization Agent | Structured summaries |

## Project Structure
```
multi-agent-assistant/
├── main.py
├── requirements.txt
├── .env.example
├── agents/
│   ├── research_agent.py
│   ├── code_agent.py
│   ├── debug_agent.py
│   ├── summarize_agent.py
│   └── crew_orchestrator.py
├── api/
│   ├── routes.py
│   └── schemas.py
└── memory/
    └── vector_store.py
```

## Setup & Run

```bash
# 1. Clone repo
git clone https://github.com/muzamilwaheed-b4/multi-agent-assistant
cd multi-agent-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup environment
cp .env.example .env
# Add your Groq API key in .env

# 4. Run
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` for Swagger UI.

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/research` | Research a topic |
| POST | `/api/v1/generate-code` | Generate code |
| POST | `/api/v1/debug` | Debug code |
| POST | `/api/v1/summarize` | Summarize text |
| POST | `/api/v1/crew/research-and-code` | Research + Code pipeline |
| POST | `/api/v1/crew/full-pipeline` | Research + Summarize pipeline |

## Get Free Groq API Key
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up → API Keys → Create API Key
