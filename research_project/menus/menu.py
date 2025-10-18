from questionary import Question


class Menu:
    def __init__(self, question: Question):
        self.question = question

    def handle_choice(self, answer):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def show(self):
        answer = self.question.ask()
        if answer == "Exit" or answer is None:
            return
        return self.handle_choice(answer)
