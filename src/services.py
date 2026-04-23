from src.config import DEFAULT_CATEGORY
from src.utils import normalize_text


def get_sources():
    return [
        {
            "name": "BBC",
            "category": DEFAULT_CATEGORY,
            "url": "https://feeds.bbci.co.uk/news/rss.xml",
        },
        {
            "name": "Reuters",
            "category": DEFAULT_CATEGORY,
            "url": "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
        },
    ]


def get_articles():
    return [
        {
            "title": normalize_text("Global markets start the week higher"),
            "source": "Reuters",
            "summary": "Markets opened higher as investors reacted to new economic signals.",
        },
        {
            "title": normalize_text("Technology trends reshape media industry"),
            "source": "BBC",
            "summary": "New AI tools are changing how content is produced and summarized.",
        },
    ]
