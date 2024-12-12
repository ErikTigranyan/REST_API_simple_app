from .base import Base, engine, SessionLocal
from .models import Artist, Artwork, Storage  # Ваши модели

#Initializing db
Base.metadata.create_all(bind=engine)
