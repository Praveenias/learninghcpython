import argparse
from pathlib import Path
import json
import pandas as pd


class Check_Output_column:
    def __init__(self,json_rel_path=None) -> None:
        self.root_path:Path = Path(__file__).resolve().parent # to get folder path of a this file
        self.result={}
        self.json_rel_path:Path ='./input.json' if not json_rel_path else json_rel_path 
        self.json_data = self.get_json_data()
        self.mandatory_column_name = ['Manufacturer Name','Manufacturer Part Number']
    
    def create_parser() -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            prog='dataClean',
            description='Check the data of given excel file')

        parser.add_argument("--ipfile1","-d",required=True,
                            help="Input file classification",)
        parser.add_argument("--ipfile2","-i",required=True,
                            help="Input file name with full path and extension")
        parser.add_argument("--ipsheetname1","-s", 
                            help="Input Sheet name(Case Sensitive)")
        parser.add_argument("--ipsheetname2","-o",
                            help="Output File Name(without extension)")
        parser.add_argument("--headerrow","-r",type=int, help="Header Name Row",
                            default=1)
        # parser.add_argument("--filetype","-f",required=True,
        #                     help="enter File type",choices=file_type) 

        args = parser.parse_args()
        return args
    
    def check_valid_path(self,ip_path:Path):
        ip_rel_path = Path.joinpath(self.root_path,ip_path)
        if not Path(ip_rel_path).is_file():
            self.result['status']='failure'
            self.result['info'] = 'File not exists'
            return False
        return True

    def get_json_data(self):
        json_data={}

        json_file_path = Path.joinpath(self.root_path,self.json_rel_path)
        if not Path(json_file_path).is_file():
            self.result['status']='failure'
            self.result['info'] = 'Json config File not exists'
            return json_data
        try:
            with open(json_file_path,encoding='utf-8') as fd:
                json_data = json.load(fd)["data"]
                return json_data
        except Exception as err:
            self.result['status']='failure'
            self.result['info'] = err
            return json_data

    def get_excel_data(self,ip_details):
        status = {"status":'',"data":''}
        if not self.check_valid_path(ip_details['file_name']):
            status['status']=False
        try:
            ip_file_path = Path.joinpath(self.root_path,ip_details['file_name'])
            ip_sheet_name = ip_details['sheet_name'] if ip_details['sheet_name'] else 0
            ip_column_name = self.mandatory_column_name+ip_details['column_name']
            df = pd.read_excel(ip_file_path,sheet_name=ip_sheet_name)[ip_column_name]
            status['status']=True
            status['data']=df
        except Exception as err:
            self.result['status']='failure'
            self.result['info'] = err
            status['status']=False
        return status



    def main(self):
        if self.json_data:
            status1 = self.get_excel_data(self.json_data['file_1'])
            status2 = self.get_excel_data(self.json_data['file_2'])
            if status1['status'] and status2['status']:
              #print(status1['data'])
              
              df1 = status1['data']
              print(df1)
              df1 = df1.astype({'Manufacturer Part Number':str})
              df1['normalized'] = df1["Manufacturer Name"]+df1["Manufacturer Part Number"]
              print(df1)
              df2 = status2['data']
        return self.result


if __name__ == '__main__':
    coc = Check_Output_column()
    print(coc.main())
