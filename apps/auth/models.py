import sqlalchemy as sa
from sqlalchemy.orm import relationship
from utils import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    first_name = sa.Column(sa.String(30))
    last_name = sa.Column(sa.String(30))
    phone_number = sa.Column(sa.String(13))
    username = sa.Column(sa.String(50), unique=True, nullable=False)
    email = sa.Column(sa.String(100), unique=True, nullable=False)
    password = sa.Column(sa.String(255))

    is_admin = sa.Column(sa.Boolean, default=False)

   