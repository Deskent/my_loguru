import datetime
import os

from myloguru.my_loguru import MyLogger, get_logger
from loguru import logger


def test_set_log_level(current_date):
    test_logger = get_logger(level=1)
    test_logger.debug("Test")
    assert os.path.exists(f'./logs/{current_date}/debug.log')
    test_logger.info("Test")
    test_logger.warning("Test")
    assert os.path.exists(f'./logs/{current_date}/warning.log')
    test_logger.error("Test")
    assert os.path.exists(f'./logs/{current_date}/error.log')


def test_my_logger(delete_logs_dir, test_logger):
    assert test_logger.log("INFO", "test") is None
    assert test_logger.info("test") is None
    assert test_logger.warning("test") is None
    assert test_logger.debug("test") is None
    assert test_logger.error("test") is None
    assert test_logger.success("test") is None


def test_my_logger_with_another_logs_dir(delete_logs_dir):
    logger_test = MyLogger(logger, logs_dir='test_dir').get_default().get_new_logger()
    logger_test.error("test")
    assert os.path.exists("test_dir")


def test_my_logger_with_another_parent_dir(delete_logs_dir):
    logger_test = MyLogger(logger, parent_dir='test_parent_dir').get_default().get_new_logger()

    logger_test.error("test")
    assert os.path.exists("test_parent_dir")


def test_my_logger_without_date_dir(delete_logs_dir, test_logger):
    logger_test = MyLogger(logger, date_dir=False).get_default().get_new_logger()
    logger_test.error("test")
    assert not os.path.exists(datetime.datetime.today().strftime("%Y-%m-%d"))


def test_my_logger_default_log_level(delete_logs_dir, test_logger):
    logger_test = MyLogger(logger, level=1).get_default().get_new_logger()
    assert logger_test.error("test") is None
