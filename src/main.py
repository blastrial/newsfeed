from fastapi import FastAPI
from src.config import APP_NAME, APP_VERSION

app = FastAPI(title=APP_NAME, version=APP_VERSION)


@app.get("/")
def home():
    return {
        "project": APP_NAME,
        "message": "NewsFeed API is running",
        "version": APP_VERSION,
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/version")
def version():
    return {
        "version": APP_VERSION
    }
