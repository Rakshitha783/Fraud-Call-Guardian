SCAM_KEYWORDS = {
    "OTP request": [
        "otp",
        "one time password",
        "verification code",
        "security code"
    ],

    "Payment request": [
        "send money",
        "transfer money",
        "make a payment",
        "pay now",
        "upi",
        "payment"
    ],

    "Bank impersonation": [
        "bank account",
        "bank officer",
        "bank representative",
        "account will be blocked",
        "account blocked",
        "bank"
    ],

    "Urgency": [
        "immediately",
        "urgent",
        "right now",
        "within minutes",
        "act now",
        "hurry"
    ],

    "Threat": [
        "police",
        "arrest",
        "legal action",
        "court case",
        "account will be closed",
        "account will be blocked"
    ],

    "Credential request": [
        "password",
        "pin",
        "cvv",
        "card number",
        "login details"
    ]
}


def detect_keywords(transcript: str) -> list[str]:
    text = transcript.lower()

    indicators = []

    for category, keywords in SCAM_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                indicators.append(category)
                break

    return indicators