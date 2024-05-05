import datetime as dt
import uuid

import sqlalchemy as sa
from sqlmodel import Field, SQLModel, text


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.UTC)


class IdMixin(SQLModel):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        nullable=True,
        sa_column_kwargs={"server_default": sa.func.gen_random_uuid()},
    )


class DatetimeMixin(SQLModel):
    created: dt.datetime | None = Field(
        default_factory=utc_now,
        sa_column_kwargs={
            "server_default": text("TIMEZONE('utc', now())"),
        },
        nullable=False,
    )
    updated: dt.datetime | None = Field(
        default_factory=utc_now,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("TIMEZONE('utc', now())"),
            "onupdate": utc_now,
        },
    )
