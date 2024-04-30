from sqlmodel import SQLModel

from app.models.common import ModelBaseMixin


class CardBase(SQLModel):
    name: str
    description: str
    code: str


class Card(CardBase, ModelBaseMixin, table=True):
    ...


class CardPublic(CardBase):
    ...
