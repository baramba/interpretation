from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings

sqlite_file_name = "database.db"
sqlite_url = "sqlite:///"

# engine = create_engine(settings.db.DATABASE_URI)
# engine = create_engine(sqlite_url, echo=True)

engine = create_async_engine(
    settings.db.DATABASE_URI.unicode_string(),
    echo=True,
    future=True,
    pool_size=20,
    max_overflow=20,
    pool_recycle=3600,
)

SessionMaker = async_sessionmaker[AsyncSession]


async def get_db_session() -> SessionMaker:
    session_maker = async_sessionmaker(engine, class_=AsyncSession)
    return session_maker
