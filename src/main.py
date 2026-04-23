from fastapi import FastAPI
from src.config import settings

app = FastAPI(title=settings.app_name, version=settings.version)


@app.get("/")
def home():
    return {
        "message": "NewsFeed API is running",
        "app": settings.app_name,
        "version": settings.version,
    }
