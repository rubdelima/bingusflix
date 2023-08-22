from fastapi import APIRouter, HTTPException
from src.schemas.library import library 

router = APIRouter()

arquivo = 'views_suspense.txt'

try:
    with open(arquivo, 'r') as f:
        views_suspense = f.read().split(',')
        views_suspense = [int(item) for item in views_suspense]
except FileNotFoundError:
      views_suspense = []

if len(views_suspense) < len(library['suspense']):
      for i in range(len(library["suspense"]) - len(views_suspense)):
            views_suspense.append(0)
elif len(views_suspense) > len(library['suspense']):
      for i in range(len(views_suspense) - len(library["suspense"])):
            del views_suspense[len(views_suspense) - 1]

@router.get('/', status_code=200, response_model=dict, tags=['suspense'])
def read_library():
    return {'suspense': library['suspense']}

@router.get('/{id}', response_model=dict, tags=['suspense'])
def view_details(id: int):
    if id > len(library['suspense']) or id < 1:
        raise HTTPException(status_code=404, detail='franchise not found')
    
    views_suspense[id-1] += 1

    with open(arquivo, "w") as f:
        lista_formatada = ",".join(map(str, views_suspense))
        f.write(lista_formatada)

    return library['suspense'][id]