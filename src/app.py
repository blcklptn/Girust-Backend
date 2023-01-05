from fastapi import FastAPI
from routers import api
from database.db import Base, engine
from models.pydantic_models import *

Base.metadata.create_all(bind=engine)

app: object = FastAPI()
app.include_router(api.router)
