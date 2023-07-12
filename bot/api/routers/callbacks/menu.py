from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.common import constants
from bot.common.callbacks import NavigationCallback
from bot.services.markups import menu

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
