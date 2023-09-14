from fastapi import APIRouter, HTTPException, Depends

from src.schemas.response import HttpResponseModel, HTTPResponses

from src.api.login import get_logged_user
from src.api.users import database
from src.schemas.user import UserDB
from src.schemas.profile import ProfileModel, ProfileDB, ProfileList
from .users import database

from typing import Annotated

router = APIRouter()

database_profiles = []


# retorna os profiles de um usuario
def get_profiles_by_id(id_user: int):
    profile_list = []

    for profile in database.get('profiles'):
        if profile["id_user"] == id_user:
            profile_list.append(profile)

    return profile_list


# # deleta um profile especifico
# def del_profile(id_profile: int, profile_list: list):
#     profile = profile_list[id_profile-1] # pega esse perfil
    
#     print(profile_list)
#     # ajeita os indexes dos perfis
#     for i in range(id_profile, len(profile_list)):
#         print(f"i: {i}")
#         p = profile_list[i]
#         print("antes")
#         print(p)
#         p["id_profile"] = p["id_profile"] - 1
#         print("depois")
#         print(p)
#         database.put('profiles', i-1, p)
    
#     # o perfil que deve ser deletado foi sobrescrito, agora vamos deletar o ultimo perfil (esta escrito 2 vezes)
#     database.delete('profiles', len(database.get('profiles')) - 1)

#     return profile

# deleta um profile especifico
def del_profile(id_profile: int, profile_list: list):
    profile = profile_list[id_profile-1] # pega esse perfil
    database.delete('profiles', profile["id"]) # deleta do banco de dados
    del profile_list[id_profile-1]

    print(profile_list)
    
    # ajeita os indexes dos perfis
    for i in range(id_profile-1, len(profile_list)):
        p = profile_list[i]
        p["id_profile"] = p["id_profile"] - 1
        database.put('profiles', p["id"], p)

    return profile

# cria um novo profile
@router.post(
    '/', status_code=201, response_model=ProfileDB, tags=['profiles']
)  
async def create_profile(
    profile: ProfileModel, current_user: Annotated[UserDB, Depends(get_logged_user)]
):  
    
    max_id = database.get_greatest_table_id_profile(('profiles'), current_user["id"]) # retorna a quantidade de usuarios

    profile_id = database.get_greatest_table_id_from_profile('profiles') + 1 # retorna o maior id de profile

    if max_id == 3 and current_user["plan"] == 0:
        raise HTTPException(status_code=403, detail='Você atingiu o limite de perfis para seu plano (comum)')
    elif max_id == 7 and current_user["plan"] == 1:
        raise HTTPException(status_code=403, detail='Você atingiu o limite de perfis para seu plano (premium)')
    
    profile_with_id = ProfileDB(**profile.model_dump(), id_profile=max_id+1, id_user=current_user["id"], id=profile_id) # retorna um dicionario com os dados do profile, além do id do usuário e do profile criado

    current_user["active_profile"] = profile_with_id.id_profile # atualiza o perfil ativo do usuário

    dumped_profile = profile_with_id.model_dump()
    database.post('profiles', dumped_profile) # insere no banco de dados
    database.put('users', current_user["id"], current_user) # atualiza o usuário no banco de dados
    
    return ProfileDB(**profile_with_id.model_dump())


# retorna todos os profiles de um usuário
@router.get(
    '/', status_code=200, response_model=ProfileList, tags=['profiles']
)
async def get_profiles(
    current_user: Annotated[UserDB, Depends(get_logged_user)]
):
    profiles = get_profiles_by_id(current_user["id"]) # retorna uma lista com todos os profiles do usuário
    return {'profiles': profiles}


# retorna um perfil especifico de um usuario
@router.get(
    '/{id}', status_code=200, response_model=ProfileDB, tags=['profiles']
)
async def get_profile(
    id:int , current_user: Annotated[UserDB, Depends(get_logged_user)]
):
    profile_list = get_profiles_by_id(current_user["id"]) # retorna uma lista com todos os profiles do usuário

    # garantir que esse profile existe
    if id < 1 or id > len(profile_list):
        raise HTTPException(status_code=404, detail='Profile não encontrado')
    
    profile = profile_list[id-1] # seleciona o profile com o id passado

    return profile


# deleta um profile especificado
@router.delete(
    '/{id}', status_code=200, response_model=ProfileDB, tags=['profiles']
)
async def remove_profile(
    id:int , current_user: Annotated[UserDB, Depends(get_logged_user)]
):
    profile_list = get_profiles_by_id(current_user["id"]) # retorna uma lista com todos os profiles do usuário

    # garantir que esse profile existe
    if id < 1 or id > len(profile_list):
        raise HTTPException(status_code=404, detail='Profile não encontrado')
    
    # garantir que haja mais de um profile
    if len(profile_list) <= 1:
        raise HTTPException(status_code=403, detail='Você não pode deletar seu único profile')
    
    deleted_profile = del_profile(id, profile_list)

    # TODO: ZERAR OS DADOS DELE DOS BANCOS DE DADOS DE FAVORITOS, HISTORICO E MINHA LISTA

    return deleted_profile # remove o profile com o id passado


# edita um perfil
@router.put(
    '/{id}', status_code=200, response_model=ProfileDB, tags=['profiles']
)
async def edit_profile(
    id:int , profile: ProfileModel, current_user: Annotated[UserDB, Depends(get_logged_user)]
):
    profile_list = get_profiles_by_id(current_user["id"]) # retorna uma lista com todos os profiles do usuário

    # garantir que esse profile existe
    # TODO: modularizar essa checagem
    if id < 1 or id > len(profile_list):
        raise HTTPException(status_code=404, detail='Profile não encontrado')

    profile_updated = profile_list[id-1] # seleciona o profile com o id passado

    profile_with_id = ProfileDB(**profile.model_dump(), id_profile=id, id_user=current_user["id"], id=profile_updated["id"]) # retorna um dicionario com os dados do profile, além do id do usuário e do profile criado

    database.put('profiles', profile_updated["id"], profile_with_id.model_dump()) # atualiza o profile no banco de dados

    return profile_with_id # retorna o profile atualizado
