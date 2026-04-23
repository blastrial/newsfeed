from fastapi import FastAPI
from src.config import APP_NAME, APP_VERSION
from src.schemas import HealthResponse, VersionResponse

app = FastAPI(title=APP_NAME, version=APP_VERSION)


@app.get("/")
def home():
    return {
        "project": APP_NAME,
        "message": "NewsFeed API is running",
        "version": APP_VERSION,
    }


@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(status="ok")


@app.get("/version", response_model=VersionResponse)
def version():
    return VersionResponse(version=APP_VERSION)
