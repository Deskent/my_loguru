from myloguru.my_loguru import logger


def test_my_logger():
    assert logger.info("test") is None
