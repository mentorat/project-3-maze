"""Model wrapper."""

from maze.settings import MAP_LEVEL_1
from maze.models.map import Map
from maze.models.hero import Hero
from maze.models.messages import messages


class Game:
    """Wrap all models."""

    def __init__(self, filename=MAP_LEVEL_1):
        """Init."""
        self.maze = Map(filename)
        self.hero = Hero()
        self.maze.add(self.hero)
        self.maze.place_items()

    def update(self, command: str, repeat: int) -> None:
        """Update the game from the command."""
        for _ in range(repeat):
            istrue = self.hero.move(command)
            if not istrue:
                break
            self.check_found_item()

    def check_found_item(self):
        """Check if the hero found an item."""
        position = self.hero.position
        items = self.maze.items
        if position in items:
            messages.add(f"Item '{items[position]}' found !", 0)
            self.hero.items.append(items[position])
            del items[position]
