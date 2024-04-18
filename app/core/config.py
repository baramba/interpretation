import logging
import pathlib
from logging.config import dictConfig
from pathlib import Path

from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings

from app.core.logger import LogConfig

# For Alembic could use app.core.config.settings from command line
load_dotenv(f"{pathlib.Path().resolve()}/.env")


class Application(BaseSettings):
    BASE_DIR: Path = pathlib.Path().resolve()
    LOG_FORMAT: str = "json"
    LOG_LEVEL: str = "INFO"
    CONTEXT: str = "/api"
    ABOUT: str = "/about"
    PROJECT_NAME: str = "Predictions"

    class Config:
        env_prefix = "APP_"


class Database(BaseSettings):
    HOST: str = "192.168.1.1"
    USER: str = "user_not_se"
    PASSWORD: str = "password_not_set"
    DBNAME: str = "predictions"
    SCHEMA: str = "postgresql+asyncpg"
    PORT: int = 5432

    # SQLAlchemy URI - postgresql+asyncpg://user:password@host:port/dbname[?key=value&key=value...]
    @property
    def DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl(url=f"{self.SCHEMA}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DBNAME}")

    class Config:
        env_prefix = "DB_"


class Settings(BaseSettings):
    app: Application = Application()
    db: Database = Database()


settings = Settings()

log_config = LogConfig().model_dump()
for handler in log_config["handlers"].values():
    handler["formatter"] = settings.app.LOG_FORMAT


dictConfig(config=log_config)
logger: logging.Logger = logging.getLogger(log_config["logger_name"])
logger.setLevel(settings.app.LOG_LEVEL)
