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
