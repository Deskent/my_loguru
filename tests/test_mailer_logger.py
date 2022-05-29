from myloguru.mailer import logger


def test_my_logger():
    assert logger.info("test") is None
