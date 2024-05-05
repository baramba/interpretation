from abc import ABC, abstractmethod
from collections.abc import Sequence

from together import AsyncTogether

from app.core.config import app_logger
from app.models.card import Card
from app.models.interpretation import InterpretationSubject
from app.services.predictions.prompts import get_prompt, llm_model


class LLMClient(ABC):
    @abstractmethod
    async def interpret(self, cards: Sequence[Card], subject: InterpretationSubject) -> str:
        ...


class TogetherLLMClient(LLMClient):
    def __init__(self, together_client: AsyncTogether) -> None:
        super().__init__()
        self.together_client = together_client

    async def interpret(self, cards: Sequence[Card], subject: InterpretationSubject) -> str:
        card_names = ",".join(card.name for card in cards)
        prompt = get_prompt(card_names, subject=subject)
        app_logger.info(f"{prompt=}")
        response = await self.together_client.chat.completions.create(messages=prompt, model=llm_model)
        text = response.choices[0].message.content

        return str(text)
