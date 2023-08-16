from pydantic import BaseModel, EmailStr, PastDate, StrictBool


class ProfileModel(BaseModel):
    nickname: str
    pg: int
    language: str


class ProfileList(BaseModel):
    users: list[ProfileModel]


class ProfileDB(ProfileModel):
    id_profile: int
    id_user: int
