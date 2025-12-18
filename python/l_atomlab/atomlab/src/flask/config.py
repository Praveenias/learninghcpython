
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from pathlib import Path
import json

db = SQLAlchemy()
ma = Marshmallow()




# used_for_api

subscriber_column_names = ["CompanyName","SiteName","DivisionName","PrimaryContact",
                "PrimaryEmail", "PhoneNumber", "Status","Action"]

license_column_name =["CompanyName","SiteName","DivisionName","Status",
      "StartDAte", "EndDate", "productType", "Component Limit", "Licence Type"]
product_column_name = ["CompanyName","SiteName","DivisionName","productName",
      "modelName", "location", "productType", "categoryName", "effectiveDate"]

boms_column_name = ["CompanyName","SiteName","DivisionName","bomName","productName","modelName","location",
                "revision", "status","Action"]

regulation_column_name = ["regulationType" ,"regulationName" ,"directiveName", "startDate"]

subtances_column_name = ["SubstanceName",'SubstanceCategory','CasNumber','EC Number']

sub_comp_map={}


def db_config()->str:
  try:
    with open(Path('file_upload.json'),encoding='utf-8') as data:
      db_config = json.load(data)['db_config']
      connection_str = f'mysql+pymysql://{db_config["username"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["db_name"]}'
      return connection_str
  except Exception as e:
      print("PLease check db config data")
      return ''



