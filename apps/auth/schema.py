from typing import Optional
from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str

class RegisterRequestSchema(BaseModel):
    username : str
    email : str
    password : str

class RegisterReponseSchema(BaseModel):
    id : int
    name : Optional[str]
    username : str
    email : Optional[str]
    phone_number : Optional[str]
    is_admin : bool

    class Config:
        orm_mode = True





