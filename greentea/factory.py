"""Provide factories that create objects."""
import abc
import argparse
from .log import LogConfiguration
from .service import BaseService


class BaseFactory(metaclass=abc.ABCMeta):
    """An abstract-factory class."""

    def __init__(self, namespace: argparse.Namespace):
        """Take a namespace that holds command-line arguments."""
        self.namespace = namespace

    @abc.abstractmethod
    def create_service(self) -> BaseService:
        """Create a service."""

    @abc.abstractmethod
    def create_arguments(self) -> dict:
        """Create the arguments for the service."""

    @abc.abstractmethod
    def create_log_configuration(self) -> LogConfiguration:
        """Create an instance to configure the logging system."""
