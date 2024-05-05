from typing import Any

from together.types.chat_completions import MessageRole

from app.models.interpretation import InterpretationSubject

llm_model = "meta-llama/Llama-2-70b-chat-hf"
prompt_1 = [
    {
        "role": MessageRole.USER,
        "content": "Представь себе, что ты умеешь предсказывать судьбу по картам Таро.",
    },
    {
        "role": MessageRole.USER,
        "content": "Я буду называть тебе карты и тему, а ты будешь давать интерпретацию",
    },
    {
        "role": MessageRole.USER,
        "content": "Не нужно использовать приветственные слова. Начинай текст с интерпретации.",
    },
    {
        "role": MessageRole.USER,
        "content": "Запрещено описывать каждую карту отдельно. Оставь только вывод.",
    },
    {
        "role": MessageRole.USER,
        "content": "Начинай текст со слова - Интерпретация:",
    },
    {
        "role": MessageRole.USER,
        "content": "Пиши только на русском языке.",
    },
    {
        "role": MessageRole.USER,
        "content": "Карты - Всадник, Клевер и Звезды. Тема - карьера.",
    },
]


def get_prompt(cards: str, subject: InterpretationSubject) -> list[dict[str, Any]]:
    content = """
    Ты сервис по интерпретации карт Таро
    Я буду называть тебе карты и тему, а ты будешь давать интерпретацию
    Не нужно использовать приветственные слова. Начинай текст с интерпретации.
    Запрещено описывать каждую карту отдельно. Оставь только вывод.
    Начинай текст со слова Интерпретация:.
    Пиши только на русском языке.

    Карты - {}. Тема - {}.
    """  # noqa: W293

    prompt = {"role": MessageRole.USER, "content": content.format(cards, subject)}

    return [prompt]
