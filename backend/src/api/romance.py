from fastapi import APIRouter, HTTPException
from src.schemas.library import library 

router = APIRouter()

arquivo = 'views_romance.txt'

try:
    with open(arquivo, 'r') as f:
        views_romance = f.read().split(',')
        views_romance = [int(item) for item in views_romance]
except FileNotFoundError:
      views_romance = []

if len(views_romance) < len(library['romance']):
      for i in range(len(library["romance"]) - len(views_romance)):
            views_romance.append(0)
elif len(views_romance) > len(library['romance']):
      for i in range(len(views_romance) - len(library["romance"])):
            del views_romance[len(views_romance) - 1]

@router.get('/', status_code=200, response_model=dict, tags=['romance'])
def read_library():
    return {'romance': library['romance']}

@router.get('/{id}', response_model=dict, tags=['romance'])
def view_details(id: int):
    if id > len(library['romance']) or id < 1:
        raise HTTPException(status_code=404, detail='franchise not found')
    
    views_romance[id-1] += 1

    with open(arquivo, "w") as f:
        lista_formatada = ",".join(map(str, views_romance))
        f.write(lista_formatada)

    return library['romance'][id]