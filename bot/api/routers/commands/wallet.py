from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from bot.common import constants
from bot.services.markups import wallet
from bot.services.wallet import wallet_service

router = Router(name="wallet-command-router")


@router.message(Command('my_wallet'))
async def my_wallet_cmd(message: Message, session: AsyncSession):
    my_wallet_data = await wallet_service.get_wallet_data(
        user_tg_id=message.from_user.id, db_session=session
    )
    await message.answer(
        constants.MAIN_MENU['my_wallet'].format(**my_wallet_data),
        reply_markup=wallet.my_wallet_markup(),
    )
