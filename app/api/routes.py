from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas import ArtistCreate, ArtistUpdate, StorageCreate, StorageUpdate, ArtworkCreate, ArtworkUpdate
from app.services.services import artist_crud, storage_crud, artwork_crud
from typing import List
from app.utils.logger import logger
router = APIRouter()

#Helper function to add routes dynamically
def generate_routes(router, crud_service, schema_create, schema_update, prefix: str):
    @router.post(f'/{prefix}/', response_model = schema_create)
    def create_item(item: schema_create, db: Session = Depends(get_db)):
        existing_item = crud_service.get(db, id = item.id)
        if existing_item:
            logger.warning(f'{prefix.capitalize()} with ID {item.id} already exists.')
            raise HTTPException(status_code = 400, detail = f'{prefix.capitalize()} with this ID already exists')
        logger.info(f'Creating {prefix} with ID {item.id}')
        return crud_service.create(db, obj_in = item)

    @router.get(f'/{prefix}/{{item_id}}', response_model = schema_create)
    def get_item(item_id: int, db: Session = Depends(get_db)):
        obj = crud_service.get(db, id = item_id)
        if not obj:
            logger.warning(f'{prefix.capitalize()} with ID {item_id} not found.')
            raise HTTPException(status_code = 404, detail = f'{prefix.capitalize()} not found')
        logger.info(f'Fetched {prefix} with ID {item_id}')
        return obj

    @router.get(f'/{prefix}/', response_model = List[schema_create])
    def get_items(skip: int = 0, limit: int = Query(10, le=100), db: Session = Depends(get_db)):
        logger.info(f'Fetching {prefix}s with skip={skip} and limit={limit}')
        return crud_service.get_all(db, skip = skip, limit=limit)

    @router.put(f'/{prefix}/{{item_id}}', response_model = schema_update)
    def update_item(item_id: int, item: schema_update, db: Session = Depends(get_db)):
        db_obj = crud_service.get(db, id = item_id)
        if not db_obj:
            logger.warning(f'{prefix.capitalize()} with ID {item_id} not found for update.')
            raise HTTPException(status_code = 404, detail = f'{prefix.capitalize()} not found')
        if item.price and item.price <= 0:
            logger.warning(f'Invalid price {item.price} for {prefix} with ID {item_id}.')
            raise HTTPException(status_code = 400, detail = 'Price must be greater than 0')
        logger.info(f'Updating {prefix} with ID {item_id}')
        return crud_service.update(db, db_obj = db_obj, obj_in = item)

    @router.delete(f'/{prefix}/{{item_id}}', response_model = schema_create)
    def delete_item(item_id: int, db: Session = Depends(get_db)):
        obj = crud_service.get(db, id = item_id)
        if not obj:
            logger.warning(f'{prefix.capitalize()} with ID {item_id} not found for deletion.')
            raise HTTPException(status_code = 404, detail = f'{prefix.capitalize()} not found')
        logger.info(f'Deleting {prefix} with ID {item_id}')
        return crud_service.delete(db, id = item_id)

# Generate routes for each model
generate_routes(router, artist_crud, ArtistCreate, ArtistUpdate, 'artists')
generate_routes(router, storage_crud, StorageCreate, StorageUpdate, 'storages')
generate_routes(router, artwork_crud, ArtworkCreate, ArtworkUpdate, 'artworks')