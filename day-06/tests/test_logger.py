import logging
from pathlib import Path

from app_logger.logger import get_logger


def test_get_logger_returns_logger():
    logger = get_logger("test_app")

    assert isinstance(logger, logging.Logger)


def test_get_logger_sets_info_level():
    logger = get_logger("test_app")

    assert logger.level == logging.INFO


def test_get_logger_adds_file_handler():
    logger = get_logger("test_app_with_file_handler")

    assert len(logger.handlers) == 1


def test_logger_writes_to_file(tmp_path):
    log_file = tmp_path / "app.log"
    logger = get_logger("file_test", log_file=log_file)
    logger.info("Hello from Day 6")

    with open(log_file, encoding="utf-8") as file:
        contents = file.read()

    assert "Hello from Day 6" in contents


def test_logger_uses_default_log_file():
    message = "Default log path test"
    logger = get_logger("default_log_file_test")
    logger.info(message)

    log_file = Path(__file__).resolve().parents[1] / "logs" / "app.log"
    with open(log_file, encoding="utf-8") as file:
        contents = file.read()

    assert message in contents


def test_logger_includes_level_in_file():
    message = "Formatter level test"
    logger = get_logger("formatter_level_test")
    logger.info(message)

    with open("logs/app.log", encoding="utf-8") as file:
        lines = file.readlines()

    assert any("INFO" in line and message in line for line in lines)


def test_logger_writes_warning_to_file():
    message = "Unique warning message"
    logger = get_logger("warning_file_test")
    logger.warning(message)

    with open("logs/app.log", encoding="utf-8") as file:
        lines = file.readlines()

    assert any("WARNING" in line and message in line for line in lines)


def test_logger_writes_error_to_file():
    message = "Unique error message"
    logger = get_logger("error_file_test")
    logger.error(message)

    with open("logs/app.log", encoding="utf-8") as file:
        lines = file.readlines()

    assert any("ERROR" in line and message in line for line in lines)


def test_get_logger_does_not_add_duplicate_handlers():
    get_logger("duplicate_test")
    logger = get_logger("duplicate_test")

    assert len(logger.handlers) == 1