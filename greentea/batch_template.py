"""Expose the template class for entrypoints."""
import sys
from .parser import BaseParser


class BaseBatch:
    """Provide a template method for entrypoints."""

    def __init__(self, parser: BaseParser):
        """Take a parser."""
        self.parser = parser

    def run(self):
        """Create a service and run it."""
        factory = self.parser.parse(sys.argv[1:])
        log_configuration = factory.create_log_configuration()
        log_configuration.configure()
        service = factory.create_service()
        arguments = factory.create_arguments()
        service.run(**arguments)
