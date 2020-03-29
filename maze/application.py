"""Application module."""

from maze.models.game import Game
from maze.views.cli import Display
from maze.controllers.cli import Keyboard


class Application:
    """Classe contrôlant la boucle de jeu principale."""

    def __init__(self):
        """Initilise l'application."""
        self.running = True

        self.game = Game()

        self.display = Display(self.game)
        self.keyboard = Keyboard(self.game)

    def run(self) -> None:
        """Démarre l'interface de l'application."""
        while self.running:
            self.display.refresh()

            if self.game.hero.found_exit():
                exit_message = "Exit found ! You won."
                break

            command, repeat = self.keyboard.wait_for_command()
            self.game.update(command, repeat)

            if command == "quit":
                exit_message = "Game closed."
                self.running = False

        print(exit_message)
