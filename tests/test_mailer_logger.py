import os

import pytest

from myloguru.mailer import MailerLogger, get_logger


@pytest.fixture
def test_mailer_logger() -> 'MailerLogger':
    return get_logger()


def test_mailer_logger_admin(test_mailer_logger, delete_logs_dir, current_date):
    assert test_mailer_logger.admin("Admin test") is None
    assert test_mailer_logger.token("Token test") is None
    assert test_mailer_logger.openai("Open Ai test") is None
    assert os.path.exists(f"logs/{current_date}/admin.log")
    assert os.path.exists(f"logs/{current_date}/error.log")
    assert os.path.exists(f"logs/{current_date}/openai.log")


def test_mailer_change_dir(delete_logs_dir, current_date, test_mailer_logger, test_logger):
    test_logger: 'MailerLogger' = MailerLogger(logger=test_logger, logs_dir='test_dir').get_default().get_new_logger()
    test_logger.admin('test')
    assert os.path.exists(f"test_dir/{current_date}/admin.log")
    test_logger.token('test')
    assert os.path.exists(f"test_dir/{current_date}/token.log")
    test_logger.openai('test')
    assert os.path.exists(f"test_dir/{current_date}/openai.log")
    test_logger.warning('test')
    assert os.path.exists(f"test_dir/{current_date}/warning.log")
    test_logger.error("test")
    assert os.path.exists(f"test_dir/{current_date}/error.log")
