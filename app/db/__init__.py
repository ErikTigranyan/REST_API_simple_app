from .base import Base, engine, SessionLocal
from .models import Artist, Artwork, Storage
from sqlalchemy.orm import Session
from datetime import date
import logging

logger = logging.getLogger('app_loger')

#adding default data for artist and storage
def add_placeholders(session: Session):
    try:
        placeholder_artist = session.query(Artist).filter_by(full_name = 'Unknown Artist').first()
        if not placeholder_artist:
            placeholder_artist = Artist(
                full_name = 'Unknown Artist',
                dob = date(1000, 1, 1),
                country = 'Unknown',
                movement = 'Unknown'
            )
            session.add(placeholder_artist)

        placeholder_storage = session.query(Storage).filter_by(storage_name = 'Unknown Storage').first()
        if not placeholder_storage:
            placeholder_storage = Storage(
                storage_name = 'Unknown Storage',
                storage_type = 'Unknown',
                storage_country = 'Unknown',
                opening_date = date(1000, 1, 1)
            )
            session.add(placeholder_storage)

        session.commit()
        logger.info('Placeholders added successfully!')
    except Exception as e:
        logger.error(f'Error while adding placeholders: {e}')

#function for getting DB's session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#initializing db
def init_db():
    try:
        logger.info('Creating database tables...')
        Base.metadata.create_all(bind = engine)

        with Session(engine) as session:
            add_placeholders(session)

        logger.info('Database initialized successfully!')
    except Exception as e:
        logger.error(f'Error while initializing database: {e}')