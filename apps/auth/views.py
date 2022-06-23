from os import access
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, Body
from pydantic import BaseModel
from .jwt_handler import AuthHandler
from sqlalchemy.orm import Session
from apps.auth.models import User
from dependencies import get_db
from .schema import RegisterReponseSchema, RegisterRequestSchema, RegisterRequestSchema
from sqlalchemy.exc import IntegrityError
from .import models
from .dependencies import get_current_user
auth = APIRouter()


auth_handler = AuthHandler()


@auth.post('/register', status_code=201, response_model=RegisterReponseSchema)
def register(request: RegisterRequestSchema = Body(default=None), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=request.username).first()

    if user:
        try:
            if user.email == request.user:
                raise HTTPException(status_code=400, detail='Email is taken')
        except:
            raise HTTPException(status_code=400, detail='Username is taken')

    hashed_password = auth_handler.get_password_hash(request.password)

    try:
        user = User()
        user.username = request.username
        user.email = request.email
        user.password = hashed_password

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    except IntegrityError as e:

        raise HTTPException(status_code=400, detail='Email Already Exist')


@auth.post('/login')
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=form.username).first()

    if (user is None) or (not auth_handler.verify_password(form.password, user.password)):
        raise HTTPException(
            status_code=401, detail='Invalid username and/or password')
    access_token = auth_handler.access_token(user.username)
    # refresh_token = auth_handler.refresh_token(user.username)

    return {"access_token": access_token, 'token_type': 'bearer'}

class RefreshToken(BaseModel):
    refresh_token : str


# @auth.post('/refresh')
# def refresh_token(request : RefreshToken):


#     payload = auth_handler.decodeJWT(bytes(refresh_token))
#     print(payload)
   

#     return refresh_token


@auth.get("/me")
async def who_Am_I(user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):

    return user
