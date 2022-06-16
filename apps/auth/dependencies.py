from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .jwt_handler import AuthHandler
from dependencies import get_db

from jose.exceptions import JWTError
from . import models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')
auth_handler = AuthHandler()

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):

    try:
        payload = auth_handler.decodeJWT(token)

        username = payload.get("username")

        if username is None:
            
            raise HTTPException(status_code=403, detail="Could not validate credentials",headers={"WWW-Authenticate": "Bearer"},)

        user = db.query(models.User).filter_by(username=username).first()

        return user

    except JWTError:
        raise HTTPException(status_code=403, detail="Could not validate credentials",headers={"WWW-Authenticate": "Bearer"},)

    