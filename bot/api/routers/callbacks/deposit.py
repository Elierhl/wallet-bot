from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.common import constants
from bot.common.callbacks import NavigationCallback
from bot.markups import deposit, menu
from bot.services.external.cryptocurrency import cryptocurrency_service

router = Router(name="deposit-callback-router")


@router.callback_query(NavigationCallback.filter(F.where == 'deposit'))
async def deposit_choose_currency_handler(query: CallbackQuery):
    await query.message.edit_text(
        constants.DEPOSIT['currency'],
        reply_markup=deposit.deposit_currency_markup(),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'deposit_BTC'))
async def deposit_proceeding_handler(
    query: CallbackQuery, callback_data: NavigationCallback
):
    currency = callback_data.where.split('_')[1]
    address = await cryptocurrency_service.give_address(
        tg_id=query.from_user.id,
        currency=currency,
    )
    await query.message.edit_text(
        constants.DEPOSIT['address'].format(
            currency=currency,
            network=constants.NETWORKS[currency],
            address=address,
        ),
        reply_markup=menu.back_to_main_menu_markup(),
    )
