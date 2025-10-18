import re

from typing_extensions import Self, TypedDict


class Group(TypedDict):
    initial: list[str]
    transformation: list[str]
    final: list[str]
    js: list[str]

    def is_empty(self) -> bool:
        if (
            not self["js"]
            and not self["initial"]
            and not self["transformation"]
            and not self["final"]
        ):
            return True
        return False

    def join(self, other: Self) -> Self:
        result = self.copy()

        if Group.is_empty(result) or Group.is_empty(other):
            return Group(initial=[], transformation=[], final=[], js=[])

        if other["initial"]:
            result["initial"] = other["initial"]
        if other["transformation"]:
            result["transformation"] = other["transformation"]
        if other["final"]:
            result["final"] = other["final"]
        if other["js"]:
            result["js"] = other["js"]

        return result

    def combine(self) -> list[str]:
        if (
            not self["js"]
            or not self["initial"]
            or not self["transformation"]
            or not self["final"]
        ):
            return []

        answers = self["js"]
        answers = Group.combine_initial(answers, self["initial"])
        answers = Group.combine_transformation(answers, self["transformation"])
        answers = Group.combine_final(answers, self["final"])

        return answers

    def combine_initial(answers: list[str], initials: list[str]) -> list[str]:
        if not initials:
            return answers

        combinations = []
        for answer in answers:
            i = re.search(r"(function\s+\w+\s*\([^)]*\)\s*{)", answer).end()
            for initial in initials:
                function = answer[: i + 1]
                body = answer[i + 1 :]
                combinations.append(function + initial + body)
        return combinations

    def combine_transformation(
        answers: list[str], transformations: list[str]
    ) -> list[str]:
        if not transformations:
            return answers

        combinations = []
        for answer in answers:
            i = re.search(r"while\s*\(.*\)\s*\{", answer).end()

            for transformation in transformations:
                body = answer[: i + 1]
                end = answer[i + 1 :]
                combinations.append(body + transformation + end)

        return combinations

    def combine_final(answers: list[str], finals: list[str]) -> list[str]:
        if not finals:
            return answers

        combinations = []
        for answer in answers:
            i = re.search(r"while\s*\(.*\)\s*\{", answer).end()
            brace = 1

            while i < len(answer) and brace > 0:
                if answer[i] == "{":
                    brace += 1
                elif answer[i] == "}":
                    brace -= 1
                i += 1

            for final in finals:
                body = answer[: i + 1]
                end = answer[i + 1 :]
                combinations.append(body + final + end)

        return combinations
