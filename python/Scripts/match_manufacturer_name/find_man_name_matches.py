from mysql.connector import connect, Error
from fuzzywuzzy import process, fuzz
import pandas as pd

def connectDB(db_details:dict):

  comp_table=[]
  try:
    with connect(**db_details) as db_con:
      print("DB Connected Successfully")

      db_query_1 = "SELECT id,normalized_name FROM `manufacturers` ORDER BY `manufacturers`.`normalized_name` ASC"
      with db_con.cursor() as cursor:
        cursor.execute(db_query_1)
        db_data = [item[1] for item in cursor.fetchall()]

        for i,data in enumerate(db_data):
          compare_list = [data]
          compare_list_common = []
          for compare in range(i+1,len(db_data)):          
            match_per = fuzz.token_sort_ratio(data,db_data[compare])
            if match_per > 70:
              compare_list_common.append(db_data[compare])
          compare_list.append(compare_list_common)
          comp_table.append(compare_list)
    df = pd.DataFrame(comp_table,columns=['Manufacturer Name','Matches'])
    df.to_excel('manufacturer_macth.xlsx',index=False)
    return True
     
  except Error as e:
    print(f'Database Connection error: {e}')


if __name__=='__main__':
    db_details = {
        "host" :"localhost",
        "database":"db_qa",
        "port":"3306",
        "username":"root",
        "password":""
    }
    clm_names = connectDB(db_details)
