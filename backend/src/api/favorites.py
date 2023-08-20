from fastapi import APIRouter, HTTPException, Depends

from src.schemas.response import HttpResponseModel, HTTPResponses

from src.api.login import get_logged_user
from src.api.users import database
from src.schemas.user import UserDB
from src.schemas.profile import ProfileModel, ProfileDB, ProfileList
from src.schemas.favorite import FavoriteModel, FavoriteDB, FavoriteList

from typing import Annotated

router = APIRouter()

database_favorites = []


# retorna todos os favorites de um usuário
def get_favorites_by_id(id_user:int, id_profile:int):
    favorites_list = []

    for favorite in database_favorites:
        if favorite.id_user == id_user and favorite.id_profile == id_profile:
            favorites_list.append(favorite)
    
    return favorites_list


# deleta um favorite especifico
def del_favorite(id_favorite: int):
    favorite = database_favorites.pop(id_favorite)

    for i in range(id_favorite, len(database_favorites)):
        database_favorites[i].id_favorite -= 1

    return favorite

# adiciona um video aos favoritos
@router.post(
    '/', status_code=201, response_model=FavoriteDB, tags=['favorites']
)
async def add_favorite(
    favorite: FavoriteModel, current_user: Annotated[UserDB, Depends(get_logged_user)]
):
    favorite_video = FavoriteDB(**favorite.model_dump(), id_user=current_user.id, id_profile=current_user.active_profile, id_favorite=len(get_favorites_by_id(current_user.id, current_user.active_profile)) + 1)

    database_favorites.append(favorite_video)
    return favorite_video


# retorna todos os favorites de um usuário
@router.get(
    '/', status_code=200, response_model=FavoriteList, tags=['favorites']
)
async def get_favorites(
    current_user: Annotated[UserDB, Depends(get_logged_user)]
):
    favorite_list = get_favorites_by_id(current_user.id, current_user.active_profile) # retorna uma lista com todos os favorites do usuário

    return {'favorites': favorite_list}


# retorna um favorite especifico
@router.get(
    '/{id_favorite}', status_code=200, response_model=FavoriteDB, tags=['favorites']
)
async def get_favorite(
    id_favorite: int, current_user: Annotated[UserDB, Depends(get_logged_user)]
):
    favorite_list = get_favorites_by_id(current_user.id, current_user.active_profile) # retorna uma lista com todos os favorites do usuário

    # garantir que esse favorite exista
    if id_favorite < 1 or id_favorite > len(favorite_list):
        raise HTTPException(status_code=404, detail='Favorite não encontrado')

    favorite = favorite_list[id_favorite-1] # seleciona o favorite com o id passado

    return favorite


# deleta um favorite especifico
@router.delete(
    '/{id_favorite}', status_code=200, response_model=FavoriteDB, tags=['favorites']
)
async def remove_favorite(
    id_favorite: int, current_user: Annotated[UserDB, Depends(get_logged_user)]
):
    favorite_list = get_favorites_by_id(current_user.id, current_user.active_profile) # retorna uma lista com todos os favorites do usuário

    # garantir que esse favorite exista
    if id_favorite < 1 or id_favorite > len(favorite_list):
        raise HTTPException(status_code=404, detail='Favorite não encontrado')
    
    favorite = del_favorite(id_favorite - 1)

    return favorite