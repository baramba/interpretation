from enum import StrEnum

from sqlmodel import SQLModel

from app.models.card import CardPublic
from app.models.common import DatetimeMixin, IdMixin
from app.models.response import AppResponse


class InterpretationBase(SQLModel):
    text: str


class Interpretation(IdMixin, DatetimeMixin, InterpretationBase, table=True):
    ...


class PredictionCreate(InterpretationBase):
    ...


class InterpretationPublic(InterpretationBase):
    cards: tuple[CardPublic]


class InterpretationResponse(AppResponse[InterpretationPublic]):
    payload: InterpretationPublic | None


class InterpretationSubject(StrEnum):
    money = "MONEY"
    love = "LOVE"
    career = "CAREER"
    health = "HEALTH"
    friendship = "FRIENDSHIP"


class InterpretationOne(SQLModel):
    subject: InterpretationSubject


class InterpretationThree(SQLModel):
    subject: InterpretationSubject
