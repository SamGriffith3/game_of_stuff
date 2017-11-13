from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
Session = sessionmaker()
session = Session()
engine = create_engine('sqlite:///:memory:', echo=True)

