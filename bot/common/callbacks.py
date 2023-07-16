from aiogram.filters.callback_data import CallbackData


class NavigationCallback(CallbackData, prefix="navigation"):
    where: str


class PagesCallback(CallbackData, prefix="pages"):
    number: int
