import asyncio

from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from bot.api import router
from bot.common.config import settings
from bot.common.logger import Logger
from bot.db.db import create_async_session
from bot.common.utils import set_ui_commands

LOGGER = Logger(__name__).get_logger()


async def main():
    bot = Bot(settings.BOT_TOKEN, parse_mode="HTML")

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()
    dp.update.middleware(create_async_session())
    # Automatically reply to all callbacks
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    # Register handlers
    dp.include_router(router)
    # Set bot commands in UI
    await set_ui_commands(bot)

    # Run bot
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    LOGGER.info("Bot started.")
    asyncio.run(main())
