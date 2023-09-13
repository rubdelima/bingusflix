from fastapi import APIRouter, Depends, HTTPException
from src.schemas.user import UserDB
from pydantic import BaseModel
from typing import Annotated, List
from src.api.login import get_logged_user
from src.schemas.videos import  VideoTimeList, history_db,  VideoAPIList, VideoModelAPI, getVideoDataAPI, VideoInfoPost
from datetime import datetime
import requests
import datetime as dt

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

router = APIRouter()

@router.post("/register_access_video/", 
            status_code=201, tags=['history'], response_model= VideoModelAPI)
async def register_access(video_info:VideoInfoPost,
                          user: Annotated [UserDB, Depends(get_logged_user)], 
                         ):
    response, model = getVideoDataAPI(video_info)
    if response:
        if (user.id, user.active_profile) not in history_db.keys():
            history_db[(user.id, user.active_profile)] = {'movie':[], 'tv' : []}        
        history_db[(user.id, user.active_profile)][model.video_type].insert(0,model)
        return model
    else:
        raise HTTPException(status_code=404, detail='Não existe esse video no Banco de Dados da Plataforma')
    

# Rota para GET para exibir o histórico todo e mais um para trazer só os dos 10 primeiros
@router.get("/",status_code=200, response_model=VideoAPIList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)]):
    try:
        videos = history_db[(user.id, user.active_profile)].get('movie', []) + history_db[(user.id, user.active_profile)].get('tv', [])
        videos.sort(key=lambda x: x.watched_at, reverse=True)
        return {'videos' : videos}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail= "Você não possui filme e séries no banco de dados")

# Rota para GET para exibir o histórico de apenas 10 vídeos
@router.get("/only10/",status_code=200, response_model=VideoAPIList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)], init:int=0, final:int=10):
    try:
        videos = history_db[(user.id, user.active_profile)].get('movie', [])
        videos = [videos[i] for i in range(len(videos)) if  init<=i < final]
        return {'videos' : videos}
    except :
        raise HTTPException(status_code=404, detail= "Você não possui filme e séries no banco de dados")

# Rota para GET para exibir o histórico de Filmes
@router.get("/movies/",status_code=200, response_model=VideoAPIList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)]):
    try:
        videos = history_db[(user.id, user.active_profile)].get('movie', [])
        return {'videos' : videos}
    except:
        raise HTTPException(status_code=404, detail= "Você não possui filme e séries no banco de dados")

# Rota para GET para exibir um certo filme procurado
@router.get("/movies/{movie_name}/",status_code=200, response_model=VideoModelAPI)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)], 
                      movie_name : str):
    movies_h =  history_db.get((user.id, user.active_profile), [])
    watched_mv = [movie for movie in movies_h if movie.video_type == "movie" and movie.video_values['title'] == movie_name]
    if len(watched_mv) > 0 :
        return watched_mv[0]
    else:
        raise HTTPException(status_code=404, detail= "Filme não encontrado no histórico")

# Rota para GET oara exibir o Histórico de Séries
@router.get("/series/",status_code=200, response_model=VideoAPIList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)]):
    try:
        videos = history_db[(user.id, user.active_profile)].get('movie', [])
        return {'videos' : videos}
    except:
        raise HTTPException(status_code=404, detail= "Você não possui filme e séries no banco de dados")