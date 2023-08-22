from pydantic import BaseModel

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
    serie_seasons : list[SerieSeason]

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