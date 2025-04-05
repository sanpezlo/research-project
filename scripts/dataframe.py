import pandas as pd
from md import read
from gen_code import gen
from gen_tests import read_lines, gen_tests, write_lines

id_problem = "31"
problems=31

def dataframe():
    dataframe = pd.DataFrame()
    for i in range(problems):
        md = read(f"/workspaces/research-project/data/problems/{i+1:02d}/correct.md")  
        codes = gen(md["codes"], "test")
        df = pd.DataFrame(codes, columns=["code"])
        unique = pd.DataFrame(df["code"].unique(), columns=["code"])
        print(f"{i+1:02d}", unique.shape, df.shape)
        unique.insert(0, "problem", md["problem"])
        dataframe = pd.concat([dataframe, unique], ignore_index=True)
    dataframe.to_excel("/workspaces/research-project/data/xlsx/all.xlsx")

dataframe()