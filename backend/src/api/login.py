from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.user import UserDB
from schemas.tokenresponse import TokenResponse
from .users import database

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # esquema de autenticação por token

async def get_logged_user(token: Annotated[str, Depends(oauth2_scheme)]): 
    for user in database: # procura o dicionário do usuário na base de dados baseado no username digitado
        if user.id == int(token):
            return user

@router.post( # rota para realizar o login de um usuário
        "/", status_code=201  , response_model=TokenResponse, tags=["login"]
) 
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    for user in database: # procura um usuário com email e senha iguais ao do formulário
        if user.email == form_data.username:
            if user.passwd == form_data.password:
                return TokenResponse(access_token=str(user.id), token_type="bearer") # se encontrar, ele recebe um token equivalente ao seu ID
            else:
                raise HTTPException(status_code=401, detail="Wrong password") # se a senha for incorreta: erro 401
    
    raise HTTPException(status_code=404, detail="User not found") # se não encontrar o usuário: erro 404


# EXEMPLO DE UMA FUNÇÃO QUE DEPENDE DO USUÁRIO ESTAR LOGADO:

'''@router.get("/me")  
async def read_users_me(current_user: Annotated[UserDB, Depends(get_logged_user)]):
    return current_user'''
