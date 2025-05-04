from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

"""
Создание движка для SQLite
"""
engine = create_async_engine("sqlite+aiosqlite:///./blog.db",)

"""
Создание фабрики сессий для работы с БД
"""
AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False
)

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session