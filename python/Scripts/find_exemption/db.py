from mysql.connector import connect, Error
import pandas as pd

def connectDB(db_details:dict):

  comp_table=[]
  try:
    with connect(**db_details) as db_con:
      print("DB Connected Successfully")

      db_query_1 = "SELECT compliance_results.component_id, group_concat(distinct exemption_id) as test FROM compliance_results left join components_exemptions_maps on components_exemptions_maps.component_id = compliance_results.component_id AND components_exemptions_maps.source_type='MANUAL' where result = 'TBD' AND compliance_source_type='Manual' group by compliance_results.component_id"
      with db_con.cursor() as cursor:

        sql_query = cursor.execute(db_query_1)
        for data in sql_query:
          print(data)
        #   if test is None:
        #     comp_table.append(component_id)
        # print("Invalid exemption count : ",len(comp_table),comp_table)
        # if (len(comp_table) == 0):return False
        # comp_table = f"({str(comp_table)[1:-1]})"
        
        
    #     db_query_2 = "SELECT manufacturer_name,manufacturer_partnumber FROM `master_components` WHERE id in"+comp_table
    #     cursor.execute(db_query_2)
    #     datas = cursor.fetchall()
    #     column_names = cursor.column_names
    # df = pd.DataFrame(datas,columns=column_names)
    # df.to_excel('invalid_exemption_list.xlsx',index=False)
    # print(df)
    return True
     
  except Error as e:
    print(f'Database Connection error: {e}')


if __name__=='__main__':
    db_details = {
        "host" :"localhost",
        "database":"db_qa",
        "port":"3307",
        "username":"root",
        "password":"Ilensys@123"
    }
    clm_names = connectDB(db_details)
