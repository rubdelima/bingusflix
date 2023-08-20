from pydantic import BaseModel


class FavoriteModel(BaseModel):
    id_video: int


class FavoriteDB(FavoriteModel):
    id_user: int
    id_profile: int
    id_favorite: int


class FavoriteList(BaseModel):
    favorites: list[FavoriteDB]