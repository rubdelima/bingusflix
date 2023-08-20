from fastapi import APIRouter

from src.api import users
from src.api import login
from src.api import account_recovery
from src.api import profiles
from src.api import favorites

api_router = APIRouter()
api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(login.router, prefix='/login', tags=['login'])
api_router.include_router(account_recovery.router, prefix='/account_recovery', tags=['account recovery'])
api_router.include_router(profiles.router, prefix='/profiles', tags=['profiles'])
api_router.include_router(favorites.router, prefix='/favorites', tags=['favorites'])