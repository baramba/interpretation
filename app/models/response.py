from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class AppError(BaseModel):
    type: str
    description: str


class AppResponse(BaseModel, Generic[T]):
    payload: T | None
    error: AppError | None
