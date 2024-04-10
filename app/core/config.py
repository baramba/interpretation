import logging
from logging.config import dictConfig
from pathlib import Path

from pydantic_settings import BaseSettings

from core.logger import LogConfig


class Application(BaseSettings):
    BASE_DIR: Path = Path(__file__).absolute().parent.parent
    LOG_FORMAT: str = "json"
    LOG_LEVEL: str = "INFO"
    CONTEXT: str = "/api"
    ABOUT: str = f"{CONTEXT}/about"

    class Config:
        env_prefix = "APP_"


class Settings(BaseSettings):
    PROJECT_NAME: str = "Predictions"
    app: Application = Application()


settings = Settings()

log_config = LogConfig().model_dump()
for handler in log_config["handlers"].values():
    handler["formatter"] = settings.app.LOG_FORMAT


dictConfig(config=log_config)
logger: logging.Logger = logging.getLogger(log_config["logger_name"])
logger.setLevel(settings.app.LOG_LEVEL)
