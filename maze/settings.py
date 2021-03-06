"""Setting module."""

from pathlib import Path

# CHARACTERS

START = "d"
EXIT = "e"
PASSAGE = "."
WALL = "#"
HERO = "I"
ITEMS = {"tube": "t", "gum": "g", "goo": "o"}

# COLORS

C__START = "blue"
C__EXIT = "green"
C__PASSAGE = "grey"
C__WALL = "blue"
C__HERO = "green"
C__LEVELS = {0: "green", 1: "yellow", 2: "red"}
C_ITEMS = "red"

# PATHS

BASE_DIR = Path(".")
MAZE_DIR = BASE_DIR / "maze"
DATA_DIR = MAZE_DIR / "data"
MAP_DIR = DATA_DIR / "maps"
TILESET_DIR = DATA_DIR / "tileset"

# DATA FILES

MAP_LEVEL_1 = str(MAP_DIR / "level-1.txt")

TILESET_1 = str(TILESET_DIR / "tileset-1.png")


# PYGAME STUFF

TILESETS = {1: (TILESET_1, 32)}
