from src.config import DEFAULT_CATEGORY
from src.parsers import parse_feed_items
from src.utils import normalize_text, shorten_text


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
        }
        for item in raw_items
    ]
