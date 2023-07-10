from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

from bot.phrases import ui_commands


async def set_ui_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description=ui_commands['start']),
        BotCommand(command="menu", description=ui_commands['menu']),
        BotCommand(command="my_wallet", description=ui_commands['my_wallet']),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
