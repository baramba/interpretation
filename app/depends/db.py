from collections.abc import AsyncGenerator
from typing import Any

from sqlmodel import Session, create_engine

sqlite_file_name = "database.db"
sqlite_url = "sqlite:///"

# engine = create_engine(settings.db.DATABASE_URI)
engine = create_engine(sqlite_url, echo=True)


async def get_db_session() -> AsyncGenerator[Session, Any]:
    with Session(engine) as session:
        yield session
