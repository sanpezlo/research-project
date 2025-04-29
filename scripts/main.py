import pandas as pd
from md import read
from gen_code import gen
from gen_tests import read_lines, gen_tests, write_lines
import os
import subprocess
import polars as pl
from typing import TypedDict
from tag import TAGS, Tag
from group import Group
from read import read_problem, read_questions


PROBLEMS = 29


class Problem(TypedDict):
    id: int
    questions: list[str]
    answers: dict[Tag, list[str]]


def dataset(problems: list[Problem]):
    rows = []
    for problem in problems:
        for tag, ans_list in problem["answers"].items():
            for ans in ans_list:
                rows.append({
                    "problem_id": problem["id"],
                    "question": problem["questions"][0],
                    "answer": ans,
                    "tag": tag
                })
    dataframe(rows)


def dataframe(rows):
    df = pl.DataFrame(rows).unique(
        subset=["problem_id", "question", "answer", "tag"])

    balanced_chunks = []
    for pid in df["problem_id"].unique().to_list():
        sub = df.filter(pl.col("problem_id") == pid)
        counts = {
            et: sub.filter(pl.col("tag") == et).height
            for et in sub["tag"].unique().to_list()
        }
        min_count = min(counts.values())
        print(counts.values(), min_count)
        for et in counts:
            group = sub.filter(pl.col("tag") == et)
            sampled = group.sample(n=min_count, shuffle=True)
            balanced_chunks.append(sampled)

    balanced_df = pl.concat(
        balanced_chunks).with_row_index(name="id", offset=1)

    balanced_df.write_csv(
        f"/workspaces/research-project/data/xlsx/balanced.csv")


def transpile(problem: dict[Tag, list[list[Group]]], tag: Tag) -> list[str]:
    flags = [flag for flag in Tag if flag in tag]
    combinations: list[str] = []
    if (len(flags) < 2):
        for block in problem[tag]:
            for i, group in enumerate(block):
                result = Group.join(problem[Tag.CORRECT][0][i], group)
                combinations += Group.combine(result)
    else:
        before = [problem[Tag.CORRECT][0]]
        for flag in flags:
            temp_tag: list[list[Group]] = []
            for before_block in before:
                for block in problem[flag]:
                    temp_block: list[Group] = []
                    for i, group in enumerate(block):
                        temp_block.append(Group.join(before_block[i], group))
                    temp_tag.append(temp_block)
            before = temp_tag
        for block in before:
            for i, group in enumerate(block):
                combinations += Group.combine(group)
    return combinations


def gen_dataframe():
    problems: list[Problem] = []
    for i in range(1, PROBLEMS + 1):
        problem: Problem = {
            "id": i,
            "questions": read_questions(i),
            "answers": {}
        }
        read = read_problem(i)
        for t in range(TAGS):
            tag = Tag(t)
            combinations = transpile(read, tag)
            problem["answers"][tag] = combinations
        problems.append(problem)
    dataset(problems)


def write_tests(id_problem, type):
    md = read(
        f"/workspaces/research-project/data/problems/{id_problem}/{type}.md")
    tests_lines = read_lines(
        f"/workspaces/research-project/tests/{id_problem}/{"tests" if type == "correct" else "error"}.js")
    tests = gen_tests(tests_lines, md["codes"])
    write_lines(
        f"/workspaces/research-project/tests/{id_problem}/_{type}.js", tests)


def run_tests(id_problem, type):
    write_tests(id_problem, type)

    correct = subprocess.Popen(
        ["node", f"/workspaces/research-project/tests/{id_problem}/_{type}.js"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read().decode().strip()

    if correct == "":
        return f"{type}: All tests passed."
    else:
        return f"{type}\n" + correct


result = None


def window(display, choices):
    global result

    while True:
        os.system('cls' if os.name == 'nt' else "printf '\033c'")

        if result:
            print(result)
            result = None

        print("\n".join([line.strip()
              for line in display.splitlines()]).strip())

        choice = input("Enter your choice: ")

        if choice == "q":
            return
        elif choices(choice):
            continue
        else:
            result = "Error: Invalid choice."


def main():
    display = """
    ---- Research project ----
    | 1. Generate dataframe  |
    | 2. Run tests           |
    | q. Quit                |
    --------------------------
    """

    def choices(choice):
        if choice == "1":
            gen_dataframe()
            return True
        elif choice == "2":
            window_tests()
            return True
        else:
            return False

    window(display, choices)


def window_tests():
    display = """
    ---- Run tests ----
    | 1-n. Run by id  |
    | all. Run all    |
    | q.   Back       |
    -------------------
"""

    def choices(choice):
        if choice == "all":
            return True
        elif choice.isnumeric():
            window_tests_by_id(int(choice))
            return True
        else:
            return False

    window(display, choices)


def window_tests_by_id(id):
    id = f"{id:02d}"

    display = f"""
    ---- Run tests {id} ----
    | r. Repit           |
    | q. Back            |
    ----------------------
"""

    def result():
        global result
        tests = []
        tests.append(run_tests(id, "correct"))
        tests.append(run_tests(id, "initial"))
        tests.append(run_tests(id, "transformation"))
        tests.append(run_tests(id, "final"))
        result = "\n".join(tests)

    def choices(choice):
        if choice == "r":
            result()
            return True
        else:
            return False

    result()
    window(display, choices)


if __name__ == "__main__":
    main()
