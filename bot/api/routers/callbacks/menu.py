from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from bot.common import constants
from bot.common.callbacks import NavigationCallback, PagesCallback
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
async def my_wallet_handler(query: CallbackQuery):
    my_wallet_data = await menu_controller.get_wallet_data(tg_id=query.from_user.id)
    await query.message.edit_text(
        constants.MAIN_MENU['my_wallet'].format(**my_wallet_data),
        reply_markup=menu.my_wallet_markup(),
    )


@router.callback_query(PagesCallback.filter())
async def my_transactions_handler(query: CallbackQuery, callback_data: PagesCallback):
    transactions_text, total_pages = await menu_controller.get_transactions_list(
        tg_id=query.from_user.id,
        callback_data=callback_data,
    )
    try:
        await query.message.edit_text(
            transactions_text,
            reply_markup=menu.my_transactions_markup(total_pages),
        )
    except TelegramBadRequest:
        await query.answer()
