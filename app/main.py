import io
from functools import lru_cache

import yaml
from fastapi import FastAPI, Response

from app.api import metadata
from app.api.routers import api_about, api_v1_router
from app.core.config import settings
from app.core.lifespan import lifespan
from app.core.middlewares.create_context import CreateContextMiddleware

app = FastAPI(
    title=settings.app.NAME,
    docs_url="/docs/swagger",
    openapi_url="/docs/openapi.json",
    openapi_tags=metadata.tags,
    description=metadata.description,
    lifespan=lifespan,
)
app.add_middleware(CreateContextMiddleware)

app.include_router(api_about)
app.include_router(api_v1_router)


# OpenAPI в yaml формате
@app.get("/openapi.yaml", include_in_schema=False)
@lru_cache
def read_openapi_yaml() -> Response:
    openapi_json = app.openapi()
    yaml_s = io.StringIO()
    yaml.dump(openapi_json, yaml_s, encoding="utf-8", sort_keys=False, allow_unicode=True)
    return Response(yaml_s.getvalue(), media_type="text/yaml")
