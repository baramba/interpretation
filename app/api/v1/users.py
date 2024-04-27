from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import ORJSONResponse, Response

from app.api.api_deps import x_correlation_id
from app.models.response import AppResponse
from app.models.user import UserIdResponse
from app.services.user import UserService, get_user_service

router = APIRouter(
    dependencies=[
        Depends(x_correlation_id),
    ],
)


@router.get(
    path="/id",
    responses={
        status.HTTP_200_OK: {"model": UserIdResponse},
    },
    summary="Метод генерации идентификатора пользователя",
    description="""
Метод генеренирует случайный идентификатор пользователя и записывает его в базу данных.
""",
)
async def gen_user_id(
    user_service: Annotated[UserService, Depends(get_user_service)],
) -> Response:
    user_id = await user_service.gen_user_id()
    return ORJSONResponse(
        content=AppResponse(
            payload={"user_id": user_id},
            error=None,
        ).model_dump()
    )
