import requests
from pydantic import BaseModel

class VideoModelAPI(BaseModel):
    video_type : str
    video_values : dict

class VideoInfoPost(BaseModel):
    video_type : str
    movie_id: int 
    serie_id : int 
    season : int 
    episode : int 

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
        vm = VideoModelAPI(video_type=video_info.video_type, video_values=response.json())
        return (True, vm)
    return(False, None)

movieModelExample = VideoInfoPost(video_type='movie', movie_id=346698, serie_id=None, season=None, episode=None)
serieModelExample = VideoInfoPost(video_type='serie', movie_id=None, serie_id = 37854, season = 21, episode=892)

_, movie_example = getVideoDataAPI(video_info=movieModelExample)
_, serie_example = getVideoDataAPI(serieModelExample)

print(_)


