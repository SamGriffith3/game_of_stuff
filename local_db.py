from sqlalchemy import create_engine, Integer, Column, String, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


association_table = Table('association', Base.metadata,
    Column('users_id', Integer, ForeignKey('users.id')),
    Column('game_data_id', Integer, ForeignKey('game_data.id')))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    games = relationship(
        "GameData",
        secondary=association_table,
        back_populates="users")

  
class GameData(Base):
    __tablename__ = 'game_data'

    id = Column(Integer, primary_key=True)
    flip_card = Column(Boolean)
    users = relationship(
        "User",
        secondary=association_table,
        back_populates="games")


class Cards(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    card = Column(String)
    rating = Column(String)