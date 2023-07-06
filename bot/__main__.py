import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from bot.config_reader import config
from bot.handlers import callbacks, commands
from bot.middlewares import DbSessionMiddleware
from bot.ui_commands import set_ui_commands


async def main():
    logging.basicConfig(level=logging.INFO)

    engine = create_async_engine(url=config.db_url.get_secret_value(), echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    # Automatically reply to all callbacks
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    # Register handlers
    dp.include_router(commands.router)
    dp.include_router(callbacks.router)

    # Set bot commands in UI
    await set_ui_commands(bot)

    logging.info("Bot started.")

    # Run bot
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
