This directory is mainly for file_upload, apicheck , compare excel file

Pre-requisite:
  python 3.10+

create virtual enviroinment:
  python3 -m venv /path/to/new/virtual/environment

activate virtual enviroinment:
  linux : source /path/to/new/virtual/environment/bin/activate
  windows : /path/to/new/virtual/environment/Scripts/activate

Once virtual enviroinment created successfully, install required pakage 
  pip3 install -r requirements.txt


For API Check
  python3 app.py ( This will create a local server that run at localhost:8001 (Editable))



FOlder Structure,


Feature FIle_upload:
  1. COnfigure file data in file_upload.json file
  2. run the file_upload.py file  comm : python3 file_upload.py

Feature API Check,
  1. Set base Url in request_api.py
  2. run the app.py file  comm : python3 app.py

pip install -U marshmallow-sqlalchemy

