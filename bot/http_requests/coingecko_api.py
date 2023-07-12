import logging

from aiohttp import ClientSession

from bot.consts import urls
from bot.http_requests.helpers import response_processing

logger = logging.getLogger(__name__)


async def get_price(crypto, fiat):
    async with ClientSession() as session:
        params = {
            'ids': crypto,
            'vs_currencies': fiat,
        }
        async with session.get(urls.CG_GET_PRICE, params=params) as response:
            response = await response_processing(response)
            return response
