from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from decimal import Decimal
from datetime import date
from app.db.models import Artist, Storage, Artwork
from app.db import Base, SessionLocal

db_url = 'mysql+mysqlconnector://V:asxlkm11@localhost/artdb'

engine = create_engine(db_url)

def add_artist(session: Session, full_name: str, dob: date, country: str, movement: str):
    try:
        existing_artist = session.query(Artist).filter_by(full_name=full_name, dob=dob, country=country, movement=movement).first()
        if not existing_artist:
            new_artist = Artist(
                full_name=full_name,
                dob=dob,
                country=country,
                movement=movement
            )
            session.add(new_artist)
            session.commit()
            return new_artist
        return existing_artist
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Error adding artist: {e}')
        raise

def add_storage(session: Session, storage_name: str, storage_type: str, storage_country: str, opening_date: date):
    try:
        existing_storage = session.query(Storage).filter_by(
            storage_name=storage_name, storage_type=storage_type, storage_country=storage_country, opening_date=opening_date
        ).first()
        if not existing_storage:
            new_storage = Storage(
                storage_name=storage_name,
                storage_type=storage_type,
                storage_country=storage_country,
                opening_date=opening_date
            )
            session.add(new_storage)
            session.commit()
            return new_storage
        return existing_storage
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Error adding storage: {e}')
        raise

def add_artwork(session: Session, artwork_name: str, artwork_type: str, medium: str, price: Decimal, height: Decimal, width: Decimal, depth: Decimal, artist_id: int, storage_id: int):
    try:
        existing_artwork = session.query(Artwork).filter_by(
            artwork_name=artwork_name,
            artwork_type=artwork_type,
            medium=medium,
            price=price,
            height=height,
            width=width,
            depth=depth,
            artist_id=artist_id,
            storage_id=storage_id
        ).first()
        if not existing_artwork:
            new_artwork = Artwork(
                artwork_name=artwork_name,
                artwork_type=artwork_type,
                medium=medium,
                price=price,
                height=height,
                width=width,
                depth=depth,
                artist_id=artist_id,
                storage_id=storage_id
            )
            session.add(new_artwork)
            session.commit()
            return new_artwork
        return existing_artwork
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Error adding artwork: {e}')
        raise

def main():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        artist_1 = add_artist(db, 'Francisco Goya', date(1746, 3, 30), 'Spain', 'Romanticism')
        storage_1 = add_storage(db, 'Lázaro Galdiano Museum', 'Art gallery', 'Madrid', date(1951, 1, 27))
        artwork_1 = add_artwork(db, 'Witches Sabbath', 'Painting', 'Oil on canvas', None, Decimal('43.00'), Decimal('30.00'), None, artist_1.artist_id, storage_1.storage_id)

        print('Successfully added the data!')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        db.close()

if __name__ == '__main__':
    main()