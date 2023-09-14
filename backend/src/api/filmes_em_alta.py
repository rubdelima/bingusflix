from fastapi import APIRouter
from src.schemas.library import categories, get_movies

router = APIRouter()

@router.get('/', status_code=200, response_model=dict, tags=['filmesEmAlta'])
def read_library():
    movies = get_movies(categories[11]['path'])
    return {'Filmes em alta': movies}



