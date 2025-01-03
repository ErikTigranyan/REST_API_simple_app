from fastapi import FastAPI
from app.db import Base, engine
from app.api.routes import router
from app.utils.logger import logger

Base.metadata.create_all(bind = engine)
app = FastAPI()
app.include_router(router, prefix = '/api')