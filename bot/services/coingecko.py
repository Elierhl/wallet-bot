from aiohttp import ClientSession

from bot.common import constants
from bot.common.helpers import response_processing
from bot.common.logger import Logger


class CoingeckoService:
    def __init__(self):
        self.logger = Logger("CoingeckoService").get_logger()

    async def get_price(self, crypto, fiat):
        async with ClientSession() as session:
            params = {
                'ids': crypto,
                'vs_currencies': fiat,
            }
            async with session.get(constants.CG_GET_PRICE, params=params) as response:
                response = await response_processing(response)
                return response


coingecko_service = CoingeckoService()
