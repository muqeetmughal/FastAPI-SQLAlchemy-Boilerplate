import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import settings


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
