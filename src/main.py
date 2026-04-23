from fastapi import FastAPI

from src.config import settings

app = FastAPI(title=settings.app_name, version=settings.version)


@app.get("/")
def read_root():
    return {
        "app": settings.app_name,
        "version": settings.version,
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }
