from sqlalchemy import create_engine, Integer, Column, String, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


association_table = Table('association', Base.metadata,
    Column('users_id', Integer, ForeignKey('users.user_id')),
    Column('game_data_id', Integer, ForeignKey('game_data.id')))


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(80))
    games = relationship(
        "GameData",
        secondary=association_table,
        back_populates="users")

  
class GameData(Base):
    __tablename__ = 'game_data'

    game_id = Column(Integer, primary_key=True)
    flip_card = Column(Boolean)
    users = relationship(
        "User",
        secondary=association_table,
        back_populates="games")


class Cards(Base):
    __tablename__ = 'cards'

    card_id = Column(Integer, primary_key=True)
    card = Column(String(80))
    rating = Column(String(2))



