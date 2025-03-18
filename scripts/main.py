import pandas as pd
from md import read
from gen_code import gen

md = read("/workspaces/research-project/data/correct/problem_1.md")

codes = gen(md["codes"], "test")

df = pd.DataFrame(codes, columns=["code"])
df.insert(0, "problem", md["problem"])

df.to_excel("/workspaces/research-project/data/correct/problem_1.xlsx")