from fastapi import APIRouter, Depends, HTTPException
from src.schemas.user import UserDB
from pydantic import BaseModel
from typing import Annotated, List
from src.api.login import get_logged_user
from src.schemas.videos import  VideoAPIList, VideoModelAPI, VideoInfoPost, TvModel, TvList
import requests
import datetime as dt

from src.db.db_mananger import Db_manager
db = Db_manager("http://localhost:4000")

headers_tmdb = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MzRhZWEzNDk4MTM4MTYxZjdjMTc1Mzk3YmM1YTgzNiIsInN1YiI6IjY0ZmIzNjQxYTI4NGViMDExZDVmNDdiOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lPrDEfSG8Cbi4DsH5Q1W1ho1bJvN9_Iw3blu3jE01fU"
}

def getHistory(history_id):
    history = db.get("watched")
    history = [h for h in history if h['id'] == history_id]
    if len(history) == 0 :
        new_history = {"id" : history_id, "movie" : [] , "tv" : []}
        db.post("watched", {"id" : history_id, "movie" : [] , "tv" : []})
        return new_history
    return history[0]

def getVideoDataAPI(video_info:VideoInfoPost)->tuple[bool, VideoModelAPI|None]:
    if video_info.video_type == "movie":
        url = f"https://api.themoviedb.org/3/movie/{video_info.movie_id}?language=pt-BR"
    else:
        url = f"https://api.themoviedb.org/3/tv/{video_info.serie_id}/season/{video_info.season}/episode/{video_info.episode}?language=pt-BR"
    response = requests.get(url, headers=headers_tmdb)
    if response.status_code == 200:
        vm = VideoModelAPI(video_type=video_info.video_type, video_values=response.json(), watched_at=str(dt.datetime.now()))
        if video_info.video_type == 'tv':
            vm.video_values['tv_id'] = video_info.serie_id
        return (True, vm)
    return(False, None)

def getTvData(tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}?language=pt-BR"
    response = requests.get(url, headers=headers_tmdb)
    return response.json()

def getSeasonData(tv_id, season_n):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_n}?language=pt-BR"
    response = requests.get(url, headers=headers_tmdb)
    return response.json()

def getTvModel(user_profile_id:int)->list[TvModel]:
    h = getHistory(user_profile_id)
    series = h['tv']

    last_episode = {}

    for i in series:
        tv_id = i['video_values']['tv_id'] 
        season_number = i['video_values']['season_number']
        episode_number = i['video_values']['episode_number']
        if  tv_id not in last_episode.keys():
            last_episode[tv_id] = (season_number, episode_number)
        elif season_number > last_episode[tv_id][0]:
            last_episode[tv_id] = (season_number, episode_number)
        elif episode_number > last_episode[tv_id][1] and season_number == last_episode[tv_id][0]:
            last_episode[tv_id] = (season_number, episode_number)
    
    tvs_arr = []

    for serie_id in last_episode.keys():
        serieData = getTvData(serie_id)
        seasonData = getSeasonData(serie_id, last_episode[serie_id][0])
        next_season_number = seasonData['season_number']
        if seasonData['episodes'][-1]['episode_number'] == last_episode[serie_id][1]: # se for o ultimo episodio da teemporada
            if seasonData['season_number'] == serieData['number_of_seasons']: # se for a ultima temporada
                next_season_number = None
                next_espisode_number = None
            else:
                next_season_number =+ 1
                next_season_data = getSeasonData(i, next_season_number)
                next_espisode_number = next_season_data['episodes'][0]['episode_number']
        else:
            for i in range(len(seasonData['episodes'])):
                if seasonData['episodes'][i-1]['episode_number'] == last_episode[serie_id][1]:
                    next_espisode_number = seasonData['episodes'][i]['episode_number']
                    break
        tvM = TvModel(serie_id=serie_id, serie_name=serieData['name'], len_seasons=serieData['number_of_seasons'],
                      last_episode_season=last_episode[serie_id][0], last_episode_number=last_episode[serie_id][1],
                      next_episode_season=next_season_number, next_episode_number=next_espisode_number)
        tvs_arr.append(tvM)

    return tvs_arr
    
router = APIRouter()

@router.post("/register_access_video/", 
            status_code=201, tags=['history'], response_model= VideoModelAPI)
async def register_access(video_info:VideoInfoPost,
                          user: Annotated [UserDB, Depends(get_logged_user)], 
                         ):
    response, model = getVideoDataAPI(video_info)
    if response:
        history_id = int(f"{user['id']}{user['active_profile']}")
        history = getHistory(history_id)
        history[video_info.video_type].append(model.model_dump())       
        db.put("watched", history_id, history)
        return model
    else:
        raise HTTPException(status_code=404, detail='Não existe esse video no Banco de Dados da Plataforma')
    

# Rota para GET para exibir o histórico todo e mais um para trazer só os dos 10 primeiros
@router.get("/",status_code=200, response_model=VideoAPIList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)]):
    try:
        history_id = int(f"{user['id']}{user['active_profile']}")
        history = getHistory(history_id)
        videos = history['movie'] + history['tv']
        videos.sort(key=lambda x: x['watched_at'], reverse=True)
        videos = [VideoModelAPI(**v) for v in videos]
        return {'videos' : videos}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail= "Você não possui filme e séries no banco de dados")

# Rota para GET para exibir o histórico de apenas 10 vídeos
@router.get("/only10/",status_code=200, response_model=VideoAPIList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)], init:int=0, final:int=10):
    try:
        history_id = int(f"{user['id']}{user['active_profile']}")
        history = getHistory(history_id)
        videos = history['movie'] + history['tv']
        videos = [videos[i] for i in range(len(videos)) if  init<=i < final]
        videos = [VideoModelAPI(**v) for v in videos]
        return {'videos' : videos}
    except :
        raise HTTPException(status_code=404, detail= "Você não possui filme e séries no banco de dados")

# Rota para GET para exibir o histórico de Filmes
@router.get("/movies/",status_code=200, response_model=VideoAPIList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)]):
    try:
        history_id = int(f"{user['id']}{user['active_profile']}")
        history = getHistory(history_id)
        videos = history['movie']
        videos = [VideoModelAPI(**v) for v in videos]
        return {'videos' : videos}
    except:
        raise HTTPException(status_code=404, detail= "Você não possui filme e séries no banco de dados")

# Rota para GET para exibir um certo filme procurado
@router.get("/movies/{movie_name}/",status_code=200, response_model=VideoModelAPI)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)], 
                      movie_name : str):
    try:
        history_id = int(f"{user['id']}{user['active_profile']}")
        history = getHistory(history_id)
        videos = history['movie']
        videos = [VideoModelAPI(**v) for v in videos]
        watched_mv = [movie for movie in videos if  movie.video_values['title'] == movie_name]
        if len(watched_mv) > 0 :
            return watched_mv[0]
        else:
            raise HTTPException(status_code=404, detail= "Filme não encontrado no histórico")
    except:
        raise HTTPException(status_code=404, detail= "Você não possui filme e séries no banco de dados")

# Rota para GET oara exibir o Histórico de Séries
@router.get("/series/",status_code=200, response_model=TvList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)]):
    try:
        history_id = int(f"{user['id']}{user['active_profile']}")
        videos = getTvModel(history_id)
        return {'series' : videos}
    except:
        raise HTTPException(status_code=404, detail= "Você não possui séries no banco de dados")