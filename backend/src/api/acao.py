from fastapi import APIRouter, HTTPException
from src.schemas.library import library

router = APIRouter()

arquivo = 'views_acao.txt'

try:
    with open(arquivo, 'r') as f:
        views_acao = f.read().split(',')
        views_acao = [int(item) for item in views_acao]
except FileNotFoundError:
      views_acao = []

if len(views_acao) < len(library['acao']):
      for i in range(len(library["acao"]) - len(views_acao)):
            views_acao.append(0)
elif len(views_acao) > len(library['acao']):
      for i in range(len(views_acao) - len(library["acao"])):
            del views_acao[len(views_acao) - 1]

@router.get('/', status_code=200, response_model=dict, tags=['acao'])
def read_library():
    return {'ação': library['acao']}

@router.get('/{id}', response_model=dict, tags=['acao'])
def view_details(id: int):
    if id > len(library['acao']) or id < 1:
        raise HTTPException(status_code=404, detail='franchise not found')
    
    views_acao[id-1] += 1

    with open(arquivo, "w") as f:
        lista_formatada = ",".join(map(str, views_acao))
        f.write(lista_formatada)

    return library['acao'][id]

