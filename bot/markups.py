from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.custom.common import NavigationCallback
from bot.phrases import buttons


def start_markup():
    builder = InlineKeyboardBuilder()
    builder.button(text=buttons['menu'], callback_data=NavigationCallback(where='menu'))
    return builder.as_markup(resize_keyboard=True)


def main_menu_markup():
    builder = InlineKeyboardBuilder()
    for target in ['my_wallet', 'market', 'support', 'settings']:
        builder.button(
            text=buttons[target], callback_data=NavigationCallback(where=target)
        )
    return builder.adjust(2).as_markup(resize_keyboard=True)


def undeveloped_menu_markup():
    builder = InlineKeyboardBuilder()
    builder.button(text=buttons['back'], callback_data=NavigationCallback(where='menu'))
    return builder.adjust(2, 2).as_markup(resize_keyboard=True)


def my_wallet_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=buttons['withdraw'],
        callback_data=NavigationCallback(where='withdraw'),
    )
    builder.button(text=buttons['back'], callback_data=NavigationCallback(where='menu'))
    return builder.adjust(2, 2).as_markup(resize_keyboard=True)


def withdraw_currency_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=buttons['BTC'],
        callback_data=NavigationCallback(where='withdraw_BTC'),
    )
    builder.button(
        text=buttons['back'], callback_data=NavigationCallback(where='my_wallet')
    )
    return builder.as_markup(resize_keyboard=True)


def withdraw_step_back_markup(where):
    builder = InlineKeyboardBuilder()
    builder.button(text=buttons['back'], callback_data=NavigationCallback(where=where))
    return builder.as_markup(resize_keyboard=True)


def withdraw_confirmation_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=buttons['yes_confirm'],
        callback_data=NavigationCallback(where='withdraw_proceed'),
    )
    builder.button(
        text=buttons['back'],
        callback_data=NavigationCallback(where='withdraw_amount'),
    )
    return builder.as_markup(resize_keyboard=True)
