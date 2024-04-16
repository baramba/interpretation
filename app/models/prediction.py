import uuid

from sqlmodel import Field, SQLModel


class PredictionBase(SQLModel):
    combination_hash: str
    text: str


class Prediction(PredictionBase, table=True):
    id: uuid.UUID = Field(default=None, primary_key=True)


class PredictionCreate(PredictionBase):
    ...


class PredictionPublic(PredictionBase):
    id: uuid.UUID
