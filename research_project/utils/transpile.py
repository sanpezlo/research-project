import re

from research_project.types.group import Group
from research_project.types.tag import Tag


def transpile(problem: dict[Tag, list[list[Group]]], tag: Tag) -> list[str]:
    flags = [flag for flag in Tag if flag in tag]
    combinations: list[str] = []
    if len(flags) <= 2:
        for block in problem[tag]:
            for i, group in enumerate(block):
                result = Group.join(problem[Tag.CORRECT][0][i], group)
                combinations += Group.combine(result)
    else:
        before = [problem[Tag.CORRECT][0]]
        for flag in flags:
            if flag == Tag.CORRECT:
                continue

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


def clean(combinations: list[str]) -> list[str]:
    result = []
    for combination in combinations:
        if re.search(r"#\(ignore-test\)", combination) is not None:
            clean = re.sub(r"#\(ignore-test\)", "", combination, flags=re.MULTILINE)
            clean = re.sub(r"\n\s*\n", "\n", clean)
            result.append(clean)
            continue
        else:
            result.append(combination)
    return result


def change_functio_name(code: str, new_name: str):
    return re.sub(r"\bfunction\s+(\w+)\s*\(", f"function {new_name}(", code)


# NOTE: YA NO SE USA
# Antes pensaba en generar datos expandiendo expresiones, como por ejemplo:
# "a++;" -> "a = a + 1;"
# y cambiando nombres de funciones
def gen_more(functions: list[str], new_functio_name: str):
    new_functions = []

    for function in functions:
        clean = re.sub(r"#\(ignore-test\)", "", function, flags=re.MULTILINE)
        clean = re.sub(r"\n\s*\n", "\n", clean)
        new_functions.append(clean)

    new_functions += [expand_code(function) for function in new_functions]

    # new_functions += [change_functio_name(function, new_functio_name)
    #                   for function in new_functions]

    return new_functions


def expand_operator(match):
    if match.group(2) == "++":
        return f"{match.group(1)} = {match.group(1)} + 1;"
    elif match.group(2) == "--":
        return f"{match.group(1)} = {match.group(1)} - 1;"
    elif match.group(2) == "+=":
        return f"{match.group(1)} = {match.group(1)} + {match.group(3)}"
    elif match.group(2) == "-=":
        return f"{match.group(1)} = {match.group(1)} - {match.group(3)}"
    elif match.group(2) == "*=":
        return f"{match.group(1)} = {match.group(1)} * {match.group(3)}"
    elif match.group(2) == "/=":
        return f"{match.group(1)} = {match.group(1)} / {match.group(3)}"
    elif match.group(2) == "++":
        return f"{match.group(1)} = {match.group(1)} + 1;"
    elif match.group(2) == "--":
        return f"{match.group(1)} = {match.group(1)} - 1;"

    return match.group(0)


def expand_code(code: str):
    expanded_code = re.sub(
        r"\b(\w+)\s*(\+=|-=|\*=|/=)\s*([\w\d_]+)\b", expand_operator, code
    )
    return re.sub(r"\b(\w+)\s*(\+\+|--);", expand_operator, expanded_code)
