from fastapi import Depends
from sqlmodel import Session

from app.depends.db import get_db_session


class PredictionService:
    def __init__(self, session: Session):
        self.session = session

    async def get_prediction(self, combination: str) -> str:
        return f"session_id - {self.session.hash_key}, combination - {combination}"


def get_prediction_service(
    session: Session = Depends(get_db_session),
) -> PredictionService:
    return PredictionService(session=session)
