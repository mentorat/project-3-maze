"""Position module."""


class Position(tuple):
    """Classe représentant une position dans un labyrinthe à deux dimensions."""

    def __new__(cls, x, y):
        """Crée une nouvelle position."""
        return super().__new__(cls, (x, y))

    @property
    def x(self):
        """Position horizontale dans le labyrinthe."""
        return self[0]

    @property
    def y(self):
        """Position verticale dans le labyrithe."""
        return self[1]

    @property
    def up(self):
        """Position adjacente située au dessus."""
        return Position(self.x, self.y - 1)

    @property
    def down(self):
        """Position adjacente située au dessous."""
        return Position(self.x, self.y + 1)

    @property
    def left(self):
        """Position adjacente située à gauche."""
        return Position(self.x - 1, self.y)

    @property
    def right(self):
        """Position adjacente située à droite."""
        return Position(self.x + 1, self.y)

    def get(self, direction: str):
        """Get a position."""
        if direction not in ("up", "down", "left", "right"):
            return None
        return getattr(self, direction)
