"""Messages model.

Attributes:
    messages (Messages): handle the messages.
"""


class Messages(list):
    """Messages class."""

    def __init__(self):
        """Add the help dict."""
        self.help = {
            "q or quit": "quit the game",
            "r or right": "moove to the right",
            "l or left": "moove to the left",
            "u or up": "moove to the top",
            "d or down": "moove to the bottom",
            "<direction> <x>": "repeat the direction x time",
        }

    def add(self, message: str, level: int) -> None:
        """Add a message.

        Also purge the other message with the same level
        to avoid having too much messages.

        Args:
            message (str): the message.
            level (int): the message level (0 for info, 1 for warning, 2 for error).
        """
        for index, item in enumerate(self):
            if level == item[1]:
                del self[index]
        self.append((message, level))

    def get(self) -> list:
        """Return all messages and purge them.

        Returns:
            list: the messages list.
        """
        result = self[:]
        del self[:]
        return result


messages = Messages()
