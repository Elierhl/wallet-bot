from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.common.callbacks import NavigationCallback
from bot.common import constants


def my_wallet_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=constants.BUTTONS['deposit'],
        callback_data=NavigationCallback(where='deposit'),
    )
    builder.button(
        text=constants.BUTTONS['withdraw'],
        callback_data=NavigationCallback(where='withdraw'),
    )
    builder.button(text=constants.BUTTONS['back'], callback_data=NavigationCallback(where='menu'))
    return builder.adjust(2, 2).as_markup(resize_keyboard=True)
