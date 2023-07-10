from aiogram.fsm.state import State, StatesGroup


class Withdraw(StatesGroup):
    currency = State()
    address = State()
    amount = State()
