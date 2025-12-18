import mysql.connector
from mysql.connector import Error
import argparse
    
def execute_sql_script(table_order):
    try:
        cnx_source = mysql.connector.connect(
            user='root',
            password='Ilensys@123',
            host='localhost',
            database='data_transfer_old'
        )
        cnx_dest = mysql.connector.connect(
            user='root',
            password='Ilensys@123',
            host='localhost',
            database='data_transfer_new',
            autocommit=True
        )

        cursor_source = cnx_source.cursor()
        cursor_dest = cnx_dest.cursor()

        cursor_source.execute("SHOW TABLES")

        table_names = [table[0] for table in cursor_source.fetchall()]
        result = all(element in table_names for element in table_order)
        if not result:
           return "tables are missing"

        for table in table_order:
          sql_command = f"SELECT * FROM {table}"
          cursor_source.execute(sql_command)
          column_names = cursor_source.column_names
          table_data = cursor_source.fetchall()
          for row in table_data:
            row_data = {column:row[index] for index,column in enumerate(column_names)}
            columns = ', '.join([f"`{column}`" for column in row_data.keys()])
            values = ', '.join(['%s'] * len(row_data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"

            cursor_dest.execute(query, tuple(row_data.values()))
          print(f"{table} is inserted successfully Row Count : {len(table_data)}")

        cursor_source.close()
        cursor_dest.close()

        cnx_source.close()
        cnx_dest.close()
    except Error as e:
        print(f"Error : {e}")

def create_argparse():
  parser = argparse.ArgumentParser(prog='praveen.py',description='copy data from one db to another')

  parser.add_argument('-d','--delete',help="Truncate the destination DB Data's",action='store_true')
  args = parser.parse_args()
  return args



if __name__ == "__main__":
    
    args = create_argparse()
    print(args.delete)
    table_order = ['activity_log','tbl_countries','tbl_user','tbl_subscriber','tbl_license','tbl_subscriber_user','tbl_manufacturers',
                    'tbl_component_master','compliance_result','tbl_products','tbl_bom_master','tbl_bom','tbl_risk_components']
     
    # out = execute_sql_script(table_order)
    # print(out)


