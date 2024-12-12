from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()
app.include_router(router)

# app/main.py
from fastapi import FastAPI
from app.api.routes import router as api_router  # Import routes

# Initialize the FastAPI app
app = FastAPI()

# Include the API routes
app.include_router(api_router)
