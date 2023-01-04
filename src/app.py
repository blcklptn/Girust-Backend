from fastapi import FastAPI
from routers import api

app: object = FastAPI()
app.include_router(api.router)
