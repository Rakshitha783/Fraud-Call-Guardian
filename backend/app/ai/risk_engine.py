RISK_WEIGHTS = {
    "OTP request": 25,
    "Payment request": 20,
    "Bank impersonation": 15,
    "Urgency": 15,
    "Threat": 10,
    "Credential request": 20
}


def calculate_risk(indicators: list[str]) -> int:
    score = 0

    for indicator in indicators:
        score += RISK_WEIGHTS.get(indicator, 0)

    return min(score, 100)


def get_risk_level(score: int) -> str:
    if score >= 80:
        return "CRITICAL"
    elif score >= 60:
        return "HIGH"
    elif score >= 30:
        return "SUSPICIOUS"
    else:
        return "SAFE"