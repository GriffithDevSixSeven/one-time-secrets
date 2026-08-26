from core.config import db_setting

from typing import Annotated,AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends

engine = create_async_engine(db_setting.DB_URL)

session_factory = async_sessionmaker(engine,expire_on_commit=False)

async def get_session() -> AsyncGenerator:
    async with session_factory() as session:
        yield session


SessionDep = Annotated[AsyncSession,Depends(get_session)]

class Base(DeclarativeBase):
    pass