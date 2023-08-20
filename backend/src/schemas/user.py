from pydantic import BaseModel, EmailStr, PastDate, StrictBool


class UserModel(BaseModel):
    name: str
    surname: str
    email: EmailStr
    passwd: str
    birthdate: PastDate
    plan: StrictBool
    active_profile: int = 1


class UserModelPublic(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    birthdate: PastDate
    plan: StrictBool
    active_profile: int


class UserList(BaseModel):
    users: list[UserModelPublic]


class UserDB(UserModel):
    id: int
