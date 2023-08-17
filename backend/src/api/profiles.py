from fastapi import APIRouter, HTTPException, Depends

from src.schemas.response import HttpResponseModel, HTTPResponses

from src.api.login import get_logged_user
from src.api.users import database
from src.schemas.user import UserDB, UserList, UserModel, UserModelPublic
from src.schemas.profile import ProfileModel, ProfileDB, ProfileList
from typing import Annotated

router = APIRouter()

database_profiles = []


# retorna os profiles de um usuario
def get_profiles_by_id(id_profile: int):
    profile_list = []

    for profile in database_profiles:
        if profile.id_user == id_profile:
            profile_list.append(profile)

    return profile_list


# cria um novo profile
@router.post(
    '/', status_code=201, response_model=ProfileDB, tags=['profiles']
)  
async def create_profile(
    profile: ProfileModel, current_user: Annotated[UserDB, Depends(get_logged_user)]
):  
    user_profiles = get_profiles_by_id(current_user.id) # retorna uma lista com todos os profiles do usuário

    if len(user_profiles) == 3 and current_user.plan == 0:
        raise HTTPException(status_code=403, detail='Você atingiu o limite de perfis para seu plano (comum)')
    elif len(user_profiles) == 7 and current_user.plan == 1:
        raise HTTPException(status_code=403, detail='Você atingiu o limite de perfis para seu plano (premium)')
    
    profile_with_id = ProfileDB(**profile.model_dump(), id_profile=len(user_profiles) + 1, id_user=current_user.id) # retorna um dicionario com os dados do profile, além do id do usuário e do profile criado
    
    
    database_profiles.append(profile_with_id)   # insere no banco de dados
    return profile_with_id


