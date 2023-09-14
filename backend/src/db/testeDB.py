from db_mananger import Db_manager
from pydantic import BaseModel
import requests

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MzRhZWEzNDk4MTM4MTYxZjdjMTc1Mzk3YmM1YTgzNiIsInN1YiI6IjY0ZmIzNjQxYTI4NGViMDExZDVmNDdiOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lPrDEfSG8Cbi4DsH5Q1W1ho1bJvN9_Iw3blu3jE01fU"
}

class TvModel(BaseModel):
    serie_id : int
    serie_name: str
    len_seasons : int
    last_episode_season : int
    last_episode_number : int
    next_episode_season : int | None
    next_episode_number : int | None

db = Db_manager("http://127.0.0.1:4000")


def getHistory(history_id):
    history = db.get("watched")
    history = [h for h in history if h['id'] == history_id]
    if len(history) == 0 :
        new_history = {"id" : history_id, "movie" : [] , "tv" : []}
        db.post("watched", {"id" : history_id, "movie" : [] , "tv" : []})
        return new_history
    return history[0]

def getTvData(tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}?language=pt-BR"
    response = requests.get(url, headers=headers)
    return response.json()

def getSeasonData(tv_id, season_n):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_n}?language=pt-BR"
    response = requests.get(url, headers=headers)
    return response.json()

def getTvModel():
    h = getHistory(11)
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
        

getTvModel()