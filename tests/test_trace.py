from unittest import TestCase
from unittest.mock import MagicMock, call, patch
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

    @patch('logging.Formatter', spec=logging.Formatter)
    @patch('logging.getLogger', spec=logging.Logger)
    @patch('logging.StreamHandler', spec=logging.StreamHandler)
    def test_create_tracer(
            self,
            stream_handler,
            get_logger,
            formatter_constructor):
        name = 'tracing'
        formatter_str = '%(levelname)s:%(asctime)s:%(name)s:%(message)s'
        level = logging.DEBUG
        handler = stream_handler.return_value
        formatter = formatter_constructor.return_value
        logger = get_logger.return_value

        tracer = t.Tracer.create_tracer(name, formatter_str, level)

        self.assertIsInstance(tracer, t.Tracer)

        self.assertEqual(get_logger.call_args_list, [call(name)])
        self.assertEqual(stream_handler.call_args_list, [call()])
        self.assertEqual(formatter_constructor.call_args_list,
                         [call(formatter_str)])
        self.assertEqual(
            handler.setFormatter.call_args_list,
            [call(formatter)])
        self.assertEqual(handler.setLevel.call_args_list, [call(level)])
        self.assertEqual(logger.addHandler.call_args_list, [call(handler)])
        self.assertEqual(tracer.logger, logger)
        self.assertEqual(tracer.log_level, level)
