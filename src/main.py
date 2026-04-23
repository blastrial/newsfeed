from fastapi import FastAPI
from src.config import APP_NAME, APP_VERSION
from src.schemas import (
    HealthResponse,
    VersionResponse,
    SourceResponse,
    ArticleResponse,
)

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

ARTICLES = [
    {
        "title": "Global markets start the week higher",
        "source": "Reuters",
        "summary": "Markets opened higher as investors reacted to new economic signals.",
    },
    {
        "title": "Technology trends reshape media industry",
        "source": "BBC",
        "summary": "New AI tools are changing how content is produced and summarized.",
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


@app.get("/articles", response_model=list[ArticleResponse])
def list_articles():
    return [ArticleResponse(**item) for item in ARTICLES]
