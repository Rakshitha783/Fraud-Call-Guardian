from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    transcript: str


class AnalyzeResponse(BaseModel):
    risk_score: int
    risk_level: str
    scam_category: str
    confidence: float
    indicators: list[str]
    recommendation: str
    transcript: str