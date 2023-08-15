from fastapi import APIRouter

from api import users
from api import login
from api import account_recovery

api_router = APIRouter()
api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(login.router, prefix='/login', tags=['login'])
api_router.include_router(account_recovery.router, prefix='/account_recovery', tags=['account recovery'])