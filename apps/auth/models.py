import sqlalchemy as sa
from sqlalchemy.orm import relationship
from database import BaseModel
from dependencies import get_db, return_db
from sqlalchemy.orm import Session

class User(BaseModel):
    __tablename__ = "users"

    name = sa.Column(sa.String(75))
    phone_number = sa.Column(sa.String(13))
    username = sa.Column(sa.String(50), unique=True, nullable=False)
    email = sa.Column(sa.String(100), unique=True, nullable=True)
    password = sa.Column(sa.String(255))

    is_admin = sa.Column(sa.Boolean, default=False)


    @classmethod
    async def get_user(cls, username):
        db = return_db()
        query = db.query(cls).filter_by(username=username).first()
        return query

    def verify_password(self, password):
        return True

   