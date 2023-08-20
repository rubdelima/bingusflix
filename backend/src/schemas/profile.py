from pydantic import BaseModel, EmailStr, PastDate, StrictBool


class ProfileModel(BaseModel):
    nickname: str
    pg: int
    language: str


class ProfileDB(ProfileModel):
    id_profile: int
    id_user: int


class ProfileList(BaseModel):
    profiles: list[ProfileDB]
