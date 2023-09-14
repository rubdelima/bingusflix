from fastapi import APIRouter
from src.schemas.library import categories, get_movies

router = APIRouter()

@router.get('/', status_code=200, response_model=dict, tags=['seriesEmAlta'])
def read_library():
    series = get_movies(categories[10]['path'])
    return {'Séries em alta': series}



