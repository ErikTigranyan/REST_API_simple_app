from pydantic import BaseModel
from typing import Optional
from sqlalchemy import DECIMAL


class ArtworkBase(BaseModel):
    artwork_name: str
    artwork_type: Optional[str]
    material: Optional[str]
    price: Optional[DECIMAL]
    height: Optional[DECIMAL]
    width: Optional[DECIMAL]
    depth: Optional[DECIMAL]
    artist_id: int
    storage_id: int

class ArtworkCreate(ArtworkBase):
    pass

class ArtworkUpdate(ArtworkBase):
    artwork_name: Optional[str] = None

class ArtworkResponse(ArtworkBase):
    artwork_id: int
    class Config:
        orm_mode = True
