from gen_code import change_functio_name
import re


def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def gen_tests(lines: list[str], functions: list[str]):
    new_lines = []
    for line in lines:
        if "function all() {" in line:
            for i, function in enumerate(functions):
                if re.search(r'#\(ignore-test\)', function) is not None:
                    clean = re.sub(
                        r'#\(ignore-test\)', '', function, flags=re.MULTILINE)
                    clean = re.sub(r'\n\s*\n', '\n', clean)
                    new_lines.append(change_functio_name(clean, f"f{i}"))
                    continue

                new_lines.append(change_functio_name(function, f"f{i}"))
                new_lines.append(f"\nfunctions.push(f{i});\n")
        new_lines.append(line)
    return new_lines


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(lines)
