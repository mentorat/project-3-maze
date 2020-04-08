"""Main app."""

from maze.application import Application

if __name__ == "__main__":
    modes = {"1": "cli", "2": "pygame"}
    mode = ""

    print("1 - Console")
    print("2 - Pygame")
    choice = input("Select a mode (1 or 2): ")
    mode = modes.get(choice, "")

    if not mode:
        print("Wrong input. Mode set to 'Console'.")
        mode = "cli"
    else:
        print(f"Mode set to '{mode}'.")

    app = Application(mode)
    app.run()
