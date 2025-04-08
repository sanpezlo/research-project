import re


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
        r"\b(\w+)\s*(\+=|-=|\*=|/=)\s*([\w\d_]+)\b", expand_operator, code)
    return re.sub(r"\b(\w+)\s*(\+\+|--);", expand_operator, expanded_code)


def change_functio_name(code: str, new_name: str):
    return re.sub(r"\bfunction\s+(\w+)\s*\(", f"function {new_name}(", code)


def gen(functions: list[str], new_functio_name: str):
    new_functions = []

    for function in functions:
        clean = re.sub(
            r'#\(ignore-test\)', '', function, flags=re.MULTILINE)
        clean = re.sub(r'\n\s*\n', '\n', clean)
        new_functions.append(clean)

    new_functions += [expand_code(function) for function in new_functions]

    # new_functions += [change_functio_name(function, new_functio_name)
    #                   for function in new_functions]

    return new_functions
