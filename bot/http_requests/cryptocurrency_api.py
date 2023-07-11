from aiohttp import ClientSession

from bot.consts import urls
from bot.http_requests.helpers import response_processing


async def send_crypto(amount, currency, address):
    address = '1Hpv9WVt1FgW4WYHQSk3ridsJhEWbgob8C'  # tmp
    async with ClientSession() as session:
        params = {
            'amount': amount,
            'currency': currency.lower(),
            'address': address,
        }
        async with session.post(urls.CC_SEND_CRYPTO, params=params) as response:
            response = await response_processing(response)
            return response['result']


async def give_address(tg_id, currency):
    async with ClientSession() as session:
        params = {
            'currency': currency.lower(),
            'telegram_id': tg_id,
        }
        async with session.post(urls.CC_GIVE_ADDRESS, params=params) as response:
            response = await response_processing(response)
            return response['result']['address']
