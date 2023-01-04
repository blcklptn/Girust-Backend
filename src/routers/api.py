from fastapi import APIRouter

router = APIRouter(
        prefix = '/api',
        tags = ['API for Girust']
        )

@router.post('/register')
async def register():
    pass

@router.post('/auth')
async def auth():
    pass

@router.post('/refresh_token')
async def refresh():
    pass
