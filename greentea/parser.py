"""Expose base classes for parseing command-line arguments."""
import abc
from typing import Sequence
from argparse import ArgumentParser, Namespace
from .factory import BaseFactory


class BaseParser(metaclass=abc.ABCMeta):
    """An abstract class for parsing command-line arguments."""

    def __init__(self):
        """Define a command."""
        self.base_parser = self.create_base_parser()
        self.base_parser.add_argument(
            '-v', '--verbose', help='Be verbose.', action='store_true')
        self.parser = self.define_parser()

    def parse(self, arguments: Sequence[str]) -> BaseFactory:
        """Interpret the command-line arguments.

        Create a factory object to prepare objects required by
        a service class that extends :py:class:`greentea.service.BaseService`.

        """
        namespace = self.parser.parse_args(arguments)
        return self.create_factory(namespace)

    @abc.abstractclassmethod
    def create_base_parser(cls) -> ArgumentParser:
        """Create a parser that will take the command-line arguments."""

    @abc.abstractmethod
    def define_parser(self) -> ArgumentParser:
        """Define a command."""

    @abc.abstractmethod
    def create_factory(self, namespace: Namespace) -> BaseFactory:
        """Create a factory from a parsed command-line properties."""
