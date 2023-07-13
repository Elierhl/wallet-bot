from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.common import constants
from bot.common.callbacks import NavigationCallback


def withdraw_currency_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=constants.BUTTONS['BTC'],
        callback_data=NavigationCallback(where='withdraw_BTC'),
    )
    builder.button(
        text=constants.BUTTONS['back'],
        callback_data=NavigationCallback(where='my_wallet'),
    )
    return builder.as_markup(resize_keyboard=True)


def withdraw_step_back_markup(where):
    builder = InlineKeyboardBuilder()
    builder.button(
        text=constants.BUTTONS['back'], callback_data=NavigationCallback(where=where)
    )
    return builder.as_markup(resize_keyboard=True)


def withdraw_confirmation_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=constants.BUTTONS['yes_confirm'],
        callback_data=NavigationCallback(where='withdraw_proceed'),
    )
    builder.button(
        text=constants.BUTTONS['back'],
        callback_data=NavigationCallback(where='withdraw_amount'),
    )
    return builder.as_markup(resize_keyboard=True)
