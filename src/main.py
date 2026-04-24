from fastapi import FastAPI
from src.config import (
    APP_NAME,
    APP_VERSION,
    DEFAULT_CATEGORY,
    DEFAULT_LIMIT,
    DEFAULT_LANGUAGE,
)
from src.schemas import (
    HealthResponse,
    VersionResponse,
    SourceResponse,
    ArticleResponse,
    FeedRequest,
    StatsResponse,
    SettingsResponse,
)
from src.services import get_sources, get_articles, get_stats

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


@app.get("/articles/first", response_model=ArticleResponse)
def first_article():
    return ArticleResponse(**get_articles()[0])


@app.get("/feed/default", response_model=FeedRequest)
def default_feed_settings():
    return FeedRequest(category=DEFAULT_CATEGORY, limit=DEFAULT_LIMIT)


@app.get("/stats", response_model=StatsResponse)
def stats():
    return StatsResponse(**get_stats())


@app.get("/settings", response_model=SettingsResponse)
def settings():
    return SettingsResponse(
        category=DEFAULT_CATEGORY,
        limit=DEFAULT_LIMIT,
        language=DEFAULT_LANGUAGE,
    )
