from typing import List, Optional

from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int]
    username: Mapped[str]

    # api_key: Mapped['ApiKey'] = relationship(back_populates='user')


class MarkupHash(Base):
    __tablename__ = "markup_hashes"

    tg_id: Mapped[int] = mapped_column(primary_key=True)
    hash: Mapped[str]


# class ApiKey(Base):
#     __tablename__ = "api_keys"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#     key: Mapped[str]
#
#     user: Mapped['User'] = relationship(back_populates='api_key')
