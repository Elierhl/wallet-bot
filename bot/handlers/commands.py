from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot import markups, texts
from bot.common import NavigationCallback

router = Router(name="commands-router")


@router.message(Command('start'))
async def start_cmd(message: Message):
    await message.answer(texts.main_menu['start'], reply_markup=markups.start_markup())


@router.message(Command('menu'))
async def menu_cmd(message: Message):
    await message.answer(texts.main_menu['menu'], reply_markup=markups.menu_markup())
