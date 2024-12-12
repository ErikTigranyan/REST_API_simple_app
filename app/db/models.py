from app.db.base import Base
from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey

class Artist(Base):
    __tablename__ = "artist"

    artist_id = Column(Integer, primary_key = True, index = True)
    full_name = Column(String, nullable = False)
    dob = Column(Date, nullable = False)
    country = Column(String, nullable = False)
    activity = Column(String, nullable = False)

class Storage(Base):
    __tablename__ = "storage"

    storage_id = Column(Integer, primary_key = True, index = True)
    storage_name = Column(String, nullable = False)
    storage_type = Column(String, nullable = False)
    storage_country = Column(String, nullable = False)
    opening_date = Column(Date, nullable = False)

class Artwork(Base):
    __tablename__ = "artwork"

    artwork_id = Column(Integer, primary_key = True, index = True)
    artwork_name = Column(String, nullable = False)
    artwork_type = Column(String, nullable = False)
    material = Column(String, nullable = True)
    price = Column(DECIMAL(10, 2), nullable = False)
    height = Column(DECIMAL(10, 2), nullable = False)
    width = Column(DECIMAL(10, 2), nullable = False)
    depth = Column(DECIMAL(10, 2), nullable = True)
    artist_id = Column(Integer, ForeignKey('artist.artist_id'), nullable = False)
    storage_id = Column(Integer, ForeignKey('storage.storage_id'), nullable = False)
