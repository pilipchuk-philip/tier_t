from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = "test"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./link.db"
    num_url_chars: int = 8

    class Config:
        env_file = "../../.env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()

