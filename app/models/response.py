from pydantic import BaseModel


class AppResponse(BaseModel):
    code: int
    description: str
