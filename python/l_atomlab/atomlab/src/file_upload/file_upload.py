from pathlib import Path
import json,re
import openpyxl
import pandas as pd
from model import *
import numpy as np
import time

class UploadFile:
  
  def __init__(self)->None:
    config_file_name='test.json'
    self.config_data = self.get_config_data(config_file_name)
    if not self.config_data:
      return None
    self.db_schema = self.config_data['db_schema']
    #print(self.config_data)

  def get_config_data(self,file_name:str) ->dict:
    try:
      with open(Path(file_name),encoding='utf-8') as data:
        return json.load(data)
    except Exception as e:
      print(e)
      return {}
    
  def normalize_string(self,raw_string:str,remove_suffix:bool=False)->str:
    suffixL = ['inc', 'corp', 'corporation', 'llc', 'ltd', 'limited']
    if (not raw_string):
      return None
    tmp_s = str(raw_string).strip()
    tmp_s = re.sub('[^\w]+', ' ',tmp_s)
    tmp_l = tmp_s.lower().split()
    if (tmp_l[-1] in suffixL) and remove_suffix: del tmp_l[-1]
    res = '_'.join(tmp_l)
    return res
  
  def get_header_data(self,header_row:int,ws):
    """normalize the header column name"""
    header_names = [cell.value for cell in ws[header_row]]
    if None in header_names:
      none_index = header_names.index(None)
      header_names = header_names[:none_index]
    normalized_header = list(map(self.normalize_string, header_names))
    return normalized_header
  
  def clean_and_upload_file(self,file_info:dict,save_path = './public/')->Path:
    """ Change the file template format to db template and save in ./public folder"""

    db_schema = self.db_schema[file_info['file_type']]
    out_file_name = save_path+file_info['file_type']+str(int(time.time()))+'.xlsx'

    if file_info['file_type'] == 'manufacturer':
      df = pd.read_excel(file_info['file_path'],sheet_name=file_info['sheet_name'])
      header_row_data = list(df.columns)
      if file_info['header_row'] > 1:
        header_row_data = df.iloc[0]
        df = df[1:]
      df.columns  = list(map(self.normalize_string, list(header_row_data)))
      df = df[db_schema['mandatory_column']]
      df['normalized_name'] = df['name'].map(lambda x :self.normalize_string(x,True))
      df['status'] = 'approved'
      df['type'] = 'manufacturer'
      df.to_excel(out_file_name,index=False) 
    
    if file_info['file_type'] == 'master':
      df = pd.read_excel(file_info['file_path'],sheet_name=file_info['sheet_name'])
      header_row_data = list(df.columns)
      if file_info['header_row'] > 1:
        header_row_data = df.iloc[0]
        df = df[1:]
      df.columns  = list(map(self.normalize_string, list(header_row_data)))
      df = df[db_schema['mandatory_column']+db_schema['optional_columns']]
      df.rename(columns = db_schema['map_excel_2_db'],inplace=True)
      df.fillna('')
      df['manufacturer_partnumber'] = df['manufacturer_partnumber'].astype(str)
      df["check_date_life_cycle"] =  pd.to_datetime(df["check_date_life_cycle"], format="mixed").astype(str)
      df["check_date_compliance"] =  pd.to_datetime(df["check_date_compliance"], format="mixed").astype(str)
      df["check_date_stock"] =  pd.to_datetime(df["check_date_stock"], format="mixed").astype(str)
      df["check_date_regulatory"] =  pd.to_datetime(df["check_date_regulatory"], format="mixed").astype(str)
      df["rohs3_exemption_date"] =  pd.to_datetime(df["rohs3_exemption_date"], format="mixed").astype(str)
      df['status'] = 'approved'
      df['stock_details'] = df['stock_position'].map(lambda x : {'market':x})
      df['lead_time_details'] = df['supply_lead_time'].map(lambda x : {'market':x})
      df.to_excel(out_file_name,index=False)
  

    if file_info['file_type'] == 'bom':
      df = pd.read_excel(file_info['file_path'],sheet_name=file_info['sheet_name'])
      header_row_data = list(df.columns)
      if file_info['header_row'] > 1:
        header_row_data = df.iloc[0]
        df = df[1:]
      df.columns  = list(map(self.normalize_string, list(header_row_data)))
      #print(set(set(df.columns)-set(db_schema['mandatory_column']+db_schema['optional_columns'])))
      df = df[db_schema['mandatory_column']+db_schema['optional_columns']]
      df.rename(columns = db_schema['map_excel_2_db'],inplace=True)
      df.fillna('')
      df['manufacturer_partnumber'] = df['manufacturer_partnumber'].astype(str)
      df["check_date_life_cycle"] =  pd.to_datetime(df["check_date_life_cycle"], format='mixed').astype(str)
      df["check_date_stock"] =  pd.to_datetime(df["check_date_stock"], format="mixed").dt.date.astype(str)
      df["supplier_cover_date"] =  pd.to_datetime(df["supplier_cover_date"], format="mixed").dt.date.astype(str)
      #df["inventory_date"] =  pd.to_datetime(df["inventory_date"], format='mixed').astype(str)
      

      df.to_excel(out_file_name,index=False)
    return out_file_name
  
  def validate_master_data(seld,data:dict)->dict:
    """Validate the incoming master row data"""

    date_columns = ['check_date_compliance','check_date_regulatory','check_date_life_cycle','check_date_stock','rohs3_exemption_date']
    for key,val in data.items():
      if key in date_columns and val in ['NaT','nat','nan','Nan']:
        data[key] = None

    # check the manufacturer name in tbl_manufacturer table
    is_valid_man_name = filter_from_manufacturer_name(data['manufacturer_name'])
    if is_valid_man_name == 0:
      raise Exception(f'Manufacturer Name not present in tbl_manufacturer {data["manufacturer_name"]}')

    data['manufacturer_partnumber'] = str(data['manufacturer_partnumber'])

    return data
  
  def validate_complaince_data(self,data:dict,id:int)->list:
    """Seperate the compliance data into two rows rohs and reach"""

    rohs_compliance_data:dict = {
      'component_id' :id,
      'type':'RoHS3',
      'result': data['rohs3'],
      'exemption_date': data['rohs3_exemption_date'],
      'comment' : data['rohs3_comment']
    }
    reach_compliance_data = {
      'component_id' :id,
      'type':'Reach',
      'result': data['reach'],
      'exemption_date': None,
      'comment' : None
    }
    comp_data = [rohs_compliance_data,reach_compliance_data]
    return comp_data
  
   

  def validate_bom_record(self,data)->dict:
    data['subscriber_part_number'] = str(data['subscriber_part_number'])
    data['supplier_part_number'] = str(data['supplier_part_number'])
    data['supplier_internal_part_number'] = str(data['supplier_internal_part_number'])
    data['manufacturer_partnumber'] = str(data['manufacturer_partnumber'])
    component_id = filter_from_master(data['manufacturer_name'],data['manufacturer_partnumber'])
    
    #check exact match component in master table
    if component_id == 0:
      raise Exception(f'No match Component for {data["manufacturer_name"]} and {data["manufacturer_partnumber"]}')
    data['component_id'] = component_id

    date_columns = ["exemption_date", "supplier_cover_date" , "inventory_date" , "check_date_life_cycle" ,  "check_date_stock"]
    for key,val in data.items():
      if key in date_columns and val in ['NaT','nat','nan','Nan']:
        data[key] = None

    #return data
  
  def create_bom_master(self,file_info)->dict:

    out = create_single_record(file_info['bom_master'],file_type='bom_master')
    return out

    
  def upload_file(self,file_info:dict)->dict:
    """Start processing the given file info"""
    res = {"status":'','msg':''}
    print(f'Started Processing file {file_info["file_path"]}')
    file_type = file_info["file_type"]
    db_schema = self.config_data['db_schema'][file_type]


    #checking file path
    if not Path(file_info["file_path"]).is_file():
      res['msg'] = f'No such file  :  {file_info["file_path"]}'
      res['status'] = 'failure'
      return res
    
    #loading excel
    ipWorkBook = openpyxl.load_workbook(filename= file_info['file_path'])
    ipworksheet = ipWorkBook.active if file_info['sheet_name'] == 'active' else ipWorkBook[file_info['sheet_name']]
    
    #normalized header column name form given file
    header_column = self.get_header_data(file_info['header_row'],ipworksheet)

    #checking mandatory column names are missing in excel
    if not all(item in header_column for item in db_schema['mandatory_column']):
      header_missing = set(db_schema['mandatory_column'])-set(header_column)
      res['status'] = 'failure'
      res['msg'] = f'{header_missing}: Mandatory Column name(s) are missing'
      return res
    
    #clean the given file according to db template and saving in ./public
    file_path = self.clean_and_upload_file(file_info=file_info)

    df = pd.read_excel(file_path)
    #replace nan to None in dataframe
    df = df.replace(np.nan, None)
    
    #get column row map as dict
    dict_df = df.to_dict(orient='index')

    bom_master_id = 0
    if file_type == 'bom':

      #creating bom master entry before bom entry
      out = self.create_bom_master(file_info)
      if out['status'] != 'success':
        res.update({'status':'failure','msg':out['msg']})
        return res
      bom_master_id = out['id']

    row_count=0
    for data in dict_df.values():
      
      if file_type == 'manufacturer': 
        out = create_single_record(data = data,file_type='manufacturer')
        if out['status'] != 'success':
          res.update({'status':'failure','msg':out['msg']})
          return res

      if file_type == 'master':
         
        try:
          validated_master_data = self.validate_master_data(data)
        except Exception as e:
          res.update({'status':'failure','msg':e})
          return res
        extract_compliance_data = {k:validated_master_data.pop(k) for k in db_schema['compliant_result_column_in_ex']}
        out = create_single_record(data = validated_master_data,file_type='master')
        if out['status'] == 'success':
          validated_complaince_data = self.validate_complaince_data(extract_compliance_data,id = out['id'])
          create_compliance_record(validated_complaince_data)
        else:
          res.update({'status':'failure','msg':out['msg']})
          return res

      if file_type == 'bom':
        if not bom_master_id:
          res.update({'status':'failure','msg':'Failed to create bom_master'})
          return res
        try:
          self.validate_bom_record(data)
        except Exception as e:
          res.update({'status':'failure','msg':e})
          return res
        
        data['bom_master_id'] = bom_master_id
        data['revision'] = file_info['bom_master']['revision']
        out = create_single_record(data,file_type='bom')
        if out['status'] != 'success':
          res.update({'status':'failure','msg':out['msg']})
          return res

      row_count +=1   
    res['status'] = 'success'
    res['msg'] = f'file {file_info["file_path"]} uploaded successfully in db Row count : {row_count}'
    return res
    
  def load_file_date(self) ->dict:
    """Load the file info from config and start processing"""

    res = {'status':'success'}
    out_dir = Path("./public").mkdir(parents=True, exist_ok=True)
    if not delete_all_tables():
      res.update({'status':'failure','msg':'Failed in deleting the table rows'})
      return res
    
    for file_info in self.config_data['file']:
      res = self.upload_file(file_info=file_info)
      if res['status'] != 'success':
        return res
      print(res)
      print()
    return res
    
    

if __name__ == '__main__':
  uf = UploadFile()
  out = uf.load_file_date()
  print(out)
  