# NewsFeed

NewsFeed is a multi-source news collection and summarization system.

## Goals

- collect news from multiple sources
- parse RSS feeds
- prepare scraping infrastructure
- build AI/NLP summarization flow
- provide a simple backend API

## Current Status

Initial FastAPI project structure is ready.
Basic services layer is added.
Parser and fetcher modules are connected.
A stats endpoint is added.
A first article endpoint is added.
A settings endpoint is added.
A categories endpoint is added.

## Project Files

- `src/main.py`
- `src/config.py`
- `src/schemas.py`
- `src/services.py`
- `src/utils.py`
- `src/parsers.py`
- `src/fetchers.py`

## Endpoints

- `/`
- `/health`
- `/version`
- `/sources`
- `/articles`
- `/articles/first`
- `/feed/default`
- `/stats`
- `/settings`
- `/categories`
