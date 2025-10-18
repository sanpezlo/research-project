from typing import TypedDict

from research_project.utils import transpile, clean, read_problem, read_questions

from .tag import TAGS, Tag


class Problem(TypedDict):
    id: int
    questions: list[str]
    answers: dict[Tag, list[str]]

    def read(id: int, clean_data: bool = True):
        problem: Problem = {"id": id, "questions": read_questions(id), "answers": {}}

        read = read_problem(id)
        for t in range(TAGS):
            tag = Tag(t)
            combinations = transpile(read, tag)
            if clean_data:
                problem["answers"][tag] = clean(combinations)
            else:
                problem["answers"][tag] = combinations

        return problem
