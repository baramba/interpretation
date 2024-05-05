from together import AsyncTogether

from app.core.config import settings
from app.depends.adapters.llm import LLMClient, TogetherLLMClient

together_client = AsyncTogether(api_key=settings.app.TOGETHER_API_KEY)


def get_llm_client() -> LLMClient:
    return TogetherLLMClient(together_client=together_client)
