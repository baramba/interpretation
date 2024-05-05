from fastapi import APIRouter

from app.api.v1 import about, interpretation, users
from app.core.config import settings

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(interpretation.router, prefix="/interpretation", tags=["prediction"])
api_v1_router.include_router(users.router, prefix="/user", tags=["user"])

api_about = APIRouter(prefix=settings.app.ABOUT)
api_about.include_router(about.router, tags=["about"])
