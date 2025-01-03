from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Date

class StorageBase(BaseModel):
    storage_name: str
    storage_type: Optional[str]
    storage_country: Optional[str]
    activity: Optional[str]
    opening_date: Optional[Date]

class StorageCreate(StorageBase):
    pass

class StorageUpdate(StorageBase):
    storage_name: Optional[str] = None

class StorageResponse(StorageBase):
    storage_id: int
    class Config:
        orm_mode = True