import logging
import sys

from bot.common.config import settings


class Logger:
    def __init__(self, name):
        self.name = name
        self.log_filepath = settings.LOGGER_FILE_PATH
        self.format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
        )

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        handler.setFormatter(self.format)
        file_handler = logging.FileHandler(self.log_filepath)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self.format)
        logger.addHandler(handler)
        logger.addHandler(file_handler)
        return logger
