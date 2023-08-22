from fastapi import APIRouter
from src.schemas.library import library

router = APIRouter()

@router.get('/', status_code=200, response_model=list, tags=['seriesEmAlta'])
def read_seriesEmAlta():
    arquivo = 'views_acao.txt'

    try:
        with open(arquivo, 'r') as f:
            views_acao = f.read().split(',')
            views_acao = [int(item) for item in views_acao]
    except FileNotFoundError:
        views_acao = []

    arquivo = 'views_comedia.txt'

    try:
        with open(arquivo, 'r') as f:
            views_comedia = f.read().split(',')
            views_comedia = [int(item) for item in views_comedia]
    except FileNotFoundError:
        views_comedia = []
    
    arquivo = 'views_ficcao.txt'

    try:
        with open(arquivo, 'r') as f:
            views_ficcao = f.read().split(',')
            views_ficcao = [int(item) for item in views_ficcao]
    except FileNotFoundError:
        views_ficcao = []

    arquivo = 'views_romance.txt'

    try:
        with open(arquivo, 'r') as f:
            views_romance = f.read().split(',')
            views_romance = [int(item) for item in views_romance]
    except FileNotFoundError:
        views_romance = []

    arquivo = 'views_suspense.txt'

    try:
        with open(arquivo, 'r') as f:
            views_suspense = f.read().split(',')
            views_suspense = [int(item) for item in views_suspense]
    except FileNotFoundError:
        views_suspense = []

    views = []

    for nome, lista in [
        ('acao', views_acao),
        ('comedia', views_comedia),
        ('ficcao', views_ficcao),
        ('romance', views_romance),
        ('suspense', views_suspense)
    ]:
        for idx, valor in enumerate(lista):
            views.append((valor, idx, nome))
    
    top10 = []
    for i in range(len(views)):
        if len(library[views[i][2]][views[i][1] + 1]) == 3:
            top10.append(views[i])

    top10.sort(reverse=True)

    top10 = top10[:10]
    emAlta = []
    for i in range(len(top10)):
        emAlta.append(library[top10[i][2]][top10[i][1] + 1])
    return emAlta
