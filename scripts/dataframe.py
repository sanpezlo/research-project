import polars as pl
import re
from typing import TypedDict
from tag import TAGS, Tag
from transpile import transpile
from read import read_problem, read_questions

PROBLEMS = 29


class Problem(TypedDict):
    id: int
    questions: list[str]
    answers: dict[Tag, list[str]]


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
            problem["answers"][tag] = clear(combinations)
        problems.append(problem)
    dataframe(problems)


def clear(combinations: list[str]):
    result = []
    for combination in combinations:
        if re.search(r'#\(ignore-test\)', combination) is not None:
            clean = re.sub(
                r'#\(ignore-test\)', '', combination, flags=re.MULTILINE)
            clean = re.sub(r'\n\s*\n', '\n', clean)
            result.append(clean)
            continue
        else:
            result.append(combination)
    return result


def dataframe(problems: list[Problem]):
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
    balanced_dataframe(rows)


def balanced_dataframe(rows):
    df = pl.DataFrame(rows).unique(
        subset=["problem_id", "answer", "tag"])

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
