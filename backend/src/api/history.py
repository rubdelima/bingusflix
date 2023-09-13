from fastapi import APIRouter, Depends, HTTPException
from src.schemas.user import UserDB
from pydantic import BaseModel
from typing import Annotated, List
from src.api.login import get_logged_user
from src.schemas.videos import VideoModel, MovieModel, MovieList, SerieModel, VideoTime, VideoTimeList, history_db, movies_db, series_db, history_series_db, get_video, getSerieDict, VideoModelAPI, getVideoDataAPI, VideoInfoPost
from datetime import datetime
import requests

router = APIRouter()
# Rotas de POST para quando o usuário clicar no vídeo ele ser adicionado no banco de dados
# @router.post("/register_access_video/", 
#              status_code=201, tags=['history'], response_model= VideoModel)
# async def register_access(n_video_id: int, 
#                           user: Annotated [UserDB, Depends(get_logged_user)], 
#                          ):
#     video, video_type, serie_name, video_id = get_video(n_video_id)

#     url = f"https://api.themoviedb.org/3/movie/{n_video_id}?language=pt-BR"
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MzRhZWEzNDk4MTM4MTYxZjdjMTc1Mzk3YmM1YTgzNiIsInN1YiI6IjY0ZmIzNjQxYTI4NGViMDExZDVmNDdiOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lPrDEfSG8Cbi4DsH5Q1W1ho1bJvN9_Iw3blu3jE01fU"
#     }

#     response = requests.get(url, headers=headers)
#     print(response.text)

#     if video_type is not None:
#         # Inserindo no Banco de Dados de Vídeos
#         video = VideoTime(**video.model_dump(), watched_at=datetime.now())
#         if (user.id, user.active_profile) not in history_db.keys():
#             history_db[(user.id, user.active_profile)] = [video]
#         else:
#             history_db[(user.id, user.active_profile)].insert(0,video) # Adiciona no inicio da fila
#         # Inserindo no Banco de Dados de Series do Usuário
#         if video_type == 'serie':
#             if (user.id, serie_name) not in history_series_db.keys():
#                 history_series_db[((user.id, user.active_profile), serie_name)] = [video_id]
#             else:
#                 history_series_db[((user.id, user.active_profile), serie_name)].insert(0,video_id)
#         return video
#     else:
#         raise HTTPException(status_code=404, detail='Não existe esse filme no Banco de Dados da Plataforma')

@router.post("/register_access_video/", 
            status_code=201, tags=['history'], response_model= VideoModelAPI)
async def register_access(video_info:VideoInfoPost,
                          user: Annotated [UserDB, Depends(get_logged_user)], 
                         ):
    response, model = getVideoDataAPI(video_info)
    if response:
        if (user.id, user.active_profile) not in history_db.keys():
            history_db[(user.id, user.active_profile)] = {'movie':[], 'serie' : []}        
        history_db[(user.id, user.active_profile)][model.video_type].insert(0,model)
        return model
    else:
        raise HTTPException(status_code=404, detail='Não existe esse video no Banco de Dados da Plataforma')
    

# Rota para GET para exibir o histórico todo e mais um para trazer só os dos 10 primeiros
@router.get("/",status_code=200, response_model=VideoTimeList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)]):
    return {'videos' : history_db.get((user.id, user.active_profile), [])}

# Rota para GET para exibir o histórico de apenas 10 vídeos
@router.get("/only10/",status_code=200, response_model=VideoTimeList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)], init:int=0, final:int=10):
    videos_h =  history_db.get((user.id, user.active_profile), [])
    videos_h = [videos_h[i] for i in range(len(videos_h)) if  init<=i < final]
    return {'videos' :videos_h}

# Rota para GET para exibir o histórico de Filmes
@router.get("/movies/",status_code=200, response_model=MovieList)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)]):
    movies_h =  history_db.get((user.id, user.active_profile), [])
    movies_h = [video.id for video in movies_h]
    watched_mv = [movie for movie in movies_db if movie.id in movies_h]
    return {'movies' :watched_mv}

# Rota para GET para exibir um ceto filme procurado
@router.get("/movies/{movie_name}/",status_code=200, response_model=MovieModel)
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)], 
                      movie_name : str):
    movies_h =  history_db.get((user.id, user.active_profile), [])
    movies_h = [video.id for video in movies_h]
    watched_mv = [movie for movie in movies_db if movie.id in movies_h and movie.name == movie_name]
    if len(watched_mv) > 0 :
        return watched_mv[0]
    else:
        raise HTTPException(status_code=404, detail= "Filme não encontrado no histórico")

# Rota para GET oara exibir o Histórico de Séries
@router.get("/series/",status_code=200, response_model=List[dict])
async def get_history(user: Annotated [UserDB, Depends (get_logged_user)]):
    watched_sr_n = [k[1] for k in history_series_db if k[0] == (user.id, user.active_profile)]
    watched_sr = [serie for serie in series_db if serie.name in watched_sr_n]
    watched_sr_dl = [getSerieDict(serie, (user.id, user.active_profile)) for serie in watched_sr]
    return watched_sr_dl