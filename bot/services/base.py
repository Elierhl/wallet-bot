from bot.common.logger import Logger


class Controller:
    def __init__(self, module_name):
        self.logger = Logger(module_name).get_logger()
