from fastapi import APIRouter
from src.schemas.library import categories, get_movies

router = APIRouter()

@router.get('/', status_code=200, response_model=dict, tags=['romance'])
def read_library():
    series = get_movies(categories[6]['path'])
    movies = get_movies(categories[7]['path'])
    return {'Filmes de romance': movies, 'Séries de romance': series}



