from fastapi import APIRouter, HTTPException
from requests.models import HTTPError
from src.db.db_mananger import Db_manager

from src.schemas.response import HttpResponseModel, HTTPResponses
from src.schemas.user import UserDB, UserList, UserModel, UserModelPublic
router = APIRouter()

database = Db_manager("http://localhost:4000")

#database = 


@router.post(
    '/', status_code=201, response_model=UserModelPublic, tags=['users']
)
def create_user(user: UserModel):
    user_with_id = UserDB(**user.model_dump(), id=database.get_greatest_table_id('users') + 1)
    database.post('users', user_with_id)

    return UserModelPublic(**user_with_id.model_dump())


@router.get('/', status_code=200, response_model=UserList, tags=['users'])
def read_user():
    return {'users': database.get('users')}


@router.put('/{user_id}', response_model=UserModelPublic, tags=['users'])
def update_user(user_id: int, user: UserModel):
    try:
        # user_with_id = UserModel(**user.model_dump(), id=user_id)
        database.put("users", user_id, user.model_dump())
    except HTTPError: 
        raise HTTPException(status_code=404, detail='User not found')

    # database[user_id - 1] = user_with_id

    return UserModelPublic(**user.model_dump(), id=user_id)


@router.delete('/{user_id}', response_model=HttpResponseModel, tags=['users'])
def delete_user(user_id: int):
    try:
        database.delete("users", user_id)
    except HTTPError: 
        raise HTTPException(
            status_code=HTTPResponses.USER_NOT_FOUND().status_code,
            detail=HTTPResponses.USER_NOT_FOUND().message,
        )

    return HTTPResponses.USER_DELETED()
