"""Application module."""

from maze.models.game import Game
from maze import views
from maze import controllers


class Application:
    """Classe contrôlant la boucle de jeu principale.

    Args:
        mode (str): the game mode.
    """

    def __init__(self, mode: str):
        """Initialize the application."""
        self.running = True

        self.game = Game()
        self.hero = self.game.hero

        self.display = getattr(views, mode).Display(self.game)
        self.keyboard = getattr(controllers, mode).Keyboard(self.game)

    def run(self) -> None:
        """Démarre l'interface de l'application."""
        while self.running:
            self.display.refresh()

            if self.hero.found_exit():
                exit_message = "The exit was found !"
                if self.hero.found_all_items():
                    exit_message += " But you didn't find all the items ! You lost."
                else:
                    exit_message = " You also found all the items ! You won."
                break

            command, repeat = self.keyboard.wait_for_command()
            self.game.update(command, repeat)

            if command == "quit":
                exit_message = "Game closed."
                self.running = False

        try:
            import pygame

            pygame.quit()
        except ImportError:
            pass
        print(exit_message)
