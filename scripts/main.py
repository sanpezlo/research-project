import pandas as pd
from md import read
from gen_code import gen

id_problem = "02"

md = read(f"/workspaces/research-project/data/problems/{id_problem}/correct.md")

codes = gen(md["codes"], "test")

df = pd.DataFrame(codes, columns=["code"])
df.insert(0, "problem", md["problem"])

df.to_excel(f"/workspaces/research-project/data/problems/{id_problem}/{id_problem}.xlsx")