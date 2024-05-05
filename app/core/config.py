import gettext
import logging
import pathlib
from logging.config import dictConfig
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field, PostgresDsn
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings

from app.core.logger import LogConfig

# For Alembic could use app.core.config.settings from command line
load_dotenv(f"{pathlib.Path().resolve()}/.env")


class Application(BaseSettings):
    TOGETHER_API_KEY: str = Field(default=...)
    BASE_DIR: Path = pathlib.Path().resolve()
    LOG_FORMAT: str = "json"
    LOG_LEVEL: str = "INFO"
    CONTEXT: str = "/api"
    ABOUT: str = "/about"
    NAME: str = Field(default="Predictions", frozen=True)
    PROXY_URL: str | None = None

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
app_logger: logging.Logger = logging.getLogger(log_config["logger_name"])
app_logger.setLevel(settings.app.LOG_LEVEL)


gettext.install(settings.app.NAME, f"{settings.app.BASE_DIR}/locale")
