from datetime import datetime

from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse, Response

from app.core.config import settings
from app.models.response import AppResponse

router = APIRouter()


@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {"model": AppResponse},
    },
    summary="Метод для получения информации о приложении.",
    include_in_schema=False,
    description="""
Метод возвращает информацию о приложении.
""",
)
async def root() -> Response:
    return ORJSONResponse(
        content=AppResponse(
            payload={
                "project": settings.app.NAME,
                "datetime": datetime.now().isoformat(),
                "root_path": str(settings.app.BASE_DIR),
            },
            error=None,
        ).model_dump()
    )
