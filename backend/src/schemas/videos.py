from pydantic import BaseModel
from datetime import datetime
import requests
import datetime as dt

# Class Definition
class VideoModel(BaseModel):
    id : int
    name : str
    duration : str
    gender : str
    year : int
    classification : int
    sinopse : str

class VideoList(BaseModel):
    videos : list[VideoModel]

class MovieModel(VideoModel):
    imdb : float

class MovieList(BaseModel):
    movies : list[MovieModel]

class SerieVideo(VideoModel):
    episode : int

class SerieSeason(BaseModel):
    season : int
    season_episodes : list[SerieVideo]

class SerieModel(BaseModel):
    name : str
    gender : str
    initial_y : int
    serie_seasons : list[SerieSeason]


class VideoTime(VideoModel):
    watched_at: datetime

class VideoTimeList(BaseModel):
    videos : list[VideoTime]

class VideoModelAPI(BaseModel):
    video_type : str
    video_values : dict
    watched_at : str

class VideoAPIList(BaseModel):
    videos : list[VideoModelAPI]

class VideoInfoPost(BaseModel):
    video_type : str
    movie_id: int | None
    serie_id : int | None
    season : int | None
    episode : int | None

class TvModel(BaseModel):
    serie_id : int
    serie_name: str
    len_seasons : int
    last_episode_season : int
    last_episode_number : int
    next_episode_season : int | None
    next_episode_number : int | None

class TvList(BaseModel):
    series : list[TvModel]

class MovieModelLibrary(BaseModel):
    id: int
    name: str
    duration: str
    gender: str
    year: int
    classification: int
    sinopse : str
    imdb: float

class SerieModelLibrary(BaseModel):
    id: int
    name: str
    serie_seasons: dict

