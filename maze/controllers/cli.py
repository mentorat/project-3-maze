"""CLI controllers."""

import re

from typing import Tuple

from maze.models.game import Game


class Keyboard:
    """CLI Keyboard class."""

    def __init__(self, game: Game):
        """Init."""
        self.game: Game = game
        self.mapping = {"r": "right", "l": "left", "u": "up", "d": "down", "q": "quit"}

    def wait_for_command(self) -> Tuple[str, int]:
        """Wait for a command."""
        command = input()

        pattern = re.match(r"^(?P<command>[A-z]*) ?(?P<repeat>[0-9]*)?", command)
        values = {}
        if pattern:
            values = pattern.groupdict()

        command = values["command"]
        repeat = int(values["repeat"] or 1)

        if command in self.mapping:
            command = self.mapping[command]

        return command, repeat
