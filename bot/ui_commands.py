from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

from bot import texts


async def set_ui_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description=texts.ui_commands['start']),
        BotCommand(command="menu", description=texts.ui_commands['menu']),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
