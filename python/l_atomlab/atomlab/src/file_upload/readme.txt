Description:
  File upload is a feature to upload manufacturer, master and bom files into an
  Database .

Pre-Requisite:
  1. Fresh migrated DB (With seeder)
  2. InitTestSeeder should be run( To get subscriber and user details)

File Description:
  1. file_upload.json
        file that contains list of input file and its information,
        and db related information.
  2. model.py
        migration file for 5 tables
          1. tbl_manufacturer
          2. tbl_component_master
          3. compliance_result
          4. tbl_bom_master
          5. tbl_bom
  3. file_upload.py
        Main File that contains logic to upload files


Run the Script

1. Fill the file informations and db information in file_upload.json file
2. run the below command
    Windows : python file_upload.py
    Linux : python3 file_upload.py





