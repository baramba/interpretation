from fastapi import APIRouter

from api.routers.v1 import predictions

api_v1_router = APIRouter(prefix="/v1")
api_v1_router.include_router(predictions.router, tags=["predictions"])
