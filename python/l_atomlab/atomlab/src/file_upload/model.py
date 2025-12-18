
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker,declarative_base

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

import datetime
from pathlib import Path
import json


def db_config()->str:
  try:
    with open(Path('test.json'),encoding='utf-8') as data:
      db_config = json.load(data)['db_config']
      connection_str = f'mysql+pymysql://{db_config["username"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["db_name"]}'
      return connection_str
  except Exception as e:
      print("PLease check db config data")
      return ''

engine = sa.create_engine(db_config())
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Manufacturer(Base):
  """Manufacturer Db Model"""

  __tablename__ = "tbl_manufacturers"
  # __table_args__ = {'extend_existing': True}
  id = sa.Column(sa.Integer, primary_key=True)
  name = sa.Column(sa.String(255), unique=True)
  normalized_name =  sa.Column(sa.String(255), unique=True)
  category = sa.Column(sa.String(255),default= 'public')
  alert_mechanism = sa.Column(sa.String(255), default= 'manual')
  registration_name = sa.Column(sa.String(255), default= 'oemalerts@ilensys.com')
  status = sa.Column(sa.String(255), default= 'approved')
  type = sa.Column(sa.String(255), default= 'manufacturer')
  created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
  updated_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)



class ManufacturerSchema(SQLAlchemyAutoSchema):
  """Manufacturer Db Schema Serialization from manufacturer dict to object"""
  class Meta:
    model = Manufacturer
    load_instance = True

manufacturer_schema = ManufacturerSchema()

class Master(Base):
  """Master Db Model"""
  __tablename__ = "tbl_component_master"
  __table_args__ = {'extend_existing': True}

  id = sa.Column(sa.Integer, primary_key=True)
  manufacturer_name = sa.Column(sa.String(80), unique=True)
  manufacturer_partnumber = sa.Column(sa.String(80))
  manufacturer_description = sa.Column(sa.String(255),nullable=True,default= ' ')
  part_category = sa.Column(sa.String(255),default= 'Not Available')
  component_type = sa.Column(sa.String(255),default= 'Not Available')
  part_type = sa.Column(sa.String(255),default= 'Not Available')
  part_status = sa.Column(sa.String(255),default= 'Not Available')

  stock_position = sa.Column(sa.Integer)
  supply_lead_time = sa.Column(sa.Double())

  status = sa.Column(sa.String(50),default= 'approved')
  component_classification = sa.Column(sa.String(50),default= 'Standard')
  assembly_type = sa.Column(sa.String(80))
  power_type = sa.Column(sa.String(80))
  regulatory_test = sa.Column(sa.Boolean(),default= False)

  check_date_regulatory = sa.Column(sa.DATE,nullable=True)
  check_date_life_cycle = sa.Column(sa.Date,nullable=True)
  check_date_stock = sa.Column(sa.DATE,nullable=True)
  check_date_compliance = sa.Column(sa.DATE,nullable=True)
  stock_details = sa.Column(sa.JSON())

  lead_time_details = sa.Column(sa.JSON())
  ltb_possibility = sa.Column(sa.Boolean())
  year_to_eol = sa.Column(sa.Double())
  price = sa.Column(sa.Double())
  remarks = sa.Column(sa.TEXT())
  created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
  updated_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)

class MasterSchema(SQLAlchemyAutoSchema):
  """Master Db Schema Serialization from Master dict to object"""
  class Meta:
    model = Master
    load_instance = True

master_schema = MasterSchema()

class ComplianceResult(Base):
    """Compliance Result Db Model"""
    __tablename__ = "compliance_result"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    component_id = sa.Column(sa.Integer)
    type = sa.Column(sa.String(255))
    result = sa.Column(sa.String(255))
    exemption_date = sa.Column(sa.DATE,nullable=True)
    comment = sa.Column(sa.String(255))
    remarks = sa.Column(sa.String(255))

class ComplianceResultSchema(SQLAlchemyAutoSchema):
  """Compliance Result Db Schema Serialization from Compliance dict to object"""
  class Meta:
    model = ComplianceResult
    load_instance = True

compliance_result_schema = ComplianceResultSchema(many=True)

class BomMaster(Base):
    """BomMaster Result Db Model"""

    __tablename__ = "tbl_bom_master"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    subscriber_id = sa.Column(sa.BIGINT)
    product_id = sa.Column(sa.BIGINT)
    approver_id = sa.Column(sa.BIGINT)
    author_id = sa.Column(sa.BIGINT)
    eau = sa.Column(sa.Integer)
    description = sa.Column(sa.String(50),default= 'Desc1')
    category = sa.Column(sa.String(50),default= 'New Product Development')

    bom_name = sa.Column(sa.String(255))
    revision = sa.Column(sa.String(15))
    status = sa.Column(sa.String(255))
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)

class BomMasterSchema(SQLAlchemyAutoSchema):
  """BomMaster Db Schema Serialization from BomMaster dict to object"""
  class Meta:
    model = BomMaster
    load_instance = True

bom_master_schema = BomMasterSchema()

class Bom(Base):
    """Bom Db Model"""

    __tablename__ = "tbl_bom"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)

    bom_master_id = sa.Column(sa.BIGINT)
    revision = sa.Column(sa.String())

    manufacturer_partnumber = sa.Column(sa.String(80))
    manufacturer_name = sa.Column(sa.String(80))
    subscriber_part_number = sa.Column(sa.String(80))
    description = sa.Column(sa.String(80))

    proactive_analysis = sa.Column(sa.Boolean())
    ltb_possibility = sa.Column(sa.Boolean())

    description = sa.Column(sa.String())
    Qty = sa.Column(sa.Float())
    Critical = sa.Column(sa.String())
    supplier_internal_part_number = sa.Column(sa.String())
    supplier_part_number = sa.Column(sa.String())
    supplier_manufacturer = sa.Column(sa.String())
    supplier_lead_time = sa.Column(sa.DECIMAL())
    supplier_stock = sa.Column(sa.Integer())
    supplier_monthly_usage = sa.Column(sa.Integer())

    component_id = sa.Column(sa.BIGINT,default=0)

    supplier_cover_months = sa.Column(sa.DECIMAL)

    supplier_cover_date = sa.Column(sa.DATE,nullable=True)
    inventory_date = sa.Column(sa.DATE,nullable=True)
    check_date_life_cycle = sa.Column(sa.DATE,nullable=True)
    check_date_stock = sa.Column(sa.DATE,nullable=True)
    remarks = sa.Column(sa.TEXT())
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)

class BomSchema(SQLAlchemyAutoSchema):
  """Bom Db Schema Serialization from Bom dict to object"""
  class Meta:
    model = Bom
    load_instance = True

bom_schema = BomSchema()

def create_single_record(data:dict,file_type:str)->dict:
  """based on file type.. create record in the respective table

  Parameters
  ----------
  data : dict , Mandatory
      column , value map in dict 
  file_type : list , Mandatory
      refers manufacturer or master or bom_master or bom

  Returns
  -------
  dict
    {'status' : success or failure,
    'msg' : reason for failure,
    'id': primary id created in table }

  
  """

  res = {'status':'','id':None,'msg':''}
  try:
    if file_type == 'manufacturer':
      data = manufacturer_schema.load(data,session=session)

    elif file_type == 'master':
      data = master_schema.load(data,session=session)

    elif file_type == 'bom_master':
      data = bom_master_schema.load(data,session=session)

    elif file_type == 'bom':
      data = bom_schema.load(data,session=session)

    else:
      raise Exception(f'Invalid file_type{file_type}')

    session.add(data)
    session.commit()
    res.update({'status':'success','id':data.id})
  except Exception as e:
    res.update({'status':'failure','msg':e})
  return res

def create_compliance_record(data):
  """two rows for rohs and reach will be inserted in one go"""
  try:
    c_r_obj = compliance_result_schema.load(data,session=session)
    session.add_all(c_r_obj)
    session.commit()
  except Exception as err:
    print(err,data)


def filter_from_master(man_name:str,man_partnumber:str)->int:
  """check for man name and man part number present in master table 

  Returns
  -------
  id : int
    0 -> if not present or 
    val -> id of filtered row
  """

  id_n = session.query(Master).filter(Master.manufacturer_name == man_name, Master.manufacturer_partnumber == man_partnumber).one_or_none()
  if id_n == None:
    return 0
  return id_n.id
  
def filter_from_manufacturer_name(man_name:str)->int:
  """check for man name present in manufacturer table 

  Returns
  -------
  id : int
    0 -> if not present or 
    val -> id of filtered row
  """
  id_n = session.query(Manufacturer).filter(Manufacturer.name == man_name).one_or_none()
  if id_n == None:
    return 0
  return id_n.id

def delete_all_records(modal_name:str)->int:
  modal_class_map = {
    'master':Master,
    'manufacturer':Manufacturer,
    'bom_master':BomMaster,
    'compliance_result':ComplianceResult,
    'bom':Bom
  }
  try:
    num_rows_deleted = session.query(modal_class_map[modal_name]).delete()
    session.commit()
    return num_rows_deleted
  except Exception as err:
    print(err)
    return -1
  
def delete_all_tables()->bool:
  """delete all the rows in the given database

  mainly "bom","master","manufacturer","compliance_result","bom_master"

  Returns
  -------
  bool
    True -> success or 
    Flase -> Failure
  
  """
  tables = ["bom","master","manufacturer","compliance_result","bom_master"]
  for data in tables:
    rows_deleted = delete_all_records(data)
    if rows_deleted == -1:
      return False
    print(f'{rows_deleted} rows deleted in {data} table')
  return True








