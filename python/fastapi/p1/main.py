from fastapi import FastAPI,Form,File,Depends,HTTPException,Request,UploadFile
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
import os
from fastapi.responses import FileResponse
# from middleware import auth_middleware

from fastapi.encoders import jsonable_encoder
import pandas as pd

app = FastAPI()
# app.middleware('http')(auth_middleware)

fake_users_db = {
    "praveen": {
        "username": "praveen",
        "email": "praveen@ilensys.com",
        "hashed_password": "fakehashedpraveen",
    },
    
}




class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

oauth2_ = OAuth2PasswordBearer(tokenUrl="token")

def fake_hash_password(password: str):
    return "fakehashed" + password



class User(BaseModel):
    username: str
    email: str | None = None
  

class UserInDB(User):
    hashed_password: str

@app.get('/')
async def root(token: Annotated[str, Depends(oauth2_)]):
  return {"token":token}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/login")
async def login(username:Annotated[str,Form()],password:Annotated[str,Form()]):
   return {"Username":username,"Password":password}


@app.post("/getipfile")
async def getipfile(ipfile:Annotated[bytes,File()],token: Annotated[str, Depends(oauth2_)]):
   df = pd.read_excel(ipfile)
   print(df.head())
   return {"file_size":len(ipfile)}

@app.post("/items")
async def create_item(item:Item)->Item:
  data = jsonable_encoder(item)
  print(type(item.name),item.name)
  return item

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    print(hashed_password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    # Define the directory where you want to save the files
    upload_dir = "uploads"
    
    
    # Create the full path to save the uploaded file
    file_path = os.path.join(upload_dir, file.filename)
    
    # Save the file to the specified directory
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    download_link = f"/download/{file_path}"
    
    return {"filename": file.filename,"downloadable_link":download_link}

@app.get("/download/{file_id}")
async def download_file(file_id: str):
    upload_dir = "uploads"
    # Verify if the file exists in the upload directory
    file_path = os.path.join(upload_dir, "bom.xlsx")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    # Return a response with the file for download
    return FileResponse(file_path, headers={"Content-Disposition": f"attachment; filename={file_id}"})