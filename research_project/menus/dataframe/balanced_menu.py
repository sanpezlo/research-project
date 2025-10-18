from questionary import Validator, ValidationError, text

from research_project.menus import Menu
from research_project.types import DataframeConfig
from research_project.dataframe import Dataframe


class BalancedValidator(Validator):
    def validate(self, document):
        if document.text.lower() == "infinite":
            return

        if not document.text.isdigit() or int(document.text) <= 0:
            raise ValidationError(
                message='Please enter a valid number or "Infinite"',
                cursor_position=len(document.text),
            )


class BalancedDataframeMenu(Menu):
    config: DataframeConfig

    def __init__(self, config: DataframeConfig):
        self.config = config
        question = text(
            "What is the maximum amount of data per tag?",
            default="Infinite",
            validate=BalancedValidator,
        )
        super().__init__(question)

    def handle_choice(self, answer) -> None:
        self.config = DataframeConfig(
            balanced=True,
            max=int(answer) if answer.lower() != "infinite" else None,
            seed=int(self.config["seed"]),
        )

        Dataframe(config=self.config).write()
