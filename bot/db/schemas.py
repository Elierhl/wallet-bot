from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(String(30))
    phone: Mapped[Optional[str]] = mapped_column(String(30))

    balances: Mapped['UserBalance'] = relationship()


class UserBalance(Base):
    __tablename__ = "user_balances"

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    btc: Mapped[float] = mapped_column(default=0)
    usdt: Mapped[float] = mapped_column(default=0)

    user: Mapped['User'] = relationship()


# class MarkupHash(Base):
#     __tablename__ = "markup_hashes"
#
#     tg_id: Mapped[int] = mapped_column(primary_key=True)
#     hash: Mapped[str]


# class ApiKey(Base):
#     __tablename__ = "api_keys"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#     key: Mapped[str]
#
#     user: Mapped['User'] = relationship(back_populates='api_key')
