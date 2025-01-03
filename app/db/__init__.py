from .base import Base, engine, SessionLocal
from .models import Artist, Artwork, Storage
from sqlalchemy.orm import Session

#initializing db
Base.metadata.create_all(bind=engine)

#function for getting DB's session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()