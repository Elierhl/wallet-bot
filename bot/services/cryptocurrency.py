from aiohttp import ClientSession

from bot.common import constants
from bot.common.config import settings
from bot.common.logger import Logger
from bot.common.helpers import response_processing


class CryptocurrencyService:
    def __init__(self):
        self.logger = Logger("CryptocurrencyService").get_logger()

    async def send_crypto(self, amount, currency, address):
        address = '1Hpv9WVt1FgW4WYHQSk3ridsJhEWbgob8C'  # tmp
        async with ClientSession() as session:
            params = {
                'amount': amount,
                'to': address,
            }
            async with session.post(
                constants.CC_SEND_CRYPTO.format(currency=currency.lower()),
                params=params,
                headers={'CCAPI-KEY': settings.CRYPTOCURRENCY_TOKEN},
            ) as response:
                response = await response_processing(response)
                return response['result']

    async def give_address(self, tg_id, currency):
        async with ClientSession() as session:
            params = {'label': tg_id}
            async with session.post(
                constants.CC_GIVE_ADDRESS.format(currency=currency.lower()),
                params=params,
                headers={'CCAPI-KEY': settings.CRYPTOCURRENCY_TOKEN},
            ) as response:
                response = await response_processing(response)
                return response['result']['address']


cryptocurrency_service = CryptocurrencyService()
