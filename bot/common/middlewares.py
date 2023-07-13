# import logging
# from typing import Any, Awaitable, Callable, Dict, Union
#
# from aiogram import BaseMiddleware
# from aiogram.types import CallbackQuery, Message, TelegramObject
# from sqlalchemy import select
#
# from bot.db.models import *
#
# logger = logging.getLogger(__name__)
#
#
# class HashValidatorMiddleware(BaseMiddleware):
#     async def __call__(
#         self,
#         handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#         event: Union[Message, CallbackQuery],
#         data: Dict[str, Any],
#     ) -> Any:
#         tg_id = data['event_from_user'].id
#         stmt = select(User.username).where(User.tg_id == tg_id)
#         saved_hash = (await data['session'].execute(stmt)).scalar()
#
#         if data['callback_data'].hash_ == saved_hash:
#             result = await handler(event, data)
#             return result
#         else:
#             await event.answer('Outdated button')
