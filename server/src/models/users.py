from typing import List, Optional
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import  Mapped, mapped_column, relationship,DeclarativeBase


class Base(DeclarativeBase):
    pass



class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    secrets: Mapped[List["Secrets"]] = relationship(back_populates="author", cascade="all, delete-orphan")


class Secrets(Base):
    __tablename__ = "secrets"
    id: Mapped[int] = mapped_column(primary_key=True)
    encrypted_text: Mapped[str] = mapped_column(Text)
    secret_key: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    author: Mapped[Optional["Users"]] = relationship(back_populates="secrets")
