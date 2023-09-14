from fastapi import APIRouter
from src.schemas.library import categories, get_movies

router = APIRouter()

@router.get('/', status_code=200, response_model=dict, tags=['comedia'])
def read_library():
    series = get_movies(categories[2]['path'])
    movies = get_movies(categories[3]['path'])
    return {'Filmes de comédia': movies, 'Séries de comédia': series}



