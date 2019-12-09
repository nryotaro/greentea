from unittest import TestCase
from unittest.mock import MagicMock, call
import logging
import greentea.trace as t


class TestTracer(TestCase):

    def setUp(self):
        self.logger = MagicMock(spec=logging.Logger)
        self.log_level = MagicMock(spec=int)
        self.tracer = t.Tracer(self.logger, self.log_level)

    def test_trace(self):
        return_value = 42
        @self.tracer.trace
        def run(positional_argument, keyword='key'):
            nonlocal return_value
            return return_value

        positinal_argument = 'pos'
        keyword_argument = 'key'
        actual = run(positinal_argument, keyword=keyword_argument)

        self.assertEqual(actual, return_value)
        calling = "run(('pos',), {'keyword': 'key'})"
        self.assertEqual(
            self.logger.log.call_args_list,
            [call(self.log_level, calling),
             call(self.log_level, f"{calling} -> 42")])
