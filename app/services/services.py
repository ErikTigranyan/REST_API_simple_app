from app.db.models import Artist, Storage, Artwork
from app.schemas import ArtistCreate, ArtistUpdate, StorageCreate, StorageUpdate, ArtworkCreate, ArtworkUpdate
from app.services.crud_base import CRUDBase

artist_crud = CRUDBase[Artist, ArtistCreate, ArtistUpdate](Artist, id_field = 'artist_id')
storage_crud = CRUDBase[Storage, StorageCreate, StorageUpdate](Storage, id_field = 'storage_id')
artwork_crud = CRUDBase[Artwork, ArtworkCreate, ArtworkUpdate](Artwork, id_field = 'artwork_id')


