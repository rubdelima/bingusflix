from pydantic import BaseModel, StrictBool
import datetime


class TVSeriesModel(BaseModel):
    backdrop_path: str
    first_air_date: datetime.date
    genre_ids: list[int]
    id: int
    name: str
    origin_country: list[str]
    original_language: str
    original_name: str
    overview: str
    popularity: float
    poster_path: str
    vote_average: float
    vote_count: int


class TVSeriesList(BaseModel):
    tv_series: list[TVSeriesModel]