
import requests

import pandas as pd
import json

params={'apikey':'ad55db2e-468c-44f6-a104-ea5b1cd2daf8'}

ip_json = {
 "SearchByPartRequest": {
    "mouserPartNumber": "ABC123048R",
    "partSearchOptions": ""
 }
}

df = pd.read_excel('praveen_input.xlsx')

for i in range(0,len(df),10):
  #print(df.iloc[i:i+10]['manufacturer_part_number'])
  data = {k:v for k, v in df.iloc[i:i+10,[1,0]].values}
  mpn_str = ' | '.join(data.keys())
  print(mpn_str)
  ip_json = {
 	"SearchByPartRequest": {
           "mouserPartNumber": mpn_str,
 	   "partSearchOptions": ""
 		}
  }
  res = requests.post('https://api.mouser.com/api/v1.0/search/partnumber', params=params,json=ip_json)
  json_data = res.json()
  print(json_data)
  #if res.status_code == 200 and not json_data['SearchResults']['Parts']:
	 # df.loc[i, "Availability"] = json_data['SearchResults']['Parts'][0]['Availability'],
  # df.loc[i, "LeadTime"] = json_data['SearchResults']['Parts'][0]['LeadTime']
  # df.loc[i, "LifecycleStatus"] = json_data['SearchResults']['Parts'][0]['LifecycleStatus'] 
# with open('get_from_json.json',encoding='utf-8',mode='r') as data:
#   json_data = json.load(data)
#   print(json_data['SearchResults']['Parts'][0]['Availability'],json_data['SearchResults']['Parts'][0]['LeadTime'],json_data['SearchResults']['Parts'][0]['LifecycleStatus'])
  
# print(df)

# res = requests.post('https://api.mouser.com/api/v1.0/search/partnumber', params=params,json=ip_json)
# print(res,res.json())
