from fastapi import APIRouter
from src.schemas.library import categories, get_movies

router = APIRouter()

@router.get('/', status_code=200, response_model=dict, tags=['acao'])
def read_library():
    series = get_movies(categories[0]['path'])
    movies = get_movies(categories[1]['path'])
    return {'Filmes de ação': movies, 'Séries de ação': series}



