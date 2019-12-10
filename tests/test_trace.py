from unittest import TestCase
from unittest.mock import MagicMock, call, patch
import logging
import greentea.trace as t


class TestTracer(TestCase):

    def setUp(self):
        self.logger = MagicMock(spec=logging.Logger)
        self.trace_level = MagicMock(spec=t.TraceLevel)
        self.tracer = t.Tracer(self.logger, self.trace_level)

    @patch('greentea.trace.Invocation.create_from',
           return_value=MagicMock(spec=t.Invocation))
    def test_trace(self, create_from):
        return_value = MagicMock()
        @self.tracer.trace
        def run(positional_argument, keyword=None):
            nonlocal return_value
            return return_value

        positinal_argument = MagicMock()
        keyword_argument = MagicMock()

        invocation = create_from.return_value

        actual = run(positinal_argument, keyword=keyword_argument)

        self.assertEqual(actual, return_value)

        self.assertEqual(
            self.trace_level.start.call_args_list, [call(self.logger,
                                                         invocation)])
        self.assertEqual(
            self.trace_level.end.call_args_list,
            [call(self.logger, invocation, return_value)])

    @patch('logging.Formatter', spec=logging.Formatter)
    @patch('logging.getLogger', spec=logging.Logger)
    @patch('logging.StreamHandler', spec=logging.StreamHandler)
    def test_create_tracer(
            self,
            stream_handler,
            get_logger,
            formatter_constructor):
        handler = stream_handler.return_value
        logger = get_logger.return_value

        tracer = t.Tracer.create_tracer()

        self.assertIsInstance(tracer, t.Tracer)

        self.assertEqual(stream_handler.call_args_list, [call()])
        self.assertEqual(handler.setLevel.call_args_list,
                         [call(logging.DEBUG)])
        formatter_str = '%(levelname)s:%(asctime)s:%(name)s:%(message)s'
        self.assertEqual(formatter_constructor.call_args_list,
                         [call(formatter_str)])
        formatter = formatter_constructor.return_value
        self.assertEqual(
            handler.setFormatter.call_args_list,
            [call(formatter)])
        self.assertEqual(get_logger.call_args_list, [call('trace')])
        self.assertEqual(logger.setLevel.call_args_list,
                         [call(logging.DEBUG)])
        self.assertEqual(logger.addHandler.call_args_list, [call(handler)])
        self.assertEqual(tracer.logger, logger)
        self.assertEqual(tracer.trace_level,
                         t.TraceLevel(logging.DEBUG, logging.DEBUG))
