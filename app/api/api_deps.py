import uuid
from typing import Annotated

from fastapi import Header


def x_user_id(
    x_user_id: Annotated[uuid.UUID, Header()],
) -> uuid.UUID:
    return x_user_id


def x_correlation_id(
    x_correlation_id: Annotated[uuid.UUID, Header()],
) -> uuid.UUID:
    return x_correlation_id
