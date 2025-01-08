from fastapi import FastAPI
from app.db import init_db
from app.api.routes import router
import logging

logger = logging.getLogger('app_logger')
logging.basicConfig(level=logging.INFO)

logger.info('Application started!')
app = FastAPI()
app.include_router(router)

def main():
    try:
        logger.info('Initializing database...')
        init_db()
        logger.info('Database is successfully initialized!')

        logger.info('Starting FastApi application...')
    except Exception as e:
        logger.error(f"Error during application startup: {e}")

if __name__ == '__main__':
    main()
