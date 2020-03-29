"""Model wrapper."""

from maze.config.settings import MAP_LEVEL_1
from maze.models.map import Map
from maze.models.hero import Hero


class Game:
    """Wrap all models."""

    def __init__(self, filename=MAP_LEVEL_1):
        """Init."""
        self.maze = Map(filename)
        self.hero = Hero()
        self.maze.add(self.hero)

    def update(self, command: str, repeat: int):
        """Update the game from the command."""
        for _ in range(repeat):
            istrue = self.hero.move(command)
            if not istrue:
                break
