from pydantic import BaseModel, StrictBool
import datetime


class MovieModel(BaseModel):
    adult: StrictBool
    backdrop_path: str
    genre_ids: list[int]
    id: int
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    release_date: datetime.date
    title: str
    video: StrictBool
    vote_average: float
    vote_count: int


class MovieList(BaseModel):
    movies: list[MovieModel]
