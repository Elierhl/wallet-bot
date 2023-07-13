import re

from aiogram.types import CallbackQuery, Message

from bot.common import constants, states
from bot.services.external.cryptocurrency import cryptocurrency_service


class WithdrawController:
    async def provide_address(self, callback_data, state):
        await state.update_data(currency=callback_data.where.split('_')[1])
        await state.set_state(states.Withdraw.address)

    async def provide_amount(self, message, state):
        if isinstance(message, Message):
            if re.fullmatch(r'\w{34}', message.text) and isinstance(message, Message):
                await state.update_data(address=message.text)
                await state.set_state(states.Withdraw.amount)
                return 'withdraw_BTC'
            else:
                return 'withdraw'
        elif isinstance(message, CallbackQuery):
            return 'withdraw_BTC'

    async def get_confirmation(self, message, state):
        if re.fullmatch(r'\d*\.?\d+', message.text):
            await state.update_data(amount=message.text)
            return await state.get_data()

    async def proceed_withdrawal(self, state):
        user_data = await state.get_data()
        response = await cryptocurrency_service.send_crypto(
            amount=user_data['amount'],
            currency=user_data['currency'],
            address=user_data['address'],
        )
        text = (
            constants.WITHDRAW['success'] if response else constants.WITHDRAW['failed']
        )
        return text


withdraw_controller = WithdrawController()
