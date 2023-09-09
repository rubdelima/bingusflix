from fastapi import APIRouter, HTTPException

from src.schemas.response import HttpResponseModel, HTTPResponses
from src.schemas.user import UserDB, UserList, UserModel, UserModelPublic

router = APIRouter()

database = []


@router.post(
    '/', status_code=201, response_model=UserModelPublic, tags=['users']
)
def create_user(user: UserModel):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)

    return UserModelPublic(**user_with_id.model_dump())


@router.get('/', status_code=200, response_model=UserList, tags=['users'])
def read_user():
    return {'users': database}


@router.put('/{user_id}', response_model=UserModelPublic, tags=['users'])
def update_user(user_id: int, user: UserModel):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')

    user_with_id = UserModel(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return UserModelPublic(**user_with_id.model_dump(), id=user_id)


@router.delete('/{user_id}', response_model=HttpResponseModel, tags=['users'])
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPResponses.USER_NOT_FOUND().status_code,
            detail=HTTPResponses.USER_NOT_FOUND().message,
        )

    del database[user_id - 1]

    return HTTPResponses.USER_DELETED()
