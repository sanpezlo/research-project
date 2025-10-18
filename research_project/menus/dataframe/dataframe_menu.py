from questionary import form, text, confirm

from research_project.menus import Menu
from research_project.types import DataframeConfig
from research_project.dataframe import Dataframe


class DataframeMenu(Menu):
    def __init__(self):
        question = form(
            seed=text(
                "What is the seed for the random number generator?",
                default="2025",
                validate=lambda x: True
                if x.isdigit()
                else "Please enter a valid number",
            ),
            balanced=confirm("Do you want to generate a balanced dataframe?"),
        )
        super().__init__(question)

    def handle_choice(self, answer) -> None:
        if answer["balanced"]:
            from .balanced_menu import BalancedDataframeMenu

            BalancedDataframeMenu(config=answer).show()
        else:
            config = DataframeConfig(seed=int(answer["seed"]), balanced=False, max=None)
            Dataframe(config=config).write()
