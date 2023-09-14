from fastapi import APIRouter
from src.schemas.library import categories, get_movies

router = APIRouter()

@router.get('/', status_code=200, response_model=dict, tags=['suspense'])
def read_library():
    series = get_movies(categories[8]['path'])
    movies = get_movies(categories[9]['path'])
    return {'Filmes de suspense': movies, 'Séries de suspense': series}



