import pandas as pd
import re

df = pd.read_excel('Manufacturer.xlsx',sheet_name='Data')



def normalize_string(raw_string:str,remove_suffix:bool=False)->str:
    suffixL = ['inc', 'corp', 'corporation', 'llc', 'ltd', 'limited']
    if (not raw_string):
      return None
    tmp_s = str(raw_string).strip()
    tmp_s = re.sub('[^\w]+', ' ',tmp_s)
    tmp_l = tmp_s.lower().split()
    if (tmp_l[-1] in suffixL) and remove_suffix: del tmp_l[-1]
    res = '_'.join(tmp_l)
    return res

header_row = df.iloc[0]
df = df[1:]
df.columns  = list(map(normalize_string, list(header_row)))
print(df)


# mandatory_column  = ["name","category","alert_mechanism"]

# df = df[mandatory_column]
# df['normalized_name'] = df['name'].map(lambda x :normalize_string(x,True))
df.to_excel('1.xlsx')
