import os
from pydantic import BaseSettings

class Settings(BaseSettings):

    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    # DATABASE_URI = "mysql+pymysql://root:@localhost/fastapi_boilerplate"
    # DATABASE_URI = "mysql+pymysql://root:12345678@localhost:3307/fastapiauth"
    DATABASE_URI = 'sqlite:///sqlite.db'
    SECRET_KEY = "hiuy7GUI7yIBUi89yilu6k9U8O7ukFO9hhi76kki8N8hnreyw6bvyudsbyusdug"

    ALGORITHM = "HS256"

settings = Settings()