# Ursula Taro, Predictions Service

## Описать функциональность сервиса
Сервис позволяет получить предсказание по комбинации из одной или трех карт.

## Application
### Зависимости
Python 3.12, FastAPI, Pydantic

### Запуск локально
```shell
# Установка зависимостей
cd project_dir
poetry update

# Запуск
cd app
poetry run gunicorn main:app
```

### Docker compose
# Запуск
```shell
cd project_dir
docker compose up --build
```

### Документация REST API
* [swagger](http://127.0.0.1:8000/docs/swagger)
* [openapi](http://127.0.0.1:8000/docs/openapi)

## Разработка
```shell
# Установка зависимостей
cd project_dir
poetry update

# Настройка pre-commit hook'a
pre-commit install
```
