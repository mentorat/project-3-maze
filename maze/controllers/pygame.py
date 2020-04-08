"""Pygame controller module."""

import time

import pygame

from typing import Tuple

from maze.models.game import Game


class Keyboard:
    """Pygame Keyboard class."""

    def __init__(self, game: Game):
        """Init."""
        self.game: Game = game
        self.mapping = {
            pygame.K_z: "down",
            pygame.K_z: "up",
            pygame.K_q: "left",
            pygame.K_r: "right",
            pygame.KEYDOWN: "down",
            pygame.KEYUP: "up",
            pygame.K_RIGHT: "right",
            pygame.K_LEFT: "left",
        }

    def wait_for_command(self) -> Tuple[str, int]:
        """Wait for a pygame command."""
        command = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                command = "quit"
            if event.type == pygame.KEYDOWN:
                command = self.mapping.get(event.key, "")

        return (command, 1)
