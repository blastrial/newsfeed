from fastapi import FastAPI
from src.config import APP_NAME, APP_VERSION
from src.schemas import HealthResponse, VersionResponse, SourceResponse

app = FastAPI(title=APP_NAME, version=APP_VERSION)

SOURCES = [
    {
        "name": "BBC",
        "category": "general",
        "url": "https://feeds.bbci.co.uk/news/rss.xml",
    },
    {
        "name": "Reuters",
        "category": "general",
        "url": "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
    },
]


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


@app.get("/sources", response_model=list[SourceResponse])
def list_sources():
    return [SourceResponse(**item) for item in SOURCES]
