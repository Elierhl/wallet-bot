from bot.common import constants
from bot.services.external.base import AsyncRequest


class CoingeckoService(AsyncRequest):
    def __init__(self):
        super().__init__(module_name=__name__)

    async def get_price(self, crypto, fiat):
        async with self.session_pool() as session:
            params = {
                'ids': crypto,
                'vs_currencies': fiat,
            }
            async with session.get(constants.CG_GET_PRICE, params=params) as response:
                response = await self.response_processing(response)
                return response


coingecko_service = CoingeckoService()
