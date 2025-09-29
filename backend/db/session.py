from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from dotenv import load_dotenv
env_path = Path(__file__).parent.parent/".env"
load_dotenv(dotenv_path=env_path)




print("hello")









from core.config import settings
SQLALCHEMY_DATABASE_URL="sqlite:///.sql_app.db"
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})

SESSIONLOCAL=sessionmaker(autoflush=False,bind=engine)