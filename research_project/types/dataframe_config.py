from typing import TypedDict


class DataframeConfig(TypedDict):
    balanced: bool
    max: int
    seed: int

    def __init__(self, balanced: bool, max: int, seed: int):
        self.balanced = balanced
        self.max = max
        self.seed = seed
