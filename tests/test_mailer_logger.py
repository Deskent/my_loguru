import os

from myloguru.mailer import get_mailer_logger


def test_mailer_logger_admin(delete_logs_dir, current_date):
    test_mailer_logger = get_mailer_logger()
    assert test_mailer_logger.admin("Admin test") is None
    assert test_mailer_logger.token("Token test") is None
    assert test_mailer_logger.openai("Open Ai test") is None
    assert os.path.exists(f"logs/{current_date}/admin.log")
    assert os.path.exists(f"logs/{current_date}/error.log")
    assert os.path.exists(f"logs/{current_date}/openai.log")


def test_mailer_change_dir(delete_logs_dir, current_date):

    test_mailer_logger = get_mailer_logger(logs_dir='test_dir')
    test_mailer_logger.admin('test')
    assert os.path.exists(f"test_dir/{current_date}/admin.log")
    test_mailer_logger.token('test')
    assert os.path.exists(f"test_dir/{current_date}/token.log")
    test_mailer_logger.openai('test')
    assert os.path.exists(f"test_dir/{current_date}/openai.log")
    test_mailer_logger.warning('test')
    assert os.path.exists(f"test_dir/{current_date}/warning.log")
    test_mailer_logger.error("test")
    assert os.path.exists(f"test_dir/{current_date}/error.log")
