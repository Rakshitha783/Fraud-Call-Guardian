from app.schemas.analysis import AnalyzeRequest, AnalyzeResponse
from app.ai.keyword_detector import detect_keywords
from app.ai.risk_engine import calculate_risk, get_risk_level
from app.ai.scam_classifier import classify_scam


def analyze_transcript(data: AnalyzeRequest) -> AnalyzeResponse:

    transcript = data.transcript

    # Detect suspicious indicators
    indicators = detect_keywords(transcript)

    # Calculate risk
    risk_score = calculate_risk(indicators)

    # Determine risk level
    risk_level = get_risk_level(risk_score)

    # Classify scam category 
    scam_category = classify_scam(transcript)

    # Basic confidence for our baseline system
    confidence = min(risk_score / 100, 0.99)

    if risk_level == "CRITICAL":
        recommendation = "Do not share OTP, passwords, PINs or banking credentials."
    elif risk_level == "HIGH":
        recommendation = "Do not make payments or share sensitive information."
    elif risk_level == "SUSPICIOUS":
        recommendation = "Verify the caller before taking any action."
    else:
        recommendation = "No major fraud indicators detected."

    return AnalyzeResponse(
        risk_score=risk_score,
        risk_level=risk_level,
        scam_category=scam_category,
        confidence=confidence,
        indicators=indicators,
        recommendation=recommendation,
        transcript=transcript
    )