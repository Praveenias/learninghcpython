from fastapi import FastAPI,File,Depends,HTTPException,status,UploadFile
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from fastapi.responses import FileResponse

from convertion import *

users_db = {
    "atomobs": {
        "username": "",
        "email": "",
        "password": "",
    },
    
}

oauth2_ = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user_dict = users_db.get(form_data.username)
    
    if not user_dict:
      raise credentials_exception
    
    if not user_dict["password"] == form_data.password:
      raise credentials_exception
        
   
    return {"access_token": form_data.username+'atom', "token_type": "bearer"}

@app.post("/getipfile")
async def getipfile(ipfile:Annotated[bytes,File()],
                    token: Annotated[str, Depends(oauth2_)]):
  out = mainstart(ipfile)
  if out["status"] == "success":
    return FileResponse('./output/outputoutput.xlsx', media_type='application/octet-stream',filename='output.xlsx')
  return out



