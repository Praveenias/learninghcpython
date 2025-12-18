import pandas as pd

file_1 = './example/set-1/BOM_1.xlsx'

file_2 = './example/set-1/BOM_2.xlsx'

df1 = pd.read_excel(file_1)

df2 = pd.read_excel(file_2)

print(df1.compare(df2))