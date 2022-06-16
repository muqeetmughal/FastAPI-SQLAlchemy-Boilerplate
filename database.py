import os
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from dependencies import return_db
from settings import settings
import datetime
import sqlalchemy as sa

engine = create_engine(settings.DATABASE_URI,
                       convert_unicode=True,
                       echo=False,
                       # connect_args={"check_same_thread": False
                       #               }
                       )

SessionLocal = sessionmaker(autocommit=False, bind=engine, autoflush=False)

Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)



class TimeStampMixin:
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.datetime.utcnow)
    deleted_at = sa.Column(sa.DateTime)


class CRUD(TimeStampMixin):

    db = return_db()

    # def save(self):
    #     if self.id == None:
    #         self.db.sesion.add(self)
    #     return self.db.sesion.commit()

    # def delete(self):
    #     self.db.sesion.delete(self)
    #     return self.db.sesion.commit()

    @classmethod
    def find(cls, **kwargs):

        
        if kwargs:
            return cls.db.sesion.query(cls).filter_by(**kwargs).first()
        raise HTTPException(status_code=400, detail="Id or keyword argument missing following /")

    @classmethod
    def findAll(cls, **kwargs):

        if kwargs:
            return cls.db.query(cls).filter_by(**kwargs).all()
        else:
            return cls.db.query(cls).all()



class BaseModel(Base, CRUD):
    __abstract__ = True
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
