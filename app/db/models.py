from base import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()
class Artist(Base):
    pass

class Piece_of_art(Base):
    pass

class Storage_location(Base):
    pass