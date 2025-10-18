import polars as pl

from research_project.types import DataframeConfig, RowDataframe, Problem


class Dataframe:
    config: DataframeConfig
    problems: list[Problem]

    def __init__(self, config: DataframeConfig):
        PROBLEMS = 29
        self.config = config

        self.problems = []
        for i in range(1, PROBLEMS + 1):
            problem = Problem.read(i)
            self.problems.append(problem)

    def write(self):
        rows: list[RowDataframe] = []
        for problem in self.problems:
            for tag, ans_list in problem["answers"].items():
                for ans in ans_list:
                    rows.append(
                        {
                            "problem_id": problem["id"],
                            # TODO: add random questions, not only first
                            "question": problem["questions"][0],
                            "answer": ans,
                            "tag": tag,
                        }
                    )

        df = pl.DataFrame(rows).unique(
            subset=["problem_id", "answer", "tag"], maintain_order=True
        )
        df_path = "/workspaces/research-project/data/xlsx/dataframe"

        if self.config["balanced"]:
            df = self.balanced_dataframe(df)
            df_path += "_balanced"
        else:
            df = df.with_row_index(name="id", offset=1)

        if self.config["max"] is not None:
            df_path += f"_{self.config['max']}"

        df.write_csv(f"{df_path}.csv")

    def balanced_dataframe(self, df: pl.DataFrame) -> pl.DataFrame:
        balanced_chunks: list[pl.DataFrame] = []
        for pid in df["problem_id"].unique().to_list():
            sub = df.filter(pl.col("problem_id") == pid)
            counts = {
                et: sub.filter(pl.col("tag") == et).height
                for et in sub["tag"].unique().to_list()
            }
            max_count = min(counts.values())
            if self.config["max"] is not None:
                max_count = min(max_count, self.config["max"])
            for et in counts:
                group = sub.filter(pl.col("tag") == et)
                sampled = group.sample(n=max_count, seed=self.config["seed"])
                balanced_chunks.append(sampled)

        return pl.concat(balanced_chunks).with_row_index(name="id", offset=1)


# def gen_dataframe(config: DataframeConfig):
#     problems: list[Problem] = []
#     for i in range(1, PROBLEMS + 1):
#         problem: Problem = {"id": i, "questions": read_questions(i), "answers": {}}
#         read = read_problem(i)
#         for t in range(TAGS):
#             tag = Tag(t)
#             combinations = transpile(read, tag)
#             # TODO: si es test, descomentar esta linea
#             # problem["answers"][tag] = combinations
#             problem["answers"][tag] = clear(combinations)
#         problems.append(problem)
#     write_dataframe(config, problems)


# def clear(combinations: list[str]):
#     result = []
#     for combination in combinations:
#         if re.search(r"#\(ignore-test\)", combination) is not None:
#             clean = re.sub(r"#\(ignore-test\)", "", combination, flags=re.MULTILINE)
#             clean = re.sub(r"\n\s*\n", "\n", clean)
#             result.append(clean)
#             continue
#         else:
#             result.append(combination)
#     return result


# def write_dataframe(config: DataframeConfig, problems: list[Problem]):
#     rows: list[RowDataframe] = []
#     for problem in problems:
#         for tag, ans_list in problem["answers"].items():
#             for ans in ans_list:
#                 rows.append(
#                     {
#                         "problem_id": problem["id"],
#                         # TODO: add random questions, not only first
#                         "question": problem["questions"][0],
#                         "answer": ans,
#                         "tag": tag,
#                     }
#                 )

#     df = pl.DataFrame(rows).unique(
#         subset=["problem_id", "answer", "tag"], maintain_order=True
#     )
#     df_path = "/workspaces/research-project/data/xlsx/dataframe"

#     if config["balanced"]:
#         df = balanced_dataframe(config, df)
#         df_path += "_balanced"

#     if config["max"] is not None:
#         df_path += f"_{config['max']}"

#     df.write_csv(f"{df_path}.csv")

#     # TODO: test
#     # write_file(problems)
#     # df = pl.DataFrame(rows).write_json(
#     #     f"/workspaces/research-project/data/xlsx/problems_{1}.json"
#     # )


# # TODO: test
# def write_file(problems: list[Problem]):
#     for problem in problems:
#         for tag, answers_list in problem["answers"].items():
#             test_type = "tests" if tag == Tag.CORRECT else "error"
#             tests_lines = read_lines(
#                 f"/workspaces/research-project/tests/04/{test_type}.js"
#             )
#             tests = gen_tests(tests_lines, answers_list)
#             write_lines(
#                 f"/workspaces/research-project/tests/04/__{tag.__str__().lower()}.js",
#                 tests,
#             )


# def balanced_dataframe(config: DataframeConfig, df: pl.DataFrame) -> pl.DataFrame:
#     balanced_chunks: list[pl.DataFrame] = []
#     for pid in df["problem_id"].unique().to_list():
#         sub = df.filter(pl.col("problem_id") == pid)
#         counts = {
#             et: sub.filter(pl.col("tag") == et).height
#             for et in sub["tag"].unique().to_list()
#         }
#         max_count = min(counts.values())
#         if config["max"] is not None:
#             max_count = min(max_count, config["max"])
#         for et in counts:
#             group = sub.filter(pl.col("tag") == et)
#             sampled = group.sample(n=max_count, seed=config["seed"])
#             balanced_chunks.append(sampled)

#     return pl.concat(balanced_chunks).with_row_index(name="id", offset=1)
