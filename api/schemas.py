from pydantic import BaseModel
from typing import Optional


class ResearchRequest(BaseModel):
    topic: str


class CodeRequest(BaseModel):
    requirement: str
    language: str = "Python"


class DebugRequest(BaseModel):
    code: str
    error: Optional[str] = ""


class SummarizeRequest(BaseModel):
    text: str
    style: str = "bullet"


class CrewRequest(BaseModel):
    topic: str
    code_requirement: Optional[str] = ""
