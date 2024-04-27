import uuid
from contextvars import ContextVar

user_id: ContextVar[str | None] = ContextVar("user_id", default="")
correlation_id: ContextVar[str | None] = ContextVar("correlation_id", default="")


class AppContext:
    @staticmethod
    def user_id() -> uuid.UUID:
        user_id_ = user_id.get()
        if user_id_:
            return uuid.UUID(user_id_)
        raise ValueError("User id is not defined")

    @staticmethod
    def correlation_id() -> uuid.UUID:
        correlation_id_ = correlation_id.get()
        if correlation_id_ is not None:
            return uuid.UUID(correlation_id_)
        raise ValueError("User id is not defined")
