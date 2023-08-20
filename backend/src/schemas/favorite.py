from pydantic import BaseModel


class FavoriteModel(BaseModel):
    id_profile: int
    id_user: int
    id_video: int


class FavoriteList(BaseModel):
    favorites: list[FavoriteModel]