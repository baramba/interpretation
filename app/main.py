from fastapi import FastAPI

from app.api import metadata
from app.api.routers import api_v1_about, api_v1_router
from app.core.config import settings
from app.core.lifespan import lifespan

app = FastAPI(
    title=settings.app.PROJECT_NAME,
    docs_url="/docs/swagger",
    openapi_url="/docs/openapi",
    openapi_tags=metadata.tags,
    description=metadata.description,
    root_path=settings.app.CONTEXT,
)
app.openapi_version = "3.1.0"

app = FastAPI(lifespan=lifespan)

app.include_router(api_v1_about)
app.include_router(api_v1_router)
