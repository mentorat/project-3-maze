"""CLI view."""

import os

from termcolor import cprint
from colorama import init as colorinit

from maze.settings import (
    WALL,
    PASSAGE,
    EXIT,
    HERO,
    ITEMS,
    C__WALL,
    C__PASSAGE,
    C__EXIT,
    C__HERO,
    C__LEVELS,
    C_ITEMS,
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
        self.hero = game.hero
        self.turns = 0

    def refresh(self):
        """Display the map."""
        os.system("cls" if os.name == "nt" else "clear")
        self.print_header()
        self.print_maze()
        self.print_bag()
        self.print_messages()
        self.print_the_help()
        self.print_input()

    def print_header(self):
        """Print the header."""
        self.turns += 1
        print("\n")
        cprint(" MAZE ".center(self.maze.width, "-"), "yellow")
        cprint(f" Turn {self.turns} ".center(self.maze.width, "-"), "yellow")

    def print_maze(self):
        """Print the maze."""
        for y in range(self.maze.height):
            print("", end="\n")
            for x in range(self.maze.width):

                position = Position(x, y)
                if position == self.maze.hero.position:
                    char, color = HERO, C__HERO
                elif position in self.maze.items:
                    char, color = ITEMS[self.maze.items[position]], C_ITEMS
                elif position in self.maze:
                    if position == self.maze.exit:
                        char, color = EXIT, C__EXIT
                    else:
                        char, color = PASSAGE, C__PASSAGE
                else:
                    char, color = WALL, C__WALL
                cprint(char, color, end="")

    def print_bag(self):
        """Print the player's bag."""
        print("\n")
        for name in ITEMS:
            has_item = "x" if name in self.hero.items else " "
            cprint(f"[{has_item}] {name}", "yellow", end=" ")

    def print_messages(self):
        """Print the messages."""
        print("\n")
        for message, level in messages.get():
            color = C__LEVELS[level]
            cprint(message, color)

    def print_the_help(self):
        """Print the help message."""
        print("\n")
        for key, value in messages.help.items():
            cprint(key, "yellow", end="")
            print(":", end=" ")
            cprint(value, "cyan")

    def print_input(self):
        """Print the input text."""
        cprint(f"\n\nEnter a key:", C__LEVELS[1], end=" ")
