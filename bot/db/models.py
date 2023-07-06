from sqlalchemy import Column, Integer, String

from bot.db.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    lang = Column(String)
