from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.common import constants
from bot.markups import menu
from bot.services.menu import menu_controller

router = Router(name="commands-router")


@router.message(Command('start'))
async def start_cmd(message: Message, state: FSMContext):
    await menu_controller.initiate_user(message)
    await message.answer(constants.MAIN_MENU['start'], reply_markup=menu.start_markup())
    await state.clear()


@router.message(Command('menu'))
async def menu_cmd(message: Message, state: FSMContext):
    await message.answer(
        constants.MAIN_MENU['menu'], reply_markup=menu.main_menu_markup()
    )
    await state.clear()


@router.message(Command('my_wallet'))
async def my_wallet_cmd(message: Message):
    my_wallet_data = await menu_controller.get_wallet_data(tg_id=message.from_user.id)
    await message.answer(
        constants.MAIN_MENU['my_wallet'].format(**my_wallet_data),
        reply_markup=menu.my_wallet_markup(),
    )
