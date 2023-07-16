from sqlalchemy import Double, ForeignKey, String, func
from sqlalchemy.dialects.mysql import DATETIME, TINYINT
from sqlalchemy.orm import Mapped, as_declarative, mapped_column, relationship


@as_declarative()
class Base:
    __name__: str
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class BaseWithDates(Base):
    created_at = mapped_column(DATETIME, default=func.now())
    updated_at = mapped_column(DATETIME, onupdate=func.now())


class Users(BaseWithDates):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(unique=True, comment="Telegram id")
    username: Mapped[str] = mapped_column(String(100), comment="Telegram login")
    phone: Mapped[str] = mapped_column(String(100), nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_banned: Mapped[bool] = mapped_column(default=False)

    wallet = relationship("Wallets", back_populates="user")


class UserSettings(BaseWithDates):
    __tablename__ = "user_settings"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    language: Mapped[str] = mapped_column(String(2), default="RU")
    local_currency: Mapped[str] = mapped_column(String(3), default="USD")

    user = relationship("Users", foreign_keys=[user_id])


class Wallets(BaseWithDates):
    __tablename__ = "wallets"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    amount: Mapped[Double]
    address: Mapped[str] = mapped_column(String(50))

    user = relationship("Users", back_populates="wallet")


class Currency(Base):
    __tablename__ = "currency"

    name: Mapped[str] = mapped_column(String(50))


class Withdraw(BaseWithDates):
    __tablename__ = "withdraw"

    amount: Mapped[Double]
    currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    address_to: Mapped[str] = mapped_column(String(50))
    aml: Mapped[str] = mapped_column(String(10))
    txid: Mapped[str] = mapped_column(String(100), comment="hash")
    state: Mapped[TINYINT]
    gate: Mapped[str] = mapped_column(String(50), index=True)
    refund: Mapped[bool]
    # ??? Not sure what these fields are about ???
    # chat_id: Mapped[Double]
    # message_id: Mapped[Double]
    # chat_name: Mapped[str] = mapped_column(String(100))

    currency = relationship("Currency", foreign_keys=[currency_id])
    wallet = relationship("Wallets", foreign_keys=[wallet_id])


class Deposit(BaseWithDates):
    __tablename__ = "deposit"

    amount: Mapped[Double]
    currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    address_from: Mapped[str] = mapped_column(String(50))
    aml: Mapped[str] = mapped_column(String(10))
    txid: Mapped[str] = mapped_column(String(100), comment="hash")
    state: Mapped[TINYINT]
    sign: Mapped[str] = mapped_column(String(50))

    currency = relationship("Currency", foreign_keys=[currency_id])
    wallet = relationship("Wallets", foreign_keys=[wallet_id])


class Commission(BaseWithDates):
    __tablename__ = "commission"

    amount: Mapped[Double]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    active: Mapped[bool] = mapped_column(default=True)

    user = relationship("Users", foreign_keys=[user_id])
    currency = relationship("Currency", foreign_keys=[currency_id])


class Exchange(BaseWithDates):
    __tablename__ = "exchange"

    amount: Mapped[Double]
    rate: Mapped[Double]
    wallet_id_from: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    wallet_id_to: Mapped[int] = mapped_column(ForeignKey("wallets.id"))

    wallet = relationship("Wallets", foreign_keys=[wallet_id_from, wallet_id_to])


class Comments(BaseWithDates):
    __tablename__ = "comments"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    comment: Mapped[str] = mapped_column(String(250))

    user = relationship("Users", foreign_keys=[user_id])


# ??? Not sure what this table is about ???
class Transactions(BaseWithDates):
    __tablename__ = "transactions"
