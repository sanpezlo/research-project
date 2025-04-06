import pandas as pd
from md import read
from gen_code import gen
from gen_tests import read_lines, gen_tests, write_lines


def dataframe(id_problem):
    md = read(
        f"/workspaces/research-project/data/problems/{id_problem}/correct.md")
    codes = gen(md["codes"], "test")
    df = pd.DataFrame(codes, columns=["code"])
    df.insert(0, "problem", md["problem"])
    df.to_excel(
        f"/workspaces/research-project/data/problems/{id_problem}/{id_problem}.xlsx")


def tests(id_problem, type):
    md = read(
        f"/workspaces/research-project/data/problems/{id_problem}/{type}.md")
    lines = read_lines(
        f"/workspaces/research-project/data/problems/{id_problem}/{"tests" if type == "correct" else "error"}.js")
    tests = gen_tests(lines, md["codes"])
    write_lines(
        f"/workspaces/research-project/data/problems/{id_problem}/{type}.js", tests)


tests("01", "initial")
