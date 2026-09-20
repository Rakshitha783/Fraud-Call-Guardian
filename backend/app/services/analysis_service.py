from app.schemas.analysis import AnalyzeRequest, AnalyzeResponse


def analyze_transcript(data: AnalyzeRequest) -> AnalyzeResponse:

    transcript = data.transcript

    # Temporary dummy analysis.
    # We will replace this with the actual AI pipeline later.

    return AnalyzeResponse(
        risk_score=96,
        risk_level="CRITICAL",
        scam_category="BANKING_SCAM",
        confidence=0.96,
        indicators=[
            "OTP request",
            "Urgency",
            "Bank impersonation"
        ],
        recommendation="Do not share OTP or banking credentials.",
        transcript=transcript
    )