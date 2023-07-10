import logging
from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from bot.db.models import *


class DbSessionMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker):
        super().__init__()
        self.session_pool = session_pool

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        async with self.session_pool() as session:
            data["session"] = session
            return await handler(event, data)


class HashValidatorMiddleware(BaseMiddleware):
    def __init__(self):
        self.session = AsyncSession()

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:
        if isinstance(event, Message):
            tg_id = event.from_user.id
        else:  # CallbackQuery
            tg_id = event.message.from_user.id

        stmt = select(MarkupHash.hash).where(MarkupHash.tg_id == tg_id)
        saved_hash = (await self.session.execute(stmt)).scalar()
        logging.info(f'!! data = {data}')
        if data['hashed'] == saved_hash:
            result = await handler(event, data)
            return result
        else:
            logging.error(f'!! received_hash = {data["hashed"]}')
