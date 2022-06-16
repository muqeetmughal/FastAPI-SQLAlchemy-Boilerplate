from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException, Security, Body
from jose import jwt
import jwt
from decouple import config
import time


JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = "SECRET"


    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm="HS256"
        )

    # def decode_token(self, token):
    #     try:
    #         payload = jwt.decode(token, self.secret, algorithms=['HS256'])
    #         return payload['sub']
    #     except jwt.ExpiredSignatureError:
    #         raise HTTPException(
    #             status_code=401, detail='Signature has expired')
    #     except jwt.InvalidTokenError as e:
    #         raise HTTPException(status_code=401, detail='Invalid token')

    # def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
    #     return self.decode_token(auth.credentials)

    def token_reponse(self, token: str):
        return token

    def signJWT(self, username: str):
        payload = {
            "username": username,
            "expiry": int(time.time() + 600),
            "created":int(time.time())

        }
        token = jwt.encode(payload, JWT_SECRET,JWT_ALGORITHM)
        return self.token_reponse(token)

    def decodeJWT(self, token: str):
        try:
            decode_token = jwt.decode(
                token, JWT_SECRET, algorithms=JWT_ALGORITHM)
            return decode_token if decode_token["expiry"] >= time.time() else None
        except:
            return {}
