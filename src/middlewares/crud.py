from sqlalchemy.orm import Session
from models.pydantic_models import Users
from typing import Union

async def register(user: Users, db: Session) -> dict:
    try:
        db.add(user)
        db.commit()
        return {'content': 'Done!'}
    except Exception as ex:
        return {'error': ex}

async def check_user(user_login: str, db: Session) -> Users:
    try:
        user = db.query(Users).filter(Users.login == user_login).one()
        return user
    except:
        return