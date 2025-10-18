from questionary import select

from research_project.tests import Tests

from .menu import Menu


class TestsMenu(Menu):
    def __init__(self):
        question = select(
            "To which problem do you want to run the tests?",
            choices=["All", "Specific Problem", "Back"],
            use_shortcuts=True,
        )
        super().__init__(question)

    def handle_choice(self, answer: str) -> None:
        if answer == "All":
            Tests().run()
        elif answer == "Specific Problem":
            Tests(id=4).run()
        elif answer == "Back":
            from .main_menu import MainMenu

            return MainMenu().show()
