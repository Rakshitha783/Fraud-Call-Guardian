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
        "pay immediately",
        "payment",
        "processing fee",
        "registration fee",
        "delivery fee"
    ],

    "UPI request": [
        "upi",
        "upi payment",
        "upi transfer"
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
    ],

    "KYC request": [
        "kyc",
        "kyc update",
        "kyc expired",
        "verify your kyc",
        "documents"
    ],

    "Job scam": [
        "job offer",
        "work from home",
        "job opportunity",
        "job vacancy",
        "registration fee"
    ],

    "Investment scam": [
        "investment",
        "invest now",
        "guaranteed returns",
        "double your money",
        "trading profit"
    ],

    "Delivery scam": [
        "delivery",
        "courier",
        "parcel",
        "package",
        "delivery fee"
    ],

    "Lottery scam": [
        "lottery",
        "lottery prize",
        "you have won",
        "lucky draw",
        "reward",
        "prize"
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