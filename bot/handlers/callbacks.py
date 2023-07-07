from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot import markups, texts
from bot.common import NavigationCallback

router = Router(name="callbacks-router")


@router.callback_query(NavigationCallback.filter(F.to == 'menu'))
async def menu_handler(query: CallbackQuery):
    await query.message.edit_text(texts.main_menu['menu'], reply_markup=markups.menu_markup())


@router.callback_query(NavigationCallback.filter())
async def my_wallet_handler(query: CallbackQuery):
    print(query)
    await query.message.edit_text(texts.main_menu[F.to], reply_markup=markups.menu_markup())
