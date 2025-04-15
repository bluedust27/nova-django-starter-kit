import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from common.config import config

MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3


def setup_logging():
    logging_config = config.get_section("logging")

    log_level = logging_config.get("level", "INFO").upper()
    enable_console = logging_config.get("enable_console", True)
    enable_file = logging_config.get("enable_file", True)
    log_dir = Path(logging_config.get("log_dir", "/app/logs"))
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / logging_config.get("log_file", "app.log")

    logger = logging.getLogger()
    logger.setLevel(log_level)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s %(name)s.%(funcName)s - %(message)s"
    )

    if enable_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if enable_file:
        file_handler = RotatingFileHandler(
            str(log_file), maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
