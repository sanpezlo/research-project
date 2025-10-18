from questionary import select

from .menu import Menu


class MainMenu(Menu):
    def __init__(self):
        question = select(
            "What do you want to do?",
            choices=["Generate dataframe", "Run tests", "Exit"],
            use_shortcuts=True,
        )
        super().__init__(question)

    def handle_choice(self, answer: str) -> None:
        if answer == "Generate dataframe":
            from .dataframe import DataframeMenu

            DataframeMenu().show()
        elif answer == "Run tests":
            from .tests_menu import TestsMenu

            TestsMenu().show()
