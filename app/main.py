from fastapi import FastAPI

from api.main import api_v1_router
from api.routers import metadata
from api.routers.about import about_router
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/docs/swagger",
    openapi_url="/docs/openapi",
    openapi_tags=metadata.tags,
    description=metadata.description,
    root_path=settings.app.CONTEXT,
)
app.openapi_version = "3.1.0"


app.include_router(about_router)
app.include_router(api_v1_router)
