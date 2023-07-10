import logging
from os import getenv

from aiohttp import ClientSession

from bot import urls


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
        ) as resp:
            try:
                resp.raise_for_status()
                response = await resp.json()
                assert list(response.keys()) == ['result']

            except Exception as e:
                logging.error(f'Error while sending crypto. Traceback: {e}')
                return None

            else:
                logging.info(response)
                return response
