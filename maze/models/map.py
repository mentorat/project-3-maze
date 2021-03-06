"""Map module."""

import random
from typing import Set, Dict, Optional

from maze.settings import PASSAGE, START, EXIT, ITEMS

from maze.models.position import Position
from maze.models.hero import Hero


class Map:
    """maze Map class.

    Handle the positions.

    Args:
        filename (str): the map file to load.

    Attributes:
        hero (Hero): the Hero character.
        start (Position): the start position.
        exit (Position): the exit position.
        passages (set): the passages.
        walls (set): the walls.

    """

    def __init__(self, filename: str) -> None:
        """Init the class."""
        self.hero: Optional[Hero] = None

        self.start: Optional[Position] = None
        self.exit: Optional[Position] = None

        self.passages: Set[Position] = set()
        self.walls: Set[Position] = set()

        self.items: Dict[Position, str] = {}

        self.height = 0
        self.width = 0

        self._load_from_file(filename)

    def __contains__(self, position: Position) -> bool:
        """Return True if the given position is in the paths.

        Args:
            position: the given Position.

        Returns:
            bool: True if the position is in the positions, else False.

        """
        return position in self.passages

    def _load_from_file(self, filename: str) -> None:
        """Load the map from a given file.

        Args:
            filename (str): the file path.

        Returns:
            None

        """
        with open(filename) as maze:
            for y, line in enumerate(maze):
                for x, col in enumerate(line):
                    if col in (PASSAGE, START, EXIT):
                        self.passages.add(Position(x, y))
                        if col == START:
                            self.start = Position(x, y)
                        elif col == EXIT:
                            self.exit = Position(x, y)
                    else:
                        self.walls.add(Position(x, y))
                self.width = max(self.width, x)
            self.height = y + 1

    def add(self, hero: Hero):
        """Place the hero on the board."""
        hero.position = self.start
        hero.maze = self
        self.hero = hero

    def place_items(self):
        """Initialize the items."""
        passages = [
            pos for pos in self.passages if pos != self.start and pos != self.exit
        ]
        for name in ITEMS:
            position = random.choice(passages)
            self.items[position] = name
