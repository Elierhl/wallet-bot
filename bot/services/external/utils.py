from aiohttp import ClientSession

from bot.common.logger import Logger


class AsyncRequest:
    def __init__(self, module_name):
        self.logger = Logger(module_name).get_logger()

    session_pool = ClientSession

    async def response_processing(self, response):
        try:
            response.raise_for_status()
            response = await response.json()

        except Exception as e:
            self.logger.error(f'Error. Traceback: {e}')
            return None

        else:
            return response
