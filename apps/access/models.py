import sqlalchemy as sa
from sqlalchemy.orm import relationship
from utils import BaseModel
from database import Base

roles_permissions_association_table = sa.Table('roles_permissions', Base.metadata,
                                               sa.Column(
                                                   'role_id', sa.ForeignKey('roles.id')),
                                               sa.Column('permission_id', sa.ForeignKey(
                                                   'permissions.id'))
                                               )
class Role(BaseModel):
    __tablename__ = "roles"
    name = sa.Column(sa.String(50), nullable=False)
    role_for = sa.Column(sa.String(50),  nullable=False)
    permissions = relationship("Permission",
                               secondary=roles_permissions_association_table)

    def __repr__(self) -> str:
        return f"(Role: {self.name}, For: {self.role_for})"


class Permission(BaseModel):
    __tablename__ = "permissions"
    name = sa.Column(sa.String(50), nullable=False, unique=True)
    code = sa.Column(sa.String(50), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"(Permission: {self.code})"