from fastapi import APIRouter

from app.schemas.analysis import AnalyzeRequest, AnalyzeResponse
from app.services.analysis_service import analyze_transcript


router = APIRouter(
    prefix="/api",
    tags=["Analysis"]
)


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_call(data: AnalyzeRequest):

    return analyze_transcript(data)