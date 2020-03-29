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

# PATHS

BASE_DIR = Path(".")
MAZE_DIR = BASE_DIR / "maze"
DATA_DIR = MAZE_DIR / "data"
MAP_DIR = DATA_DIR / "maps"

# DATA FILES

MAP_LEVEL_1 = str(MAP_DIR / "level-1.txt")
