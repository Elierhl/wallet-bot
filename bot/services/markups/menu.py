from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.common import constants
from bot.common.callbacks import NavigationCallback


def start_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=constants.BUTTONS['menu'], callback_data=NavigationCallback(where='menu')
    )
    return builder.as_markup(resize_keyboard=True)


def main_menu_markup():
    builder = InlineKeyboardBuilder()
    for target in ['my_wallet', 'support', 'settings']:
        builder.button(
            text=constants.BUTTONS[target],
            callback_data=NavigationCallback(where=target),
        )
    return builder.adjust(2, 1).as_markup(resize_keyboard=True)


def back_to_main_menu_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=constants.BUTTONS['back_to_main_menu'],
        callback_data=NavigationCallback(where='menu'),
    )
    return builder.as_markup(resize_keyboard=True)


def undeveloped_menu_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=constants.BUTTONS['back'], callback_data=NavigationCallback(where='menu')
    )
    return builder.adjust(2, 2).as_markup(resize_keyboard=True)
