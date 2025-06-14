from md import read
from gen_tests import read_lines, gen_tests, write_lines
import os
import subprocess
from dataframe import gen_dataframe


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
