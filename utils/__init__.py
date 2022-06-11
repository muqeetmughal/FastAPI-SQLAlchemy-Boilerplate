from database import Base
import sqlalchemy as sa
class BaseModel(Base):
    __abstract__ = True
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
