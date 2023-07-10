from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot import markups
from bot.phrases import MAIN_MENU

router = Router(name="commands-router")


@router.message(Command('start'))
async def start_cmd(message: Message, state: FSMContext):
    await message.answer(MAIN_MENU['start'], reply_markup=markups.start_markup())
    await state.clear()


@router.message(Command('menu'))
async def menu_cmd(message: Message, state: FSMContext):
    await message.answer(MAIN_MENU['menu'], reply_markup=markups.main_menu_markup())
    await state.clear()


@router.message(Command('my_wallet'))
async def my_wallet_cmd(message: Message, state: FSMContext):
    await message.answer(
        MAIN_MENU['my_wallet'], reply_markup=markups.my_wallet_markup()
    )
    await state.clear()
