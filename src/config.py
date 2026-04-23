from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "NewsFeed"
    version: str = "0.1.0"


settings = Settings()
