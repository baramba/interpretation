import uuid

from fastapi import Depends
from sqlmodel import Session

from app.depends.db import get_db_session


class UserService:
    def __init__(self, session: Session):
        self.session = session

    async def gen_user_id(self) -> uuid.UUID:
        return uuid.uuid4()


def get_user_service(
    session: Session = Depends(get_db_session),
) -> UserService:
    return UserService(session=session)
