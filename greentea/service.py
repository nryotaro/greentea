"""Expose the Use case template class."""
import abc
from typing import Any


class BaseService(metaclass=abc.ABCMeta):
    """A template class for an use case."""

    @abc.abstractmethod
    def run(self, **kwargs) -> Any:
        """Execute the use case."""
