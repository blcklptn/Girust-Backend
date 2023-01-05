from pydantic import BaseModel

class User(BaseModel):
    login: str
    password: str

class RefreshToken(BaseModel):
    refresh_token: str