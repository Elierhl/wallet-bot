from aiogram.filters.callback_data import CallbackData


class NavigationCallback(CallbackData, prefix="navigation"):
    to: str
