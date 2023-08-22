from pytest_bdd import scenario, given, when, then, parsers
from src.schemas.library import library
from src.schemas.videos import MovieModelLibrary


@scenario(
    scenario_name='Ver um filme de ação',
    feature_name='../features/gender.feature'
)
def test_sucessful_acao():
    pass

@given(
    parsers.cfparse(
        'Um filme com id "{id}" está cadastrado no banco de dados para ação'
    )
)
def mock_film_in_database(id: str):
    library.clear()
    library['acao'][int(id)] = {MovieModelLibrary(
                   id=int(id),
                   name='legal',
                   duration='100 min',
                   gender='acao',
                   year=2023,
                   classification=14,
                   sinopse='Um filme bem legal',
                   imdb=10.0
                   )}
    

@when(
    parsers.cfparse(
        'Um usuário faz uma requisição GET para "{movie_url}"'
    )
)

def send_acao_request(client, context, movie_url):
    response = client.get(movie_url)
    context['response'] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context") 
def check_acao_response_statuscode(context, status_code: str):
    assert context['response'].status_code == int(status_code)
    return context

@then(parsers.cfparse('O JSON da resposta deve conter as informações do filme com id "{id}"'), target_fixture='context')
def check_acao_response_user(context, id:str):
    expected_response = library['acao'][int(id)]
    assert context['response'].json() == expected_response
    return context


@scenario(
    scenario_name='Filme de ação não cadastrado',
    feature_name='../features/gender.feature'
)
def test_acao_nao_resgistrado():
    pass


@given(
    parsers.cfparse('Nenhum filme com id "{id}" está cadastrado no banco de dados para ação')
)
def clear_database(): #garante que não há nenhum filme na database
    library.clear()

@when(
    parsers.cfparse('Um usuário faz uma requisição GET para "{movie_url}"'),
    target_fixture="context"
)

def send_acao_request(client, context, movie_url):
    response = client.get(movie_url)
    context['response'] = response
    return context

@then(parsers.cfparse('O status da resposta deve ser "{status_code}"'), target_fixture='context')
def check_acao_response_statuscode(context, status_code: str):
    assert context['response'].status_code == int(status_code)
    return context

@then(parsers.cfparse('a mensagem de erro deve ser "{error_message}"'), target_fixture='context')
def check_acao_response_errormessage(context, error_message:str):
    assert context['response'].json()["detail"] == error_message
    return context