from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings 


engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session_maker = sessionmaker(bind=engine, 
                            class_=AsyncSession,
                            expire_on_commit=False # don't refresh on next commit
                            )


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
