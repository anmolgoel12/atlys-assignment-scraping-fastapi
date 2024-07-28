from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    class Config:
        env_file = ".env"  # Load environment variables from .env file


settings = Settings()
