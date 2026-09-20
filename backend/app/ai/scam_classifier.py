SCAM_PATTERNS = {
    "BANKING_SCAM": [
        "bank account",
        "bank officer",
        "bank representative",
        "account will be blocked",
        "account blocked"
    ],

    "UPI_PAYMENT_SCAM": [
        "upi",
        "send money",
        "transfer money",
        "make a payment",
        "payment"
    ],

    "KYC_SCAM": [
        "kyc",
        "kyc update",
        "kyc expired",
        "verify your kyc",
        "documents"
    ],

    "POLICE_IMPERSONATION": [
        "police",
        "arrest",
        "court case",
        "legal action",
        "cyber crime"
    ],

    "JOB_SCAM": [
        "job offer",
        "work from home",
        "job opportunity",
        "registration fee",
        "job vacancy"
    ],

    "INVESTMENT_SCAM": [
        "investment",
        "invest now",
        "guaranteed returns",
        "double your money",
        "trading profit"
    ],

    "DELIVERY_SCAM": [
        "delivery",
        "courier",
        "parcel",
        "package",
        "delivery fee"
    ],

    "LOTTERY_SCAM": [
        "lottery",
        "you have won",
        "prize",
        "lucky draw",
        "reward"
    ],

    "CREDENTIAL_SCAM": [
        "password",
        "pin",
        "cvv",
        "card number",
        "login details"
    ]
}


def classify_scam(transcript: str) -> str:

    text = transcript.lower()

    category_scores = {}

    for category, keywords in SCAM_PATTERNS.items():

        score = 0

        for keyword in keywords:
            if keyword in text:
                score += 1

        if score > 0:
            category_scores[category] = score

    if not category_scores:
        return "UNKNOWN"

    return max(category_scores, key=category_scores.get)