"""Messages model.

Attributes:
    messages (Messages): handle the messages.
"""

from typing import Optional


class Messages(list):
    """Messages class."""

    def __init__(self):
        """Add the help dict."""
        self._stack = {}
        self._index = 0
        self.help = {
            "q or quit": "quit the game",
            "r or right": "moove to the right",
            "l or left": "moove to the left",
            "u or up": "moove to the top",
            "d or down": "moove to the bottom",
            "<direction> <x>": "repeat the direction x time",
        }

    def add(self, message: str, level: int, tag: Optional[str] = None) -> None:
        """Add a message.

        Also purge the other message with the same level
        to avoid having too much messages.

        Args:
            message (str): the message.
            level (int): the message level (0 for info, 1 for warning, 2 for error).
            tag (str): a tag if you want a unique type of message.
        """
        if not tag:
            tag = self._index
            self._index += 1

        self._stack[tag] = (message, level)

    def get(self) -> list:
        """Return all messages and purge them.

        Returns:
            list: the messages list.
        """
        result, self._stack = self._stack, {}
        return result.values()


messages = Messages()
