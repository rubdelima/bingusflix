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


def getVideoDataAPI(video_info:VideoInfoPost)->tuple[bool, VideoModelAPI|None]:
    if video_info.video_type == "movie":
        url = f"https://api.themoviedb.org/3/movie/{video_info.movie_id}?language=pt-BR"
    else:
        url = f"https://api.themoviedb.org/3/tv/{video_info.serie_id}/season/{video_info.season}/episode/{video_info.episode}?language=pt-BR"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MzRhZWEzNDk4MTM4MTYxZjdjMTc1Mzk3YmM1YTgzNiIsInN1YiI6IjY0ZmIzNjQxYTI4NGViMDExZDVmNDdiOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lPrDEfSG8Cbi4DsH5Q1W1ho1bJvN9_Iw3blu3jE01fU"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        vm = VideoModelAPI(video_type=video_info.video_type, video_values=response.json(), watched_at=str(dt.datetime.now()))
        return (True, vm)
    return(False, None)

# DataBase

history_db = {}
history_series_db = {}

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

