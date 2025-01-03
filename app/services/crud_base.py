from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, Optional, List
from pydantic import BaseModel

ModelType = TypeVar('ModelType')
CreateSchemaType = TypeVar('CreateSchemaType', bound = BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound = BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], id_field: str = 'id'):
        self.model = model
        self.id_field = id_field

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj = self.model(**obj_in.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        id_column = getattr(self.model, self.id_field)
        return db.query(self.model).filter(id_column == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 10) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def update(self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        for field, value in obj_in.model_dump(exclude_unset = True).items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id: int) -> Optional[ModelType]:
        id_column = getattr(self.model, self.id_field)
        obj = db.query(self.model).filter(id_column == id).first()
        if obj:
            db.delete(obj)
            db.commit()
        return obj