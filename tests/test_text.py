from unittest import TestCase
from greentea.text import Text


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
