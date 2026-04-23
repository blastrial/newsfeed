from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class VersionResponse(BaseModel):
    version: str


class SourceResponse(BaseModel):
    name: str
    category: str
    url: str


class ArticleResponse(BaseModel):
    title: str
    source: str
    summary: str


class FeedRequest(BaseModel):
    category: str
    limit: int


class StatsResponse(BaseModel):
    total_sources: int
    total_articles: int
