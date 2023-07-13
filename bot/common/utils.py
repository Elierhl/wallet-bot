from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

from bot.common.constants import UI_COMMANDS


async def set_ui_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description=UI_COMMANDS['start']),
        BotCommand(command="menu", description=UI_COMMANDS['menu']),
        BotCommand(command="my_wallet", description=UI_COMMANDS['my_wallet']),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
