from fastapi import FastAPI
from src.config import (
    APP_NAME,
    APP_VERSION,
    DEFAULT_CATEGORY,
    DEFAULT_LIMIT,
)
from src.schemas import (
    HealthResponse,
    VersionResponse,
    SourceResponse,
    ArticleResponse,
    FeedRequest,
    StatsResponse,
)
from src.services import get_sources, get_articles

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


@app.get("/sources", response_model=list[SourceResponse])
def list_sources():
    return [SourceResponse(**item) for item in get_sources()]


@app.get("/articles", response_model=list[ArticleResponse])
def list_articles():
    return [ArticleResponse(**item) for item in get_articles()]


@app.get("/feed/default", response_model=FeedRequest)
def default_feed_settings():
    return FeedRequest(category=DEFAULT_CATEGORY, limit=DEFAULT_LIMIT)


@app.get("/stats", response_model=StatsResponse)
def stats():
    return StatsResponse(
        total_sources=len(get_sources()),
        total_articles=len(get_articles()),
    )
