from fastapi import APIRouter, HTTPException

from src.schemas.library import library 

router = APIRouter()

arquivo = 'views_comedia.txt'

try:
    with open(arquivo, 'r') as f:
        views_comedia = f.read().split(',')
        views_comedia = [int(item) for item in views_comedia]
except FileNotFoundError:
      views_comedia = []

if len(views_comedia) < len(library['comedia']):
      for i in range(len(library["comedia"]) - len(views_comedia)):
            views_comedia.append(0)
elif len(views_comedia) > len(library['comedia']):
      for i in range(len(views_comedia) - len(library["comedia"])):
            del views_comedia[len(views_comedia) - 1]

@router.get('/', status_code=200, response_model=dict, tags=['comedia'])
def read_library():
    return {'comedia': library['comedia']}

@router.get('/{id}', response_model=dict, tags=['comedia'])
def view_details(id: int):
    if id > len(library['comedia']) or id < 1:
        raise HTTPException(status_code=404, detail='franchise not found')
    
    views_comedia[id-1] += 1

    with open(arquivo, "w") as f:
        lista_formatada = ",".join(map(str, views_comedia))
        f.write(lista_formatada)

    return library['comedia'][id]