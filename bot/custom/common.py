from aiogram.filters.callback_data import CallbackData


class NavigationCallback(CallbackData, prefix="navigation"):
    where: str


class HashedCallback(CallbackData, prefix='hashed'):
    hash_: str
