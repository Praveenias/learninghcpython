import pandas as pd
import random
from faker import Faker

manufacturer_choises = ['murata','dell','hp','samsung']

columns = ['name','category','type','alert_mechanism','email']
data_dict = {column_name:[] for column_name in columns}
manufacturer_df = pd.DataFrame(data_dict,columns=columns)
company_name = []
fake = Faker()
for _ in range(10000):
  name = fake.unique.company()
  if name in company_name:
    print("duplicate",_)
    break
  company_name.append(name)
print('hit')

# for i in range(10):
#   dict_1 = {'name': random.choice(manufacturer_choises), 
#             'category': 'public', 
#             'type': 'manufacturer', 
#             'alert_mechanism': 'manual',
#             'email': 'ilensys@gmail.com'}
#   manufacturer_df =  manufacturer_df._append(dict_1,ignore_index=True)

# manufacturer_df.to_excel('manufacturer.xlsx',index=False)
