import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Field, SQLModel


class ModelBaseMixin(SQLModel):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        nullable=True,
        sa_column_kwargs={"server_default": sa.func.gen_random_uuid()},
    )
    created: datetime | None = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated: datetime | None = Field(
        default_factory=datetime.now,
        nullable=False,
        sa_column_kwargs={
            "server_default": sa.func.now(),
            "onupdate": datetime.now(),
        },
    )
