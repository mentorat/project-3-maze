"""CLI view."""

import os

from termcolor import cprint
from colorama import init as colorinit

from maze.config.settings import (
    WALL,
    PASSAGE,
    EXIT,
    HERO,
    C__WALL,
    C__PASSAGE,
    C__EXIT,
    C__HERO,
    C__LEVELS,
)
from maze.models.game import Game
from maze.models.position import Position
from maze.models.messages import messages


class Display:
    """map view class."""

    def __init__(self, game: Game, use_color=True):
        """Init."""
        colorinit(convert=True)
        self.use_color = use_color
        self.game = game
        self.maze = game.maze
        self.turns = 0

    def refresh(self):
        """Display the map."""
        self.turns += 1
        os.system("cls" if os.name == "nt" else "clear")
        print("\n")
        cprint(" MAZE ".center(self.maze.width, "-"), "yellow")
        cprint(f" Turn {self.turns} ".center(self.maze.width, "-"), "yellow")

        for y in range(self.maze.height):
            print("", end="\n")
            for x in range(self.maze.width):

                position = Position(x, y)
                if position == self.maze.hero.position:
                    char, color = HERO, C__HERO
                elif position in self.maze:
                    if position == self.maze.exit:
                        char, color = EXIT, C__EXIT
                    else:
                        char, color = PASSAGE, C__PASSAGE
                else:
                    char, color = WALL, C__WALL
                cprint(char, color, end="")

        print("\n")
        for message, level in messages.get():
            color = C__LEVELS[level]
            cprint(message, color)

        print("\n")
        self.print_the_help()

        cprint(f"\n\nEnter a key:", C__LEVELS[1], end=" ")

    def print_the_help(self):
        """Print the help message."""
        for key, value in messages.help.items():
            cprint(key, "yellow", end="")
            print(":", end=" ")
            cprint(value, "cyan")
