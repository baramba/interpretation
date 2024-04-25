from fastapi import Request
from starlette.types import ASGIApp, Receive, Scope, Send

from app.core.context import user_id


class CreateContextMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            request = Request(scope)
            user_id.set(request.headers.get("x-user-id"))
        await self.app(scope, receive, send)
