from enum import StrEnum

from sqlmodel import SQLModel

from app.models.card import Card
from app.models.common import ModelBaseMixin
from app.models.response import AppResponse


class PredictionBase(SQLModel):
    text: str


class Prediction(ModelBaseMixin, PredictionBase, table=True):
    ...


class PredictionCreate(PredictionBase):
    ...


class PredictionPublic(PredictionBase):
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
