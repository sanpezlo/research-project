from enum import IntFlag, auto

TAGS = 8


class Tag(IntFlag):
    CORRECT = 0
    INITIAL = auto()
    TRANSFORMATION = auto()
    FINAL = auto()
