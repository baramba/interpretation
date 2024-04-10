from logging import Filter, LogRecord


class ExtraParamsFilter(Filter):
    """Фильтр, который расширяет контекст логгера"""

    def __init__(self, name: str = ""):
        super().__init__(name=name)

    def filter(self, record: LogRecord) -> bool:
        # Пример использования
        # setattr(record, "app.extra_params", app_context.get())
        return True
