from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import texts
from bot.common import NavigationCallback


def start_markup():
    builder = InlineKeyboardBuilder()
    builder.button(text=texts.buttons['menu'], callback_data=NavigationCallback(to='menu'))
    return builder.as_markup(resize_keyboard=True)


def menu_markup():
    builder = InlineKeyboardBuilder()
    for target in ['my_wallet', 'market', 'support', 'settings']:
        builder.button(text=texts.buttons[target], callback_data=NavigationCallback(to=target))
    return builder.adjust(2).as_markup(resize_keyboard=True)
