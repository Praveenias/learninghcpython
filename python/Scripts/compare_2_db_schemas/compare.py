from mysql.connector import connect, Error
import pandas as pd

def connectDB(db_details:dict):
	try:
		with connect(**db_details) as db_con:
			print("DB Connected Successfully")
			db_query_1 = "show tables;"
			with db_con.cursor(buffered=True) as cursor:
				cursor.execute(db_query_1)
				l1 = [x for x, in cursor.fetchall()]
				return l1
	except Exception as e:
		print(f'Database Connection error: {e}')

def get_column_names(db_details,table_names):
    try:
        with connect(**db_details) as db_con:
          df=pd.DataFrame()
          print(table_names)
          print("DB Connected Successfully")
          for tab in table_names:
            db_query = f"select * from {tab}"
            with db_con.cursor(buffered=True) as cursor:
              cursor.execute(db_query)
              column_name = [i[0] for i in cursor.description]
              #print(pd.Series(column_name))
              s = pd.Series(column_name,index=range(len(column_name)))
              df = pd.concat([df,s.rename(tab)],axis=1)
              #print(df[tab])
          return df

            
        
    except Exception as e:
        print(f'Database Connection error: {e}')
    


if __name__=='__main__':
    db_details1 = {
        "host" :"localhost",
        "database":"obs_2_1_0",
        "port":"3307",
        "username":"root",
        "password":"Ilensys@123"
    }
    db_details2 = {"host" :"localhost",
        "database":"obs_malvern",
        "port":"3307",
        "username":"root",
        "password":"Ilensys@123"
    }
    table_name1 = connectDB(db_details1)
    table_name2 = connectDB(db_details2)

    if table_name1 != table_name2:
        print("table names varies")
    else:
        print("table names are same")
        df1 = get_column_names(db_details1,table_name1)
        df2 = get_column_names(db_details2,table_name2)
        print(df1,df2)
        #print(df1.reset_index(drop=True) == df2.reset_index(drop=True))
        #print(df1.sort_index().sort_index(axis=1) == df2.sort_index().sort_index(axis=1))
        #print(df1.equals(df2))
        #print(df1.to_excel('1.xlsx'),df2.to_excel('2.xlsx'))
