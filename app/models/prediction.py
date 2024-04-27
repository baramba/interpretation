import uuid
from enum import StrEnum

from sqlmodel import Field, SQLModel

from app.models.card import Card
from app.models.response import AppResponse


class PredictionBase(SQLModel):
    text: str


class Prediction(PredictionBase, table=True):
    id: uuid.UUID = Field(default=None, primary_key=True)


class PredictionCreate(PredictionBase):
    ...


class PredictionPublic(PredictionBase):
    id: uuid.UUID
    cards: list[Card]


class PredictionResponse(AppResponse[PredictionPublic]):
    payload: PredictionPublic | None


class PredictionSubject(StrEnum):
    money = "MONEY"
    love = "LOVE"
    career = "CAREER"
    health = "HEALTH"
    friendship = "FRIENDSHIP"


class PredictionOne(SQLModel):
    subject: PredictionSubject


class PredictionThree(SQLModel):
    subject: PredictionSubject
