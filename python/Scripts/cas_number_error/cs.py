import re
from mysql.connector import connect, Error
import pandas as pd

def connectDB(db_details:dict):
  try:
    with connect(**db_details) as db_con:
      print("DB Connected Successfully")
      db_query_1 = "SELECT * from tbl_bom;"
      with db_con.cursor(buffered=True) as cursor:
        cursor.execute(db_query_1)
        print(cursor.fetchall())
      #   list1=[]
      #   for data in cursor:
          #print(data[0])
          # if data[0] == 4126:
          #   print(data[3],'7440-02-0',len(data[3]))
          #   print(re.fullmatch('[0-9]{2,6}-[0-9]{2}-[0-9]{1}',data[3]))
          #   break
        #   if re.fullmatch('[0-9]{2,6}-[0-9]{2}-[0-9]{1}',data[3]) is None:
        #     #break
        #     data2 = dict(zip(cursor.column_names,data))
        #     # print(data2)7
        #     # break
        #     list1.append(data2)
        # print("len : ",len(list1))
        # df = pd.DataFrame( cursor.fetchall(),columns=cursor.column_names)
        # # df.to_excel('output1.xlsx',index=False)
        # x = df[df['cas_number'].str.fullmatch('[0-9]{2,6}-[0-9]{2}-[0-9]{1}')]
        # df_diff = pd.concat([df,x]).drop_duplicates(keep=False)
        # if df_diff.empty:
        #   print("No Informat Cas_number")
        #   return True
        # print(df_diff)
        # # writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
        # # df_diff.to_excel(writer, sheet_name='data')
        # # writer.save()
        # df_diff.to_excel(db_details['database']+"_informat_cas_error2.xlsx",index=False)       
    return True
     
  except Error as e:
    print(f'Database Connection error: {e}')


if __name__=='__main__':
    db_details = {
        "host" :"localhost",
        "database":"obs_new",
        "port":"3306",
        "username":"root",
        "password":""
    }
    clm_names = connectDB(db_details)
