from pydantic import BaseModel
from src.schemas.movies import MovieModel
from src.schemas.tv_series import TVSeriesModel
from typing import Union


class GenericMediaModel(BaseModel):
    id: int
    title: str
    vote_average: float
    vote_count: int
    popularity: float


class GenericMediaList(BaseModel):
    medias: list[Union[MovieModel, TVSeriesModel]]
