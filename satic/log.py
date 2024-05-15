import logging
from logging import getLogger
from logging.handlers import RotatingFileHandler
from logging.handlers import WatchedFileHandler


def execlude_debug(exclude_list):
    for name in exclude_list:
        logger = logging.getLogger(name)
        logger.setLevel(logging.ERROR)


def init_log():
    format = '%(asctime)s [%(threadName)s:%(thread)d] %(levelname)-5s %(name)s - %(message)s (%(funcName)s:%(lineno)d)'
    handler = WatchedFileHandler("./satic.log", encoding='utf-8')
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)

    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # execlude_debug(['aiosqlite', 'passlib', 'db_client', "tortoise", "multipart"])