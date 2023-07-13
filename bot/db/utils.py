from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from bot.common.config import settings
from bot.common.logger import Logger


class Database:
    engine = create_async_engine(url=settings.DB_URL, echo=True)
    session_pool = async_sessionmaker(engine, expire_on_commit=False)

    def __init__(self, module_name):
        self.logger = Logger(module_name).get_logger()
