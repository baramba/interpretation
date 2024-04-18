from typing import Any

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["about"])


@router.get(
    path="/",
    summary="Метод для получения информации о приложении.",
    description="""
Метод возвращает информацию о приложении.
""",
)
async def root() -> dict[str, dict[Any, Any]]:
    return {
        "message": {
            "Project": settings.app.PROJECT_NAME,
            "Path": settings.app.BASE_DIR,
        },
    }
