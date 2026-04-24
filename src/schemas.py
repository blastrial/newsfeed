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
    slug: str
    category: str
    language: str


class FeedRequest(BaseModel):
    category: str
    limit: int


class StatsResponse(BaseModel):
    total_sources: int
    total_articles: int


class SettingsResponse(BaseModel):
    category: str
    limit: int
    language: str


class CategoryListResponse(BaseModel):
    categories: list[str]


class SummaryPreviewRequest(BaseModel):
    text: str


class SummaryPreviewResponse(BaseModel):
    original_text: str
    short_summary: str
