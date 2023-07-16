from sqlalchemy import ForeignKey, String, func
from sqlalchemy.dialects.mysql import DATETIME, DOUBLE
from sqlalchemy.orm import Mapped, as_declarative, mapped_column, relationship


@as_declarative()
class Base:
    __name__: str
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class Dates:
    created_at = mapped_column(DATETIME, default=func.now())
    updated_at = mapped_column(DATETIME, onupdate=func.now())


class Users(Base, Dates):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(unique=True, comment="Telegram id")
    username: Mapped[str] = mapped_column(String(100), comment="Telegram login")
    phone: Mapped[str] = mapped_column(String(100), nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_banned: Mapped[bool] = mapped_column(default=False)

    wallet = relationship("Wallets", back_populates="user")


class UserSettings(Base, Dates):
    __tablename__ = "user_settings"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    language: Mapped[str] = mapped_column(String(2), default="RU")
    local_currency: Mapped[str] = mapped_column(String(3), default="RUB")

    user = relationship("Users", foreign_keys=[user_id])


class Wallets(Base, Dates):
    __tablename__ = "wallets"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    amount = mapped_column(DOUBLE, nullable=False, default=0.00)
    frozen_amount = mapped_column(DOUBLE, nullable=False, default=0.00)
    address: Mapped[str] = mapped_column(String(50))

    user = relationship("Users", back_populates="wallet")


class Currency(Base):
    __tablename__ = "currency"

    name: Mapped[str] = mapped_column(String(50))


class Withdraw(Base, Dates):
    __tablename__ = "withdraw"

    amount = mapped_column(DOUBLE, nullable=False)
    currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    address_to: Mapped[str] = mapped_column(String(50))
    aml: Mapped[str] = mapped_column(String(10))
    txid: Mapped[str] = mapped_column(String(100), comment="hash")
    state: Mapped[bool]
    gate: Mapped[str] = mapped_column(String(50), index=True)
    refund: Mapped[bool]
    chat_id: Mapped[float]
    message_id: Mapped[float]
    chat_name: Mapped[str] = mapped_column(String(100))
    confirmation: Mapped[int]
    sign: Mapped[str] = mapped_column(String(50))

    currency = relationship("Currency", foreign_keys=[currency_id])
    wallet = relationship("Wallets", foreign_keys=[wallet_id])


class Deposit(Base, Dates):
    __tablename__ = "deposit"

    amount = mapped_column(DOUBLE, nullable=False)
    currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    address_from: Mapped[str] = mapped_column(String(50))
    aml: Mapped[str] = mapped_column(String(10))
    txid: Mapped[str] = mapped_column(String(100), comment="hash")
    state: Mapped[bool]
    sign: Mapped[str] = mapped_column(String(50))

    currency = relationship("Currency", foreign_keys=[currency_id])
    wallet = relationship("Wallets", foreign_keys=[wallet_id])


class Commission(Base, Dates):
    __tablename__ = "commission"

    amount = mapped_column(DOUBLE, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    active: Mapped[bool] = mapped_column(default=True)

    user = relationship("Users", foreign_keys=[user_id])
    currency = relationship("Currency", foreign_keys=[currency_id])


class Exchange(Base, Dates):
    __tablename__ = "exchange"

    amount = mapped_column(DOUBLE, nullable=False)
    rate = mapped_column(DOUBLE, nullable=False)
    wallet_id_from: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    wallet_id_to: Mapped[int] = mapped_column(ForeignKey("wallets.id"))

    wallet = relationship("Wallets", foreign_keys=[wallet_id_from, wallet_id_to])


class Comments(Base, Dates):
    __tablename__ = "comments"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    comment: Mapped[str] = mapped_column(String(250))

    user = relationship("Users", foreign_keys=[user_id])
