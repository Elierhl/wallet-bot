from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot import markups
from bot.phrases import main_menu

router = Router(name="commands-router")


@router.message(Command('start'))
async def start_cmd(message: Message, state: FSMContext):
    await message.answer(main_menu['start'], reply_markup=markups.start_markup())
    await state.clear()


@router.message(Command('menu'))
async def menu_cmd(message: Message, state: FSMContext):
    await message.answer(main_menu['menu'], reply_markup=markups.main_menu_markup())
    await state.clear()


@router.message(Command('my_wallet'))
async def my_wallet_cmd(message: Message, state: FSMContext):
    await message.answer(
        main_menu['my_wallet'], reply_markup=markups.my_wallet_markup()
    )
    await state.clear()
