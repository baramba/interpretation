import uuid

from sqlmodel import SQLModel

from app.models.response import AppResponse


class User(SQLModel):
    user_id: uuid.UUID


class UserIdResponse(AppResponse[User]):
    payload: User | None
