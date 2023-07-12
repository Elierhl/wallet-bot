from sqlalchemy.ext.asyncio import AsyncSession

from bot.common.callbacks import NavigationCallback
from aiogram.types import CallbackQuery
from aiogram import F, Router

from bot.common import constants
from bot.services.markups import wallet
from bot.services.wallet import wallet_service

router = Router(name="wallet-callback-router")


@router.callback_query(NavigationCallback.filter(F.where == 'my_wallet'))
async def my_wallet_handler(query: CallbackQuery, session: AsyncSession):
    my_wallet_data = await wallet_service.get_wallet_data(user_tg_id=query.from_user.id, db_session=session)
    await query.message.edit_text(
        constants.MAIN_MENU['my_wallet'].format(**my_wallet_data),
        reply_markup=wallet.my_wallet_markup(),
    )
