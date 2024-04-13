from typing import Any

from fastapi import APIRouter

from core.config import settings

about_router = APIRouter(tags=["about"])


@about_router.get(
    path=settings.app.ABOUT,
    summary="Метод для получения информации о приложении.",
    description="""
Метод возвращает информацию о приложении.
""",
)
async def root() -> dict[str, dict[Any, Any]]:
    return {
        "message": {
            "Project": settings.PROJECT_NAME,
            "Path": settings.app.BASE_DIR,
        },
    }
