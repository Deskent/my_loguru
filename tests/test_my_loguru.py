import datetime
import os

from myloguru.my_loguru import MyLogger, get_logger, logger


def test_my_logger(delete_logs_dir):
    logger_test = get_logger()
    assert logger_test.info("test") is None
    assert logger_test.warning("test") is None
    assert logger_test.debug("test") is None
    assert logger_test.error("test") is None
    assert logger_test.success("test") is None


def test_my_logger_with_another_logs_dir(delete_logs_dir):
    logger_test = MyLogger(logger, logs_dir='test_dir').get_default().get_new_logger()
    logger_test.error("test")
    assert os.path.exists("test_dir")


def test_my_logger_with_another_parent_dir(delete_logs_dir):
    logger_test = MyLogger(logger, parent_dir='test_parent_dir').get_default().get_new_logger()

    logger_test.error("test")
    assert os.path.exists("test_parent_dir")


def test_my_logger_without_date_dir(delete_logs_dir):
    logger_test = MyLogger(logger, date_dir=False).get_default().get_new_logger()
    logger_test.error("test")
    assert not os.path.exists(datetime.datetime.today().strftime("%Y-%m-%d"))


def test_my_logger_default_log_level(delete_logs_dir):
    logger_test = MyLogger(logger, default_log_level=1).get_default().get_new_logger()
    assert logger_test.error("test") is None
