from fastapi import APIRouter, HTTPException
from src.schemas.library import library 

router = APIRouter()

arquivo = 'views_ficcao.txt'

try:
    with open(arquivo, 'r') as f:
        views_ficcao = f.read().split(',')
        views_ficcao = [int(item) for item in views_ficcao]
except FileNotFoundError:
      views_ficcao = []

if len(views_ficcao) < len(library['ficcao']):
      for i in range(len(library["ficcao"]) - len(views_ficcao)):
            views_ficcao.append(0)
elif len(views_ficcao) > len(library['ficcao']):
      for i in range(len(views_ficcao) - len(library["ficcao"])):
            del views_ficcao[len(views_ficcao) - 1]

@router.get('/', status_code=200, response_model=dict, tags=['ficcao'])
def read_library():
    return {'ficcao': library['ficcao']}

@router.get('/{id}', response_model=dict, tags=['ficcao'])
def view_details(id: int):
    if id > len(library['ficcao']) or id < 1:
        raise HTTPException(status_code=404, detail='franchise not found')
    
    views_ficcao[id-1] += 1

    with open(arquivo, "w") as f:
        lista_formatada = ",".join(map(str, views_ficcao))
        f.write(lista_formatada)

    return library['ficcao'][id]