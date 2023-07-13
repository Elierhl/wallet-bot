from bot.common import constants
from bot.common.config import settings
from bot.services.external.utils import AsyncRequest


class CryptocurrencyService(AsyncRequest):
    def __init__(self):
        super().__init__(module_name=__name__)

    async def send_crypto(self, amount, currency, address):
        address = '1Hpv9WVt1FgW4WYHQSk3ridsJhEWbgob8C'  # tmp
        async with self.session_pool() as session:
            params = {
                'amount': amount,
                'to': address,
            }
            async with session.post(
                constants.CC_SEND_CRYPTO.format(currency=currency.lower()),
                params=params,
                headers={'CCAPI-KEY': settings.CRYPTOCURRENCY_TOKEN},
            ) as response:
                response = await self.response_processing(response)
                return response['result']

    async def give_address(self, tg_id, currency):
        async with self.session_pool() as session:
            params = {'label': tg_id}
            async with session.post(
                constants.CC_GIVE_ADDRESS.format(currency=currency.lower()),
                params=params,
                headers={'CCAPI-KEY': settings.CRYPTOCURRENCY_TOKEN},
            ) as response:
                response = await self.response_processing(response)
                return response['result']['address']


cryptocurrency_service = CryptocurrencyService()
