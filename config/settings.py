from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    AUTH_TOKEN: str = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    )

    class Config:
        env_file = ".env"  # Load environment variables from .env file


settings = Settings()
