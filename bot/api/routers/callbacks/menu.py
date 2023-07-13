from aiogram import F, Router
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from bot.common import constants
from bot.common.callbacks import NavigationCallback
from bot.markups import menu
from bot.services.menu import menu_controller

router = Router(name="menu-callback-router")


@router.callback_query(NavigationCallback.filter(F.where == 'menu'))
async def menu_handler(query: CallbackQuery):
    await query.message.edit_text(
        constants.MAIN_MENU['menu'], reply_markup=menu.main_menu_markup()
    )


@router.callback_query(NavigationCallback.filter(F.where.in_(['support', 'settings'])))
async def menu_generator_handler(
    query: CallbackQuery, callback_data: NavigationCallback
):
    await query.message.edit_text(
        constants.MAIN_MENU[callback_data.where],
        reply_markup=menu.undeveloped_menu_markup(),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'my_wallet'))
async def my_wallet_handler(query: CallbackQuery, session: AsyncSession):
    my_wallet_data = await menu_controller.get_wallet_data(
        tg_id=query.from_user.id, db_session=session
    )
    await query.message.edit_text(
        constants.MAIN_MENU['my_wallet'].format(**my_wallet_data),
        reply_markup=menu.my_wallet_markup(),
    )
