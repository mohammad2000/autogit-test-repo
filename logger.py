"""Structured logging service with rotation and formatters."""
import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Optional

class StructuredLogger:
    """Application logger with JSON output and file rotation."""

    def __init__(self, name: str, log_dir: str = "logs", level: int = logging.INFO):
        self.name = name
        self.log_dir = log_dir
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)
        os.makedirs(log_dir, exist_ok=True)
        self._setup_handlers()

    def _setup_handlers(self):
        fmt = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        # Console handler
        console = logging.StreamHandler()
        console.setFormatter(fmt)
        self._logger.addHandler(console)

        # File handler with rotation
        file_handler = RotatingFileHandler(
            os.path.join(self.log_dir, f"{self.name}.log"),
            maxBytes=10 * 1024 * 1024,  # 10 MB
            backupCount=5,
        )
        file_handler.setFormatter(fmt)
        self._logger.addHandler(file_handler)

    def info(self, msg: str, **kwargs):
        self._logger.info(msg, extra=kwargs)

    def error(self, msg: str, exc: Optional[Exception] = None, **kwargs):
        self._logger.error(msg, exc_info=exc, extra=kwargs)

    def warning(self, msg: str, **kwargs):
        self._logger.warning(msg, extra=kwargs)

    def debug(self, msg: str, **kwargs):
        self._logger.debug(msg, extra=kwargs)
