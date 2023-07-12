from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from bot.common import constants
from bot.services.markups import menu
from bot.services.user import user_service

router = Router(name="start-command-router")


@router.message(Command('start'))
async def start_cmd(message: Message, state: FSMContext, session: AsyncSession):
    await user_service.initiate_user(message, session)
    await message.answer(constants.MAIN_MENU['start'], reply_markup=menu.start_markup())
    await state.clear()
