import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NAME: str = "zyt-szr"
    DEBUG: bool = False
    ENV: str = "development"

    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000

settings = Settings()
