from fastapi import APIRouter, Depends
from models.abstract_models import User, RefreshToken
from models.pydantic_models import Users
from middlewares import crud, jwt_bearer
from middlewares.create_tokens import signJWT, decodeJWT
from database.db import get_db
from sqlalchemy.orm import Session
from core.security import get_password_hash, verify_password

router = APIRouter(
        prefix = '/api',
        tags = ['API for Girust']
        )

@router.post('/register')
async def register(user: User, db: Session = Depends(get_db)) -> dict:
    hashed_password = get_password_hash(user.password)
    new_user = Users (
        login = user.login,
        password_hash = hashed_password
    )
    return await crud.register(user=new_user, db=db)


@router.post('/auth')
async def auth(user: User, db: Session = Depends(get_db)) -> dict:
    user_ch: object = await crud.check_user(user.login, db=db)
    if not user:
        return {'error', 'user not found'}
    if not verify_password(user.password, user_ch.password_hash):
        return {'error', 'password incorrect'}
    return await signJWT(user.login)
    

@router.post('/refresh_token')
async def refresh(rt: RefreshToken):
    user: dict = await decodeJWT(rt.refresh_token)
    print(user)
    return await signJWT(user['UserID'])

