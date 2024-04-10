from fastapi import status
from fastapi.responses import ORJSONResponse, Response
from fastapi.routing import APIRouter

from core.config import logger
from models.response import AppResponse

router = APIRouter(prefix="/predictions", tags=["predictions"])


@router.get(
    path="",
    responses={
        status.HTTP_200_OK: {"model": AppResponse},
    },
    summary="Метод для получения предсказания.",
    description="""
Метод позволяет получить предсказание по одной или трём картам.
""",
)
async def prediction() -> Response:
    resp = AppResponse(code=200, description="It's ok.").model_dump()
    logger.info(f"Return {resp}")
    return ORJSONResponse(content=resp)
