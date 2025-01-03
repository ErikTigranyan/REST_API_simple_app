from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Date

class ArtistBase(BaseModel):
    full_name: str
    dob: Optional[Date]
    country: Optional[str]
    activity: Optional[str]

class ArtistCreate(ArtistBase):
    pass

class ArtistUpdate(ArtistBase):
    full_name: Optional[str] = None

class ArtistResponse(ArtistBase):
    artist_id: int
    class Config:
        orm_mode = True