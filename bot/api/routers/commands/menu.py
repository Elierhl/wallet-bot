from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.services.markups import menu
from bot.common import constants

router = Router(name="menu-command-router")


@router.message(Command('menu'))
async def menu_cmd(message: Message, state: FSMContext):
    await message.answer(constants.MAIN_MENU['menu'], reply_markup=menu.main_menu_markup())
    await state.clear()
