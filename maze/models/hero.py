"""Hero module."""

from typing import Optional

from maze.settings import ITEMS

from maze.models.position import Position
from maze.models.messages import messages


class Hero:
    """Hero class."""

    def __init__(self):
        """Init."""
        self.maze = None
        self.position: Optional[Position] = None
        self.items = []

    def found_exit(self) -> bool:
        """Prédicat qui retourne VRAI si le héro a trouvé la sortie.

        Returns:
            bool: True if the player found the exit, then False.
        """
        return self.position == self.maze.exit

    def found_all_items(self):
        """Return True if the Hero found all items."""
        return self.items == list(ITEMS.keys())

    def move(self, direction: str) -> bool:
        """Déplace le héro dans la direction demandée.

        Returns:
            bool: the move status.
        """
        if not self.maze or not self.position:
            raise ValueError("Hero attributes are not defined.")

        new_position = self.position.get(direction)
        if new_position is None:
            messages.add(f"The direction '{direction}' is not valid.", 2)
        elif new_position in self.maze:
            self.position = new_position
            messages.add(f"New position: '{new_position}'.", 0, "position")
            return True
        elif new_position in self.maze.walls:
            messages.add(f"The position '{new_position}' is a wall.", 2)
        else:
            messages.add(f"The position '{new_position}' is outside the maze.", 2)
        return False
