from core.config import db_settings

from typing import Annotated,AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from fastapi import Depends

engine = create_async_engine(db_settings.DB_URL)

session_factory = async_sessionmaker(engine,expire_on_commit=False)

async def get_session() -> AsyncGenerator:
    async with session_factory() as session:
        yield session


SessionDep = Annotated[AsyncSession,Depends(get_session)]

