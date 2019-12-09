"""Provide methods to trace execution."""
import logging
import functools
from typing import Callable


class Tracer:
    """Record information about a program's execution."""

    def __init__(self,
                 logger: logging.Logger,
                 log_level: int = logging.DEBUG):
        """Take a logger and the level for tracing."""
        self.logger = logger
        self.log_level = log_level

    def trace(self, function: Callable):
        """Provide a function decorator to trace the decorated function."""
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            call_message = '%s(%s, %s)' % (function.__name__, args, kwargs)
            self._log(call_message)
            result = function(*args, **kwargs)
            self._log('%s -> %s' % (call_message, result))
            return result
        return wrapper

    def _log(self, message):
        self.logger.log(self.log_level, message)

    @classmethod
    def create_tracer(
            cls,
            logger_name: str = 'trace',
            format: str = '%(levelname)s:%(asctime)s:%(name)s:%(message)s',
            level: int = logging.DEBUG):
        """Create a tracer named with `logger_name`.

        Returns
        -------
        tracer: Tracer

        """
        handler = logging.StreamHandler()
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(format))
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return Tracer(logger, level)
