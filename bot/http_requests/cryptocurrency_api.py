from os import getenv

from aiohttp import ClientSession

from bot.consts import urls
from bot.http_requests.helpers import response_processing


async def send_crypto(amount, currency, address):
    address = '1Hpv9WVt1FgW4WYHQSk3ridsJhEWbgob8C'  # tmp
    async with ClientSession() as session:
        params = {
            'amount': amount,
            'to': address,
        }
        async with session.post(
            urls.CC_SEND_CRYPTO.format(currency=currency.lower()),
            params=params,
            headers={'CCAPI-KEY': getenv('cryptocurrency_token')},
        ) as response:
            response = await response_processing(response)
            return response['result']


async def give_address(tg_id, currency):
    async with ClientSession() as session:
        params = {'label': tg_id}
        async with session.post(
            urls.CC_GIVE_ADDRESS.format(currency=currency.lower()),
            params=params,
            headers={'CCAPI-KEY': getenv('cryptocurrency_token')},
        ) as response:
            response = await response_processing(response)
            return response['result']['address']
