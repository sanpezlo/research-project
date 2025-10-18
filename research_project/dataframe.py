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
