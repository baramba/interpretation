from typing import Annotated

from fastapi import Depends, status
from fastapi.responses import ORJSONResponse, Response
from fastapi.routing import APIRouter

from app.core.config import logger
from app.models.response import AppResponse
from app.services.prediction import PredictionService, get_prediction_service

router = APIRouter(prefix="/predictions", tags=["predictions"])

PredictionDep = Annotated[PredictionService, Depends(get_prediction_service)]


@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {"model": AppResponse},
    },
    summary="Метод для получения предсказания.",
    description="""
Метод позволяет получить предсказание по одной или трём картам.
""",
)
async def prediction(prediction_service: PredictionDep) -> Response:
    prediction = await prediction_service.get_prediction("1_2_3")
    resp = AppResponse(code=200, description=prediction).model_dump()
    logger.info(f"Return {resp}")
    return ORJSONResponse(content=resp)
