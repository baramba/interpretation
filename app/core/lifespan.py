from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import app_logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    ## before application start
    app_logger.info(f"Before application '{app.title}' start")
    yield
    ## before application stop
    app_logger.info(f"Before application '{app.title}' stop")
