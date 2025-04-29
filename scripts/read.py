import re

from group import Group
from tag import Tag


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def read_lines(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def read_problem_by_tag(id: int, tag: Tag) -> list[list[Group]]:
    content = read_file(
        f"/workspaces/research-project/data/problems/{id:02d}/{tag.name.lower()}.md")

    blocks = []

    for block in [re.split(r"\n={3,}\n", block)
                  for block in re.split(r"\n={6,}\n", content)]:
        result = []
        for group in block:
            fragments = re.findall(r'```(\w+)\n(.*?)```', group, re.DOTALL)

            initials = []
            transformations = []
            finals = []
            js = []

            for lang, code in fragments:
                if lang == 'initial' and tag in Tag.INITIAL:
                    initials.append(code)
                elif lang == 'transformation' and tag in Tag.TRANSFORMATION:
                    transformations.append(code)
                elif lang == 'final' and tag in Tag.FINAL:
                    finals.append(code)
                elif lang == 'js' and tag in Tag.FINAL:
                    clean = re.sub(
                        r"(//.*?$)|(/\*[\s\S]*?\*/)", '', code, flags=re.MULTILINE)
                    clean = re.sub(r'\n\s*\n', '\n', clean)
                    js.append(clean)

            result.append({
                "initial": initials,
                "transformation": transformations,
                "final": finals,
                "js": js
            })

        blocks.append(result)

    return blocks


def read_problem(id: int):
    problem = {
        Tag.CORRECT: read_problem_by_tag(id, Tag.CORRECT)
    }

    for tag in Tag:
        problem[tag] = read_problem_by_tag(id, tag)

    return problem


def read_questions(id: int):
    content = read_lines(
        f"/workspaces/research-project/data/problems/{id:02d}/questions.md")

    return content
