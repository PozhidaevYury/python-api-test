import logging
import sys
from logging.handlers import TimedRotatingFileHandler


class Logger(object):

    def __init__(self):
        self.formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
        self.log_file = "/Users/urij/PycharmProjects/python-api-test/log/my_app.log"

    def _get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def _get_file_handler(self):
        file_handler = TimedRotatingFileHandler(self.log_file, when='midnight')
        file_handler.setFormatter(self.formatter)
        return file_handler

    def get_logger(self, logger_name=""):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        logger.addHandler(self._get_console_handler())
        logger.addHandler(self._get_file_handler())
        logger.propagate = False
        return logger
