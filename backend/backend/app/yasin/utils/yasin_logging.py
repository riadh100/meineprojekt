"""
Zentrales Logging-System
für Yasin AI.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "yasin_ai.log"


def get_logger(
    name: str = "yasin_ai",
    level: int = logging.INFO,
) -> logging.Logger:

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level)

    formatter = logging.Formatter(
        "[%(asctime)s] "
        "[%(levelname)s] "
        "[%(name)s] "
        "%(message)s",
        "%Y-%m-%d %H:%M:%S",
    )

    # Konsolen-Logger
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Datei-Logger mit Rotation
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


logger = get_logger()


def debug(message: str):

    logger.debug(message)


def info(message: str):

    logger.info(message)


def warning(message: str):

    logger.warning(message)


def error(message: str):

    logger.error(message)


def critical(message: str):

    logger.critical(message)
