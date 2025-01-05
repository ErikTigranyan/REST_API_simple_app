from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class ArtworkBase(BaseModel):
    artwork_name: str
    artwork_type: Optional[str]
    material: Optional[str]
    price: Optional[Decimal]
    height: Optional[Decimal]
    width: Optional[Decimal]
    depth: Optional[Decimal]
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
