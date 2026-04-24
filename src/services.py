from src.config import DEFAULT_CATEGORY, DEFAULT_LANGUAGE
from src.parsers import parse_feed_items
from src.utils import normalize_text, shorten_text, make_slug


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
    raw_items = parse_feed_items()

    return [
        {
            "title": normalize_text(item["title"]),
            "source": normalize_text(item["source"]),
            "summary": shorten_text(item["summary"]),
            "slug": make_slug(item["title"]),
            "category": normalize_text(item["category"]),
        }
        for item in raw_items
    ]


def get_stats():
    return {
        "total_sources": len(get_sources()),
        "total_articles": len(get_articles()),
    }


def get_settings():
    return {
        "category": DEFAULT_CATEGORY,
        "limit": 10,
        "language": DEFAULT_LANGUAGE,
    }
