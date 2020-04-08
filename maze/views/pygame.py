"""CLI view."""

import os
import random
from typing import List

import pygame

from maze.settings import WALL, PASSAGE, EXIT, HERO, ITEMS, TILESETS
from maze.models.game import Game
from maze.models.position import Position
from maze.models.messages import messages


class Display:
    """Pygame view class."""

    def __init__(self, game: Game):
        """Init."""
        pygame.init()

        self.game = game
        self.maze = game.maze
        self.hero = game.hero
        self.turns = 0

        tileset_path, case_len = TILESETS[1]
        self.pixels = case_len
        self.window_width = self.maze.width * case_len
        self.window_height = self.maze.height * case_len
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.tileset = self.load_tileset(tileset_path, case_len)

        self.images = {}

    def load_tileset(self, tileset_path: str, pixels: int) -> list:
        """Load a given tileset.

        Returns:
            list: a list of lists of Surfaces.
        """
        image = pygame.image.load(tileset_path).convert()
        image_width, image_height = image.get_size()

        tileset = []
        for tile_x in range(0, image_width // pixels):
            line: List[pygame.Surface] = []
            tileset.append(line)
            for tile_y in range(0, image_height // pixels):
                rect = (tile_x * pixels, tile_y * pixels, pixels, pixels)
                line.append(image.subsurface(rect))
        return tileset

    def refresh(self) -> None:
        """Refresh the pygame window."""
        image = None
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                position = Position(x, y)

                if self.images.get(position):
                    image = self.images[position]

                elif position in self.maze:
                    if position == self.maze.exit:
                        image = self.tileset[13][0]
                        self.images[position] = image
                    else:
                        image = self.tileset[6][12]
                        self.images[position] = image
                else:
                    image = random.choice([self.tileset[9][6], self.tileset[10][6]])
                    self.images[position] = image
                # if position == self.maze.hero.position:
                #     image = "hero"
                # elif position in self.maze.items:
                #     image = "item x"
                self.screen.blit(image, (x * self.pixels, y * self.pixels))
        pygame.display.flip()
