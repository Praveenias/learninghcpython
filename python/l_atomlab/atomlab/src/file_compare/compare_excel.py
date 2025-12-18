import pandas as pd
import json

def checkExcel(excelv2,excelv3,limit):
  # excelv2.set_index(uniquefds, inplace=True)
  # excelv3.set_index(uniquefds, inplace=True)

  diff = pd.DataFrame()
  missing = pd.DataFrame(columns=uniquefds)

  for i in range(limit):
    unique_combination = excelv2.iloc[i][uniquefds]
    matching_row_df2 = excelv3[(excelv3[uniquefds] == unique_combination.values).all(axis=1)]
   

    
    if not matching_row_df2.empty:

      row_df1 = excelv2.iloc[i][comparisonfds]
      row_df2 = matching_row_df2.iloc[0][comparisonfds]
      
      differences = row_df1.compare(row_df2, keep_shape=True, keep_equal=True,align_axis=0)
      differences = row_df1[row_df1.notna() | row_df2.notna()].compare(row_df2[row_df1.notna() | row_df2.notna()])
      for uq in uniquefds:
        differences[uq] = unique_combination[uq]

      if len(differences) > 0:
        diff = pd.concat([diff,differences])   
         
    else:
      missing.loc[i] = {uq:unique_combination[uq] for uq in uniquefds}
    if i%4000 == 0:
      print(f"Row completed : {i}")

  diff.to_excel('compared.xlsx')
  if len(missing) > 0:
    missing.to_excel('missing.xlsx')
    print("Missing Component in v3 will be saved as missing.xlsx")


if __name__ == '__main__':
  print("Started..")
  ipArg = {}
  with open('setup.json', 'r') as file:
    ipArg = json.load(file)

  limit=ipArg['rowLimit'] # set this as 0, to compare whole excel
  uniquefds = ipArg['uniqueFds']
  comparisonfds =ipArg['ComparisionFds']

  excelv2 = pd.read_excel(ipArg['v2filePath'])
  print("v2 excel loaded")

  excelv3 = pd.read_excel(ipArg['v3filePath'])
  print("v3 excel loaded")

  # for iom manufacturer name and part number will be differ .
  excelv3 = excelv3.rename(columns={
    'Manufacturer Name':'Mapped Manufacturer Name',
  'Manufacturer Part Number':'Mapped Manufacturer PartNumber',
  'Mapped Manufacturer Name':'Manufacturer Name',
  'Mapped Manufacturer Part Number':'Manufacturer Part Number'})
  
  
  if limit != 0:
    excelv2 = excelv2.head(limit)

  limit = len(excelv2) if limit == 0 else limit
  print("Row count : ",limit)


  missingColumnsv2 = [col for col in uniquefds+comparisonfds if col not in excelv2.columns]
  missingColumnsv3 = [col for col in uniquefds+comparisonfds if col not in excelv3.columns]
  if missingColumnsv2:
    print("V2 Excel Header Missing",missingColumnsv2)
  elif missingColumnsv3:
    print("V3 Excel Header Missing",missingColumnsv3)
  else:
    excelv2 = excelv2[uniquefds + comparisonfds]
    excelv3 = excelv3[uniquefds + comparisonfds]
    checkExcel(
      excelv2=excelv2,
      excelv3=excelv3,
      limit=limit
    )
    print("Difference WIll be Saved as compared.xlsx")
