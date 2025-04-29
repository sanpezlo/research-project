from typing import Self, TypedDict
import re


class Group(TypedDict):
    initial: list[str]
    transformation: list[str]
    final: list[str]
    js: list[str]

    def join(self, other: Self) -> Self:
        result = self.copy()

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
        answers = self["js"]
        answers = combine_initial(answers, self["initial"])
        answers = combine_transformation(answers, self["transformation"])
        answers = combine_final(answers, self["final"])

        return answers


def combine_initial(answers, initials):
    if not initials:
        return answers

    combinations = []
    for answer in answers:
        i = re.search(r'(function\s+\w+\s*\([^)]*\)\s*{)', answer).end()
        for initial in initials:
            function = answer[:i + 1]
            body = answer[i + 1:]
            combinations.append(function + initial + body)
    return combinations


def combine_transformation(answers, transformations):
    if not transformations:
        return answers

    combinations = []
    for answer in answers:
        i = re.search(r'while\s*\(.*\)\s*\{', answer).end()

        for transformation in transformations:
            body = answer[:i + 1]
            end = answer[i + 1:]
            combinations.append(body + transformation + end)

    return combinations


def combine_final(answers, finals):
    if not finals:
        return answers

    combinations = []
    for answer in answers:
        i = re.search(r'while\s*\(.*\)\s*\{', answer).end()
        brace = 1

        while i < len(answer) and brace > 0:
            if answer[i] == '{':
                brace += 1
            elif answer[i] == '}':
                brace -= 1
            i += 1

        for final in finals:
            body = answer[:i + 1]
            end = answer[i + 1:]
            combinations.append(body + final + end)

    return combinations
