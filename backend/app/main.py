from fastapi import FastAPI

from app.api.analysis import router as analysis_router


app = FastAPI(
    title="Fraud Call Guardian API",
    description="AI-powered real-time fraud prevention backend",
    version="1.0.0"
)


app.include_router(analysis_router)


@app.get("/")
def root():
    return {
        "message": "Fraud Call Guardian API is running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Fraud Call Guardian Backend"
    }