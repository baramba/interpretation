from typing import Annotated

from fastapi import Depends, status
from fastapi.responses import ORJSONResponse, Response
from fastapi.routing import APIRouter

from app.api.api_deps import x_correlation_id, x_user_id
from app.core.config import logger
from app.models.prediction import PredictionResponse, PredictionSubject
from app.models.response import AppResponse
from app.services.prediction import PredictionService, get_prediction_service

router = APIRouter(
    dependencies=[
        Depends(x_correlation_id),
        Depends(x_user_id),
    ],
)

PredictionServiceDep = Annotated[PredictionService, Depends(get_prediction_service)]
UserIdDep = Annotated[str, Depends(x_user_id)]


@router.get(
    path="/one",
    responses={
        status.HTTP_200_OK: {"model": PredictionResponse},
    },
    summary="Метод для получения предсказания.",
    description="""
Метод позволяет получить предсказание по одной карте.
""",
)
async def prediction_one(
    prediction_service: PredictionServiceDep,
    user_id: UserIdDep,
    subject: PredictionSubject,
) -> Response:
    prediction = await prediction_service.get_prediction("1_2_3")
    resp = AppResponse(payload={"user_id": user_id, "subject": subject}, error=None).model_dump()
    logger.info(f"Return {resp} - {prediction}")
    return ORJSONResponse(content=resp)


@router.get(
    path="/three",
    responses={
        status.HTTP_200_OK: {"model": PredictionResponse},
    },
    summary="Метод для получения предсказания.",
    description="""
Метод позволяет получить предсказание по комбинации из трёх карт.
""",
)
async def prediction_three(
    prediction_service: PredictionServiceDep,
    subject: PredictionSubject,
    user_id: UserIdDep,
) -> Response:
    prediction = await prediction_service.get_prediction("1_2_3")
    resp = AppResponse(payload={"user_id": user_id, "subject": subject}, error=None).model_dump()

    logger.info(f"Return {resp} {prediction}")
    return ORJSONResponse(content=resp)
