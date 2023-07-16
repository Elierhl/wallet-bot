from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.common import constants
from bot.common.callbacks import NavigationCallback, PagesCallback


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
    builder.button(
        text=constants.BUTTONS['transactions'],
        callback_data=PagesCallback(number=1),
    )
    return builder.adjust(2, 2).as_markup(resize_keyboard=True)


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
    builder.button(
        text=constants.BUTTONS['back'], callback_data=NavigationCallback(where='menu')
    )
    return builder.adjust(2, 2).as_markup(resize_keyboard=True)


def my_transactions_markup(total_pages):
    builder = InlineKeyboardBuilder()
    for number in range(1, total_pages + 1):
        builder.button(text=str(number), callback_data=PagesCallback(number=number))
    builder.button(
        text=constants.BUTTONS['back'], callback_data=NavigationCallback(where='menu')
    )
    # TO DO: create dynamic adjust param for pages
    return builder.adjust(total_pages, 1).as_markup(resize_keyboard=True)
