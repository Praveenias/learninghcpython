#dont change column order name in db query and column_names
import mysql.connector
from mysql.connector import Error
import json
    
def v3Json():
  out = {'status':''}
  try:
      cnx_source = mysql.connector.connect(
          user='root',
          password='Ilensys@123',
          host='localhost',
          database='2_1_7'
      )

      query = "SELECT tbl_bom.id,subscriber_part_number as ipn,tbl_bom.manufacturer_name as cmfr,tbl_bom.manufacturer_partnumber as cmpn,Qty,mc_risk,mc_risk_details,supplier_lead_time,supplier_stock,mc.manufacturer_name as mmfr,mc.manufacturer_partnumber as mmpn,mc.power_type,mc.part_status,mc.stock_position,mc.supply_lead_time,group_concat(comp.type) as type,group_concat(comp.result) as result,group_concat(comp.exemption_date) as exemption_date FROM 2_1_7.tbl_bom left join 2_1_7.tbl_component_master as mc on tbl_bom.component_id=mc.id left join 2_1_7.compliance_result as comp on comp.component_id=mc.id where bom_master_id=23 group by id"

      cursor_source = cnx_source.cursor()
      columns_names = ['id','ipn','cmfr','cmpn','Qty','mc_risk',
        'mc_risk_details','supplier_lead_time','supplier_stock','mmfr','mmpn',
        'power_type','part_status','stock_position','supply_lead_time','type','result','exemption_date'
      ]
      mc_columns = ['mmfr','mmpn',
        'power_type','part_status','stock_position','supply_lead_time','result','exemption_date']
      bc_columns = ['ipn','cmfr','cmpn','Qty','supplier_stock','supplier_lead_time']
      result_columns = ['mc_risk','mc_risk_details']
      columnMap = {
          'mmpn':"manufacturer_partnumber",
          "mmfr":"manufacturer_name",
          "Qty":'quantity',
          'part_status':'lifecycle_status',
          'cmfr':'manufacturer_name',
          'cmpn':'manufacturer_partnumber',
          'ipn':'customer_partnumber',
          'stock_position':'stock_position',
          'power_type':'power_type',
          'supply_lead_time':'supply_lead_time',
          'supplier_stock':'supplier_stock',
          'supplier_lead_time':'supplier_lead_time',
          'mc_risk':'risk_priority',
          'mc_risk_details':'mc_risk_details',
          'type':'type',
          'result':'result',
          'exemption_date':'exemption_date'

      }

      cursor_source.execute(query)
      json_data = {
          "bom":{
            "bom_details":{
              "bom_number":"riskcheck1",
              "bom_name":"riskcheck1",
              "normalized_name":"riskcheck1",
              "revision":"1",
              "bom_eau":500
              },
            "data":[]
          }
      }

      for data in cursor_source.fetchall():
        mastercomponent = { 'company_id':None,
                            'manufacturer_description':'V3Json',
                            "part_category":"unconfirmed",
                            "component_type":"unconfirmed",
                            "part_type":"unconfirmed"
                          }
        bomcomponent = {}
        result = {}
        
        for i,j in zip(columns_names,data):
          
          if i in mc_columns:
            if i == 'result':
                resultData = j.split(",")
                mastercomponent['rohs3']=resultData[0]
                mastercomponent['reach']=resultData[1]
            elif i=='exemption_date':
              exemptionData = j.split(",") if j else ['']
              mastercomponent['exemption_date'] = exemptionData[0]

            else:
              mastercomponent[columnMap[i]] = str(j)
          if i in bc_columns:
            # if i == 'ipn':
            #   if j in 
                
            bomcomponent[columnMap[i]] = str(j)
          if i in result_columns: 
            if i == 'mc_risk_details':
              
              riskData = json.loads(j)
              result['risk_type'] = riskData['type_of_risk']
            else: result[columnMap[i]] = j

        json_data['bom']['data'].append({'mastercomponent':[mastercomponent],
                'bomcomponent':bomcomponent,'result':result})
      cursor_source.execute('SELECT id,bom_name,revision,eau FROM 2_1_7.tbl_bom_master where id=23')
      bommasterdata = cursor_source.fetchone()

      #fillupBomDetails(bommasterdata)
      json_data['bom']['bom_details']['bom_number'] = bommasterdata[1]
      json_data['bom']['bom_details']['bom_name'] = bommasterdata[1]
      json_data['bom']['bom_details']['normalized_name'] = bommasterdata[1]
      json_data['bom']['bom_details']['revision'] = bommasterdata[2]
      json_data['bom']['bom_details']['bom_eau'] = bommasterdata[3]
      with open('data.json', 'w') as f:
        json.dump(json_data, f)
      cnx_source.close()
      out['status'] = 'success'
      out['file_name'] = 'data.json'
  except Error as e:
      print(f"Error : {e}")

  return out

if __name__ == "__main__":    
  out = v3Json()
  print(out)


