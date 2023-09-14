from fastapi import APIRouter
from src.schemas.library import categories, get_movies

router = APIRouter()

@router.get('/', status_code=200, response_model=dict, tags=['ficcao'])
def read_library():
    series = get_movies(categories[4]['path'])
    movies = get_movies(categories[5]['path'])
    return {'Filmes de ficção': movies, 'Séries de ficção': series}



