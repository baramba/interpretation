import uuid

from sqlmodel import Field, SQLModel


class CardBase(SQLModel):
    name: str
    description: str


class Card(CardBase, table=True):
    id: uuid.UUID = Field(default=None, primary_key=True)


class CardPublic(CardBase):
    id: uuid.UUID
