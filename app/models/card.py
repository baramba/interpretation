import uuid

from sqlmodel import Field, SQLModel

from app.models.common import DatetimeMixin, IdMixin


class CardBase(SQLModel):
    name: str
    description: str
    code: str


class Card(CardBase, IdMixin, DatetimeMixin, table=True):
    ...


class CardPublic(CardBase, IdMixin):
    id: uuid.UUID = Field(exclude=True)
