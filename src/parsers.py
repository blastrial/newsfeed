from src.fetchers import fetch_sample_feed


def parse_feed_items():
    items = fetch_sample_feed()

    return [
        {
            "title": item["title"],
            "source": item["source"],
            "summary": item["summary"],
            "category": item["category"],
        }
        for item in items
    ]
