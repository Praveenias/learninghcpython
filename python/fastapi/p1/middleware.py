# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from fastapi import  Depends, HTTPException,Request

# def authenticate_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
#     if token != "your_secret_token":
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return {"username": "user"}

# async def auth_middleware(request: Request, user=Depends(authenticate_user)):
#     # Attach the authenticated user to the request state
#     request.state.user = user