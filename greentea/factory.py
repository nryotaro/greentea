"""Provide factories that create objects."""
import abc
import argparse
from .log import LogConfiguration


class BaseFactory(metaclass=abc.ABCMeta):
    """An abstract-factory class."""

    def __init__(self, namespace: argparse.Namespace):
        """Take a namespace that holds command-line arguments."""
        self.namespace = namespace

    @abc.abstractmethod
    def create_service(self):
        """Create a service."""

    @abc.abstractmethod
    def create_arguments(self) -> dict:
        """Create the arguments for the runner."""

    @abc.abstractproperty
    def base_logger_name(self) -> str:
        """Return the base logger name."""

    @abc.abstractmethod
    def create_log_configuration(self) -> LogConfiguration:
        """Create an instance to configure the logging system."""
