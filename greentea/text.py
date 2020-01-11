"""Implement a wrapper for `str`."""
from dataclasses import dataclass


@dataclass
class Text:
    """Represent a text.

    Attributes
    ----------
    text: str

    """

    text: str

    def concat(self, text, separator='. '):
        """Concatenation of itself and `text`.

        Parameters
        ----------
        text: Text
            a text to be concatenated.

        """
        if text.is_empty():
            return self
        return Text(f'{self.text}{separator}{text.text}')

    def is_empty(self) -> bool:
        """Return `True` iff empty."""
        return len(self.text) == 0

    def strip(self):
        """Return the Stripped text.

        Returns
        -------
        Text

        """
        text = self.text.strip()
        return Text(text)

    def empty():
        """Return an emtpy :py:class:`Text`."""
        return Text('')
