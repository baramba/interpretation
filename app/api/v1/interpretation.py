import uuid
from typing import Annotated

from fastapi import Depends, status
from fastapi.responses import ORJSONResponse, Response
from fastapi.routing import APIRouter

from app.api.api_deps import x_correlation_id, x_user_id
from app.core.config import app_logger
from app.models.interpretation import InterpretationResponse, InterpretationSubject
from app.services.interpretation import InterpretationService, get_interpretation_service

router = APIRouter(
    dependencies=[
        Depends(x_correlation_id),
        Depends(x_user_id),
    ],
)

InterpretationDeps = Annotated[InterpretationService, Depends(get_interpretation_service)]
UserIdDep = Annotated[uuid.UUID, Depends(x_user_id)]


class Deps:
    def __init__(self, interpretation_service: InterpretationDeps):
        self.interpretation_service = interpretation_service


class Params:
    def __init__(self, user_id: UserIdDep, subject: InterpretationSubject):
        self.user_id = user_id
        self.subject = subject


@router.get(
    path="/one",
    responses={
        status.HTTP_200_OK: {"model": InterpretationResponse},
    },
    summary="Метод для получения предсказания.",
    description="""
Метод позволяет получить предсказание по одной карте.
""",
)
async def interpretation_one(
    params: Annotated[Params, Depends(Params)],
    deps: Annotated[Deps, Depends(Deps)],
) -> Response:
    prediction = await deps.interpretation_service.get_interpretation_one(params.user_id, params.subject)
    resp = InterpretationResponse(payload=prediction, error=None).model_dump()
    return ORJSONResponse(content=resp)


@router.get(
    path="/three",
    responses={
        status.HTTP_200_OK: {"model": InterpretationResponse},
    },
    summary="Метод для получения предсказания.",
    description="""
Метод позволяет получить предсказание по комбинации из трёх карт.
""",
)
async def interpretation_three(
    params: Annotated[Params, Depends(Params)],
    deps: Annotated[Deps, Depends(Deps)],
) -> Response:
    prediction = await deps.interpretation_service.get_interpretation_one(params.user_id, params.subject)
    resp = InterpretationResponse(payload=prediction, error=None).model_dump()
    app_logger.info(f"Return {resp} {prediction}")
    return ORJSONResponse(content=resp)
