from pydantic import BaseModel
from datetime import datetime

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

# DataBase

history_db = {}
history_series_db = {}
movies_db = [
    MovieModel(
        id = 7,
        name= 'Star Wars - Uma Nova Esperança', duration= '02:00:00',
        year = 1977, gender = 'Adventure',
        imdb= 8.9, classification=10 ,sinopse='Após os Planos da Estrela da Morte serem pegos surge uma nova esperança'
    ),
    MovieModel(
        id = 8,
        name= 'Star Wars - O Império Contra-Ataca', duration= '02:00:00',
        year = 1980, gender = 'Adventure',
        imdb= 8.9, classification=10 ,sinopse='Após os Planos da Estrela da Morte serem pegos surge uma nova esperança'
    ),
    MovieModel(
        id = 9,
        name= 'Star Wars - O Retorno de Jedi', duration= '02:00:00',
        year = 1983, gender = 'Adventure',
        imdb= 8.9, classification=10 ,sinopse='Após os Planos da Estrela da Morte serem pegos surge uma nova esperança'
    ),
    MovieModel(
        id=10,
        name='Inception',
        duration='02:28:00',
        year=2010,
        gender='Action',
        imdb=8.8,
        classification=14,
        sinopse='A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.'
    ),

    MovieModel(
        id=11,
        name='The Shawshank Redemption',
        duration='02:22:00',
        year=1994,
        gender='Drama',
        imdb=9.3,
        classification=16,
        sinopse='Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'
    ),

    MovieModel(
        id=12,
        name='Pulp Fiction',
        duration='02:34:00',
        year=1994,
        gender='Crime',
        imdb=8.9,
        classification=18,
        sinopse='The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'
    )

]
series_db = [
    SerieModel(
        name='Breaking Bad',
        initial_y=2009,
        gender='Drama',
        serie_seasons=[
            SerieSeason(
                season=1,
                season_episodes= [
                    SerieVideo(
                        id=1,
                        name= '1 - O Inicio de Tudo', duration = '00:54:00',
                        gender= 'Drama', year=2009, classification= 12,
                        sinopse= 'Primeiro episódio dessa jornada incrível',
                        episode=1
                    ),
                    SerieVideo(
                        id=2,
                        name= '2 - O Segundo Episodio', duration = '00:56:00',
                        gender= 'Drama', year=2009, classification= 12,
                        sinopse= 'Primeiro episódio dessa jornada incrível',
                        episode=2
                    )
                ]
            ),
            SerieSeason(
                season=2,
                season_episodes= [
                    SerieVideo(
                        id=3,
                        name= '1 - O Inicio da Segunda Temporada', duration = '00:54:00',
                        gender= 'Drama', year=2010, classification= 0,
                        sinopse= 'Primeiro episódio dessa jornada incrível',
                        episode=1
                    ),
                    SerieVideo(
                        id=4,
                        name= '2 - O Segundo Episodio da Segunda Temporada', duration = '00:56:00',
                        gender= 'Drama', year=2010, classification= 0,
                        sinopse= 'Primeiro episódio dessa jornada incrível',
                        episode=2
                    )
                ]
            )
        ],
    ),
    SerieModel(
        name='One Piece',
        initial_y=1999,
        gender='Adventure',
        serie_seasons= [
            SerieSeason(
                season = 1,
                season_episodes= [
                    SerieVideo(
                        id=5,
                        name= '1 - O Inicio da Segunda Temporada',
                        duration = '00:54:00',
                        gender= 'Drama',
                        year=2010,
                        classification= 0,
                        sinopse= 'Primeiro episódio dessa jornada incrível',
                        episode=1
                    ),
                    SerieVideo(
                        id=6,
                        name= '2 - O Segundo Episodio da Segunda Temporada',
                        duration = '00:56:00',
                        gender= 'Drama',
                        year=2010,
                        classification= 0,
                        sinopse= 'Primeiro episódio dessa jornada incrível',
                        episode=2
                    )
                ]
            )
        ]
    )
]

# Functions DB

def is_series(video_id)->tuple[bool,str,int]:
    for serie in series_db:
        for season in serie.serie_seasons:
            for episode in season.season_episodes:
                if episode.id == video_id:
                    return (True, serie.id, episode.id)
    return (False, None, None)

def get_video(video_id, search='all')->tuple[VideoModel, str, str, int]:
    if search == 'all' or search == 'movie':
        for movie in movies_db:
            if movie.id == video_id:
                return (movie, 'movie', None, movie.id)
    if search == 'all' or search == 'serie':
        for serie in series_db:
            for season in serie.serie_seasons:
                for episode in season.season_episodes:
                    if episode.id == video_id:
                        return (episode, 'serie', serie.name, episode.id)
    return (None, None, None, None)

def getSerieDict(serie : SerieModel, user_profile)->dict:
    last_wc = history_series_db[(user_profile, serie.name)][0]
    serie_videos_id = [episode.id for season in serie.serie_seasons for episode in season.season_episodes]
    next_ep = None
    if last_wc != serie_videos_id[-1]:
        next_ep_id = serie_videos_id[serie_videos_id.index(last_wc)+1]
        next_ep = get_video(next_ep_id, search='serie')[0]
    return {'name' : serie.name, 'gender': serie.gender, 'initial_year' : serie.initial_y,
            'total_seasons' : len(serie.serie_seasons), 
            'last_episode': get_video(last_wc, search='serie')[0], 'next_episode' : next_ep}

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

