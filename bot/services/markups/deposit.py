from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.common.callbacks import NavigationCallback
from bot.common import constants


def deposit_currency_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=constants.BUTTONS['BTC'],
        callback_data=NavigationCallback(where='deposit_BTC'),
    )
    builder.button(
        text=constants.BUTTONS['back'], callback_data=NavigationCallback(where='my_wallet')
    )
    return builder.as_markup(resize_keyboard=True)
