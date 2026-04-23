def normalize_text(value: str) -> str:
    return value.strip()


def shorten_text(value: str, limit: int = 120) -> str:
    text = value.strip()
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."
