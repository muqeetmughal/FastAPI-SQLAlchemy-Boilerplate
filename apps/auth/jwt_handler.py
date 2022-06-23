from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException, Security, Body
from decouple import config
import time
import jwt
JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)


    def token_reponse(self, token: str):
        return token

    def access_token(self, username: str):
        payload = {
            "exp": int(time.time() + 60*60*24),
            'iat': int(time.time()),
            'username': username,
            'type' : "access"

        }
        token = jwt.encode(payload, JWT_SECRET,JWT_ALGORITHM)
        return self.token_reponse(token)

    # def refresh_token(self, username : str):

    #     payload = {
    #         "exp": int(time.time() + 60*60*24),
    #         'iat': int(time.time()),
    #         'username': username,
    #         'type' : "refresh"
    #     }
    #     return jwt.encode(payload,JWT_SECRET, JWT_ALGORITHM)


    def decodeJWT(self, token: str):
        try:
            decode_token = jwt.decode(
                token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return decode_token if decode_token["exp"] >= time.time() else None
        except Exception as e:

            print(e)
            return {}

   