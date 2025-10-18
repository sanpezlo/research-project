import re

from research_project.types import Problem, Tag, TAGS
from research_project.utils import read_lines
from research_project.utils import change_functio_name

import subprocess


class Tests:
    problems: list[Problem] = []

    def __init__(self, id: int = None):
        if id is None:
            PROBLEMS = 29

            for i in range(1, PROBLEMS + 1):
                problem = Problem.read(id=i, clean_data=False)
                self.problems.append(problem)
        else:
            self.problems = [Problem.read(id=id, clean_data=False)]

    def write(self):
        for problem in self.problems:
            # NOTE: Si se quiere escribir todos los test combinados
            # for t in range(TAGS):
            for tag in Tag:
                test_type = "tests" if tag == Tag.CORRECT else "error"

                tests_lines = read_lines(
                    f"/workspaces/research-project/tests/{problem['id']:02d}/{test_type}.js"
                )
                tests_file = gen_tests_file(tests_lines, problem["answers"][tag])

                tag_name = tag.__str__().lower().split(".")[1]

                write_lines(
                    f"/workspaces/research-project/tests/{problem['id']:02d}/_{tag_name}.js",
                    tests_file,
                )

    def run(self):
        self.write()

        for problem in self.problems:
            # NOTE: Si se quiere ejecutar todos los test combinados
            # for t in range(TAGS):
            for tag in Tag:
                tag_name = tag.__str__().lower().split(".")[1]
                correct = (
                    subprocess.Popen(
                        [
                            "node",
                            f"/workspaces/research-project/tests/{problem['id']:02d}/_{tag_name}.js",
                        ],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                    )
                    .stdout.read()
                    .decode()
                    .strip()
                )

                if not (correct == ""):
                    return f"{problem['id']:02d}{tag_name}\n" + correct


def gen_tests_file(base_file: list[str], answers: list[str]) -> list[str]:
    new_lines: list[str] = []
    for line in base_file:
        if "function all() {" in line:
            for i, function in enumerate(answers):
                if re.search(r"#\(ignore-test\)", function) is not None:
                    clean = re.sub(
                        r"#\(ignore-test\)", "", function, flags=re.MULTILINE
                    )
                    clean = re.sub(r"\n\s*\n", "\n", clean)
                    new_lines.append(change_functio_name(clean, f"f{i}"))
                    continue

                new_lines.append(change_functio_name(function, f"f{i}"))
                new_lines.append(f"\nfunctions.push(f{i});\n")
        new_lines.append(line)
    return new_lines


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(lines)
