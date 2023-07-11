from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.classes.common import NavigationCallback
from bot.consts.phrases import BUTTONS


def start_markup():
    builder = InlineKeyboardBuilder()
    builder.button(text=BUTTONS['menu'], callback_data=NavigationCallback(where='menu'))
    return builder.as_markup(resize_keyboard=True)


def main_menu_markup():
    builder = InlineKeyboardBuilder()
    for target in ['my_wallet', 'support', 'settings']:
        builder.button(
            text=BUTTONS[target], callback_data=NavigationCallback(where=target)
        )
    return builder.adjust(2, 1).as_markup(resize_keyboard=True)


def back_to_main_menu_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=BUTTONS['back_to_main_menu'],
        callback_data=NavigationCallback(where='menu'),
    )
    return builder.as_markup(resize_keyboard=True)


def undeveloped_menu_markup():
    builder = InlineKeyboardBuilder()
    builder.button(text=BUTTONS['back'], callback_data=NavigationCallback(where='menu'))
    return builder.adjust(2, 2).as_markup(resize_keyboard=True)


def my_wallet_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=BUTTONS['deposit'],
        callback_data=NavigationCallback(where='deposit'),
    )
    builder.button(
        text=BUTTONS['withdraw'],
        callback_data=NavigationCallback(where='withdraw'),
    )
    builder.button(text=BUTTONS['back'], callback_data=NavigationCallback(where='menu'))
    return builder.adjust(2, 2).as_markup(resize_keyboard=True)


# DEPOSIT
def deposit_currency_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=BUTTONS['BTC'],
        callback_data=NavigationCallback(where='deposit_BTC'),
    )
    builder.button(
        text=BUTTONS['back'], callback_data=NavigationCallback(where='my_wallet')
    )
    return builder.as_markup(resize_keyboard=True)


# WITHDRAW
def withdraw_currency_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=BUTTONS['BTC'],
        callback_data=NavigationCallback(where='withdraw_BTC'),
    )
    builder.button(
        text=BUTTONS['back'], callback_data=NavigationCallback(where='my_wallet')
    )
    return builder.as_markup(resize_keyboard=True)


def withdraw_step_back_markup(where):
    builder = InlineKeyboardBuilder()
    builder.button(text=BUTTONS['back'], callback_data=NavigationCallback(where=where))
    return builder.as_markup(resize_keyboard=True)


def withdraw_confirmation_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=BUTTONS['yes_confirm'],
        callback_data=NavigationCallback(where='withdraw_proceed'),
    )
    builder.button(
        text=BUTTONS['back'],
        callback_data=NavigationCallback(where='withdraw_amount'),
    )
    return builder.as_markup(resize_keyboard=True)
