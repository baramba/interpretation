import uuid
from collections.abc import Sequence

from fastapi import Depends
from pydantic import TypeAdapter
from sqlalchemy import func
from sqlmodel import select

from app.depends.adapters.llm import LLMClient
from app.depends.db import SessionMaker, get_db_session
from app.depends.llm_client import get_llm_client
from app.models.card import Card, CardPublic
from app.models.interpretation import InterpretationPublic, InterpretationSubject


class InterpretationService:
    def __init__(self, session_maker: SessionMaker, llm_client: LLMClient):
        self.session_maker = session_maker
        self.llm_client = llm_client

    async def get_interpretation_one(self, user_id: uuid.UUID, subject: InterpretationSubject) -> InterpretationPublic:
        cards = await self.random_combination()
        text = await self.llm_client.interpret(cards=cards, subject=subject)
        ta = TypeAdapter(tuple[CardPublic])
        return InterpretationPublic(cards=ta.validate_python(cards), text=text)

    async def random_combination(self, size: int = 1) -> Sequence[Card]:
        stmt = select(Card).order_by(func.random()).limit(size)
        async with self.session_maker() as session:
            cards = (await session.scalars(stmt)).all()
        return cards


def get_interpretation_service(
    session_maker: SessionMaker = Depends(get_db_session),
    llm_client: LLMClient = Depends(get_llm_client),
) -> InterpretationService:
    return InterpretationService(session_maker=session_maker, llm_client=llm_client)
