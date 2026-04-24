def normalize_text(value: str) -> str:
    return value.strip()


def shorten_text(value: str, limit: int = 120) -> str:
    text = value.strip()
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."


def make_slug(value: str) -> str:
    return value.strip().lower().replace(" ", "-")


def unique_list(values: list[str]) -> list[str]:
    return sorted(set(values))
