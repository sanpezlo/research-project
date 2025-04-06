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


def gen(codes: list[str], new_functio_name: str):
    codes += [expand_code(code) for code in codes]
    # codes += [change_functio_name(code, new_functio_name) for code in codes]
    return codes
