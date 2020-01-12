from unittest import TestCase
import os
from greentea.text import Text, Texts


class TestText(TestCase):
    """Tests for Text."""

    def test_concat_concatenation(self):
        """Join with '。' if `text` is not empty."""
        actual = Text('a').concat(Text('b'), '。')
        self.assertEqual(actual, Text('a。b'))

    def test_is_empty_empty_string_true(self):
        """Return true if text is ''."""
        self.assertTrue(Text('').is_empty())

    def test_is_empty_false(self):
        """Return true if the length of the text is more than one."""
        self.assertFalse(Text('a').is_empty())

    def test_end_with_linesep(self):
        """ends_with_linesep.

        Append a line separator if not exists.

        """
        target = Text('a')
        result = target.end_with_linesep()
        self.assertEqual(result, Text(f'a{os.linesep}'))

    def test_end_with_linesep_skip(self):
        """ends_with_linesep.

        Return itself if the `text` ends with os.linesep.

        """
        target = Text(f'a{os.linesep}')
        result = target.end_with_linesep()
        self.assertEqual(result, target)

    def test_remove_consec_linesep(self):
        """Convert the consecutive line separators to a line separator."""
        target = Text(f'a{os.linesep}{os.linesep}{os.linesep}b')

        actual = target.remove_consec_linesep()
        self.assertEqual(actual, Text(f'a{os.linesep}b'))

    def test_tokenize(self):
        """tokenize."""
        result = Text('ab bc cd').tokenize(
                lambda x: [Text(t) for t in x.split()])

        self.assertEqual(result, Texts([Text('ab'), Text('bc'), Text('cd')]))

    def test_join(self):
        """join"""
        expected = Text('.').join(Texts([Text('a'), Text('b')]))
        self.assertEqual(expected, Text('a.b'))
