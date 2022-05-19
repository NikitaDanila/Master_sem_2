from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'my_db.db')

Base = declarative_base()

engine = create_engine(connection_string, echo=True)

Session = sessionmaker()
