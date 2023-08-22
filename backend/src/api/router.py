from fastapi import APIRouter

from src.api import users
from src.api import login
from src.api import account_recovery
from src.api import profiles
from src.api import favorites
from src.api import my_list
from src.api import acao
from src.api import comedia
from src.api import ficcao
from src.api import romance
from src.api import suspense
from src.api import series_em_alta
from src.api import filmes_em_alta


api_router = APIRouter()
api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(login.router, prefix='/login', tags=['login'])
api_router.include_router(account_recovery.router, prefix='/account_recovery', tags=['account recovery'])
api_router.include_router(profiles.router, prefix='/profiles', tags=['profiles'])
api_router.include_router(favorites.router, prefix='/favorites', tags=['favorites'])
api_router.include_router(my_list.router, prefix='/my-list', tags=['my-list'])
api_router.include_router(acao.router, prefix= '/acao', tags=['acao'])
api_router.include_router(comedia.router, prefix= '/comedia', tags=['comedia'])
api_router.include_router(romance.router, prefix= '/romance', tags=['romance'])
api_router.include_router(ficcao.router, prefix= '/ficcao', tags=['ficcao'])
api_router.include_router(suspense.router, prefix= '/suspense', tags=['suspense'])
api_router.include_router(series_em_alta.router, prefix= '/seriesEmAlta', tags=['seriesEmAlta'])
api_router.include_router(filmes_em_alta.router, prefix= '/filmesEmAlta', tags=['filmesEmAlta'])