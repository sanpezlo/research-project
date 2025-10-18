from typing import TypedDict

from .tag import Tag


class RowDataframe(TypedDict):
    problem_id: int
    question: str
    answer: str
    tag: Tag
