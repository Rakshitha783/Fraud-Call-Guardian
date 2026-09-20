RISK_WEIGHTS = {
    "OTP request": 25,
    "Payment request": 20,
    "UPI request": 15,
    "Bank impersonation": 15,
    "Urgency": 15,
    "Threat": 15,
    "Credential request": 20,
    "KYC request": 15,
    "Job scam": 15,
    "Investment scam": 20,
    "Delivery scam": 15,
    "Lottery scam": 20
}


HIGH_RISK_INDICATORS = {
    "OTP request",
    "Credential request",
    "Threat"
}


HIGH_RISK_COMBINATIONS = [
    {"Payment request", "Delivery scam"},
    {"Payment request", "Investment scam"},
    {"Payment request", "Lottery scam"},
    {"Payment request", "Job scam"},
    {"Payment request", "KYC request"},
    {"Urgency", "Delivery scam"},
]


def calculate_risk(indicators: list[str]) -> int:

    score = 0

    for indicator in indicators:
        score += RISK_WEIGHTS.get(indicator, 0)

    return min(score, 100)


def get_risk_level(score: int, indicators: list[str]) -> str:

    indicator_set = set(indicators)

    # Critical signals
    if score >= 80:
        return "CRITICAL"

    # High-risk combinations
    for combination in HIGH_RISK_COMBINATIONS:
        if combination.issubset(indicator_set):
            return "HIGH"

    # High-risk individual indicators
    if any(
        indicator in HIGH_RISK_INDICATORS
        for indicator in indicators
    ):
        return "SUSPICIOUS"

    if score >= 60:
        return "HIGH"

    if score >= 30:
        return "SUSPICIOUS"

    # Certain scam categories should never be SAFE
    if "Investment scam" in indicator_set:
        return "SUSPICIOUS"

    if "Lottery scam" in indicator_set:
        return "SUSPICIOUS"

    if "Job scam" in indicator_set:
        return "SUSPICIOUS"

    if "Delivery scam" in indicator_set:
        return "SUSPICIOUS"

    return "SAFE"