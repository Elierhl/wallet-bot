import logging

logger = logging.getLogger(__name__)


async def response_processing(response):
    try:
        response.raise_for_status()
        response = await response.json()

    except Exception as e:
        logger.error(f'Error. Traceback: {e}')
        return None

    else:
        return response
