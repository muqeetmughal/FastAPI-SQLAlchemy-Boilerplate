from typing import List
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from database import BaseModel
from dependencies import get_db, return_db
from sqlalchemy.orm import Session
from apps.access.models import Permission


class User(BaseModel):
    __tablename__ = "users"

    name = sa.Column(sa.String(75))
    phone_number = sa.Column(sa.String(13))
    username = sa.Column(sa.String(50), unique=True, nullable=False)
    email = sa.Column(sa.String(100), unique=True, nullable=True)
    password = sa.Column(sa.String(255))

    is_superuser = sa.Column(sa.Boolean, default=False)

    permissions = relationship("Permission", secondary='user_permissions')

    roles = relationship("Role", secondary='user_roles')


    @classmethod
    async def get_user(cls, username):
        db = return_db()
        query = db.query(cls).filter_by(username=username).first()
        return query

    def verify_password(self, password):
        return True

    @property
    def all_permissions(self):

        permissions = self.permissions

        for role in self.roles:
            permissions.extend(role.permissions)
        return set([permission.code for permission in permissions])

    def has_permission(self, perm_codes:List[str]):
        perm_codes : set = set(perm_codes)
        if perm_codes.issubset(self.all_permissions):
            return True
        else:
            return False