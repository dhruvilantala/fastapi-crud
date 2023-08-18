from typing import Union,Optional
from fastapi import FastAPI, Path, HTTPException, status, Depends
from crud import schemas
from crud import models
from crud.database import engine, get_db
from sqlalchemy.orm import Session
from crud.routers import item
import uvicorn


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# List of routers
routes = [item]  # Add more routers if needed

for route in routes:
    app.include_router(route.router)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)