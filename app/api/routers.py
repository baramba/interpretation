from fastapi import APIRouter

from app.api.v1 import about, predictions
from app.core.config import settings

api_v1_router = APIRouter(prefix="/v1")
api_v1_router.include_router(predictions.router, tags=["predictions"])

api_v1_about = APIRouter(prefix=settings.app.ABOUT)
api_v1_about.include_router(about.router, tags=["predictions"])
