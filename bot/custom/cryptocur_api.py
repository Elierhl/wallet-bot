import logging
from os import getenv

from aiohttp import ClientSession

from bot import urls


async def response_processing(response):
    try:
        response.raise_for_status()
        response = await response.json()
        assert list(response.keys()) == ['result']

    except Exception as e:
        logging.error(f'Error while sending crypto. Traceback: {e}')
        return None

    else:
        logging.info(response)
        return response['result']


async def send_crypto(amount, currency, address):
    address = '1Hpv9WVt1FgW4WYHQSk3ridsJhEWbgob8C'  # tmp
    async with ClientSession() as session:
        async with session.post(
            urls.CC_SEND_API.format(
                key=getenv('cryptocur_token'),
                amount=amount,
                currency=currency.lower(),
                address=address,
            )
        ) as response:
            return response_processing(response)


async def give_address(telegram_id, currency):
    async with ClientSession() as session:
        async with session.post(
            urls.CC_GIVE_ADDRESS.format(
                key=getenv('cryptocur_token'),
                currency=currency.lower(),
                telegram_id=telegram_id,
            )
        ) as response:
            response = await response_processing(response)
            return response['address']
