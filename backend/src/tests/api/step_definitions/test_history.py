from pytest_bdd import scenario, given, when, then, parsers
from src.schemas.user import UserDB
from src.api.users import database as db
from src.schemas.videos import get_video
import json

def pass_user_profile(client, user_id, user_email, user_psw ):
    db.clear()
    db.append(UserDB(
        id=int(user_id),
        name="Nome",
        surname="Sobrenome",
        email=user_email,
        birthdate="2000-01-01",  
        plan=True,
        passwd=user_psw
    ))

    login_response = client.post(
        '/login/',
        data = {
            "username" : user_email,
            "password" : user_psw
        }
    )
    access_token = login_response.json()['access_token']
    profile_post = client.post(
        '/profiles/',
        json = {
            "nickname" : "fred",
            "pg" : 16,
            "language" : "pt-br",
        },
        headers={'Authorization' : f'Bearer {access_token}'}
    )
    return client, access_token

# Scenario 1

@scenario(
    scenario_name='Inserção de um Filme que está presente no Banco de Dados',
    feature_name= '../features/history.feature'
)
def test_successful_put_in_history():
    pass

@given(
    parsers.cfparse(
        'um profile de id "{profile_id}" do usuário com id "{user_id}" e e-mail "{user_email}" e senha "{user_password}" está cadastrado no sistema',
    )
)
def mock_user_in_database(client, context, user_id: str, user_email: str, user_password: str, profile_id: str):
    # adiciona o usuário na base de dados (condição anterior ao teste)
    client,context['access_token'] =  pass_user_profile(client, user_id, user_email, user_password)
    return context

@when(
    parsers.cfparse(
    'o usuário envia uma requisição POST para "{post_url}" com o video "{n_video_id}"'
    ),target_fixture="context"
)
def send_post_history_request(client, context, post_url: str, n_video_id: str):
    response = client.post(
        post_url, params={"n_video_id" :int(n_video_id)},
        headers={'Authorization' : f'Bearer {context["access_token"]}'})
    context["response"] = response
    return context

@then(
    parsers.cfparse('recebo o status da resposta "{cod_resp}"'),
    target_fixture="context"
)
def check_code_history_post(client, context, cod_resp :str):
    assert context["response"].status_code == int(cod_resp)
    return context
@then(
    parsers.cfparse(
    'o JSON da resposta deve conter dados relacionados ao video "{video_id}"'),
    target_fixture="context"
)
def check_pst_history_video(client, context, video_id:str):
    expected_video = json.loads(get_video(int(video_id))[0].model_dump_json())
    response_dict =  context["response"].json()
    for key in response_dict.keys():
        assert expected_video[key] == response_dict[key]


# Scenario 2

@scenario(
    scenario_name='Obter todo o histórico de um Profile',
    feature_name= '../features/history.feature'
)
def test_successful_get_history():
    pass

@given(
    parsers.cfparse(
        'um profile de id "{profile_id}" do usuário com id "{user_id}" e e-mail "{user_email}" e senha "{user_password}" está cadastrado no sistema',
    )
)
def mock_user_in_database2(client, context, user_id: str, user_email: str, user_password: str, profile_id: str):
    # adiciona o usuário na base de dados (condição anterior ao teste)
    client,context['access_token'] =  pass_user_profile(client, user_id, user_email, user_password,)
    return context
@given(
    parsers.cfparse(
        'ele tem os videos de "{first_vd}" a "{last_vd}" no seu histórico',
    )
)
def mock_videos_in_database2(client, context, first_vd: str, last_vd: str):
    # adiciona 12 videos no bd do user-profile
    first_vd, last_vd = int(first_vd), int(last_vd)
    for video in range(first_vd,last_vd+1):
            response = client.post(
                '/history/register_access_video/', params={"n_video_id" :video},
                headers={'Authorization' : f'Bearer {context["access_token"]}'})
            assert response.status_code == 201
    return context

@when(
    parsers.cfparse(
    'o usuário envia uma requisição GET para "{get_url}"'
    ),target_fixture="context"
)
def send_get_history_videos2(client, context, get_url: str):
    response = client.get(
        get_url, headers={'Authorization' : f'Bearer {context["access_token"]}'})
    context["response"] = response
    return context

@then(
    parsers.cfparse('recebo o status da resposta "{cod_resp}"'),
    target_fixture="context"
)
def check_code_history_post2(client, context, cod_resp :str):
    assert context["response"].status_code == int(cod_resp)
    return context
@then(
    parsers.cfparse(
    'o JSON da resposta deve conter uma lista com dados relacionados a todos os {list_size} videos assistidos'),
    target_fixture="context"
)
def check_pst_history_video2(client, context, list_size:str):
    response_dict =  context["response"].json()
    assert len(response_dict['videos']) == int(list_size)


scenario1_3 = '''
# Scenario 3

@scenario(
    scenario_name='Obter apenas 10 videos do histórico de um Profile',
    feature_name= '../features/history.feature'
)
def test_successful_get_only10_in_history():
    pass

@given(
    parsers.cfparse(
        'um profile de id "{profile_id}" do usuário com id "{user_id}" e e-mail "{user_email}" e senha "{user_password}" está cadastrado no sistema',
    )
)
def mock_user_in_database10(client, context, user_id: str, user_email: str, user_password: str, profile_id: str):
    # adiciona o usuário na base de dados (condição anterior ao teste)
    client,context['access_token'] =  pass_user_profile(client, user_id, user_email, user_password,)
    return context
@given(
    parsers.cfparse(
        'ele tem os videos de "{first_vd}" a "{last_vd}" no seu histórico',
    )
)
def mock_videos_in_database10(client, context, first_vd: str, last_vd: str):
    # adiciona 12 videos no bd do user-profile
    first_vd, last_vd = int(first_vd), int(last_vd)
    for video in range(first_vd,last_vd+1):
            response = client.post(
                '/history/register_access_video/', params={"n_video_id" :video},
                headers={'Authorization' : f'Bearer {context["access_token"]}'})
            assert response.status_code == 201
    return context

@when(
    parsers.cfparse(
    'o usuário envia uma requisição GET para "{get_url}" com parametros init "{init}" e final "{final}"'
    ),target_fixture="context"
)
def send_get_history_videos10(client, context, get_url: str, init:str, final:str):
    response = client.get(
        get_url, headers={'Authorization' : f'Bearer {context["access_token"]}'},
        params = {'init' : int(init), 'final' : int(final)})
    context["response"] = response
    return context

@then(
    parsers.cfparse('recebo o status da resposta "{cod_resp}"'),
    target_fixture="context"
)
def check_code_history_post10(client, context, cod_resp :str):
    assert context["response"].status_code == int(cod_resp)
    return context
@then(
    parsers.cfparse(
    'o JSON da resposta deve conter uma lista com dados relacionados a todos os "{list_size}" ultimos videos assistidos'),
    target_fixture="context"
)
def check_pst_history_video10(client, context, list_size:str):
    list_size = [i for i in list_size if i in ['1','0']]
    list_size = ''.join(list_size)
    list_size = 10
    response_dict =  context["response"].json()
    assert len(response_dict['videos']) == int(list_size)

'''
# Scenario 4

@scenario(
    scenario_name='Obter o histórico de filmes um Profile',
    feature_name= '../features/history.feature'
)
def test_successful_get_movies():
    pass

@given(
    parsers.cfparse(
        'um profile de id "{profile_id}" do usuário com id "{user_id}" e e-mail "{user_email}" e senha "{user_password}" está cadastrado no sistema',
    )
)
def mock_user_in_database(client, context, user_id: str, user_email: str, user_password: str, profile_id: str):
    # adiciona o usuário na base de dados (condição anterior ao teste)
    client,context['access_token'] =  pass_user_profile(client, user_id, user_email, user_password,)
    return context
@given(
    parsers.cfparse(
        'ele tem os filmes "{film1}" e "{film2}" no seu histórico',
    )
)
def mock_videos_in_database(client, context, film1: str, film2: str):
    # adiciona 12 videos no bd do user-profile
    films = [int(film1), int(film2)]
    for video in films:
            response = client.post(
                '/history/register_access_video/', params={"n_video_id" :video},
                headers={'Authorization' : f'Bearer {context["access_token"]}'})
            assert response.status_code == 201
    return context

@when(
    parsers.cfparse(
    'o usuário envia uma requisição GET para "{get_url}"'
    ),target_fixture="context"
)
def send_get_history_movie(client, context, get_url: str):
    response = client.get(
        get_url, headers={'Authorization' : f'Bearer {context["access_token"]}'})
    context["response"] = response
    return context

@then(
    parsers.cfparse('recebo o status da resposta "{cod_resp}"'),
    target_fixture="context"
)
def check_code_movie_get(client, context, cod_resp :str):
    assert context["response"].status_code == int(cod_resp)
    return context
@then(
    parsers.cfparse(
    'o JSON da resposta deve conter uma lista com os filmes "{film1}" e "{film2}"'),
    target_fixture="context"
)
def check_pst_history_movie(client, context, film1:str, film2:str):
    response_dict =  context["response"].json()
    for movie in response_dict['movies']:
        assert int(movie['id']) in (int(film1),int(film2))



# Scenario 5

@scenario(
    scenario_name='Obter infos de um filme do historico',
    feature_name= '../features/history.feature'
)
def test_successful_get_mov():
    pass

@given(
    parsers.cfparse(
        'um profile de id "{profile_id}" do usuário com id "{user_id}" e e-mail "{user_email}" e senha "{user_password}" está cadastrado no sistema',
    )
)
def mock_user_in_database(client, context, user_id: str, user_email: str, user_password: str, profile_id: str):
    # adiciona o usuário na base de dados (condição anterior ao teste)
    client,context['access_token'] =  pass_user_profile(client, user_id, user_email, user_password,)
    return context
@given(
    parsers.cfparse(
        'ele tem os filmes "{film1}" e "{film2}" no seu histórico',
    )
)
def mock_videos_in_database(client, context, film1: str, film2: str):
    # adiciona 12 videos no bd do user-profile
    films = [int(film1), int(film2)]
    for video in films:
            response = client.post(
                '/history/register_access_video/', params={"n_video_id" :video},
                headers={'Authorization' : f'Bearer {context["access_token"]}'})
            assert response.status_code == 201
    return context

@when(
    parsers.cfparse(
    'o usuário envia uma requisição GET para "{get_url}"'
    ),target_fixture="context"
)
def send_get_history_movie(client, context, get_url: str):
    response = client.get(
        get_url, headers={'Authorization' : f'Bearer {context["access_token"]}'})
    context["response"] = response
    return context

@then(
    parsers.cfparse('recebo o status da resposta "{cod_resp}"'),
    target_fixture="context"
)
def check_code_movie_get(client, context, cod_resp :str):
    assert context["response"].status_code == int(cod_resp)
    return context
@then(
    parsers.cfparse(
    'o JSON da resposta deve conter informacões sobre o filme "{film_id}" como name "{film_name}".'),
    target_fixture="context"
)
def check_pst_history_movie(client, context, film_id:str, film_name):
    response_dict =  context["response"].json()
    assert response_dict['id'] == int(film_id)
    assert response_dict['name'] == film_name



# Scenario 6

@scenario(
    scenario_name='Obter infos das séries do histórico',
    feature_name= '../features/history.feature'
)
def test_successful_get_series():
    pass

@given(
    parsers.cfparse(
        'um profile de id "{profile_id}" do usuário com id "{user_id}" e e-mail "{user_email}" e senha "{user_password}" está cadastrado no sistema',
    )
)
def mock_user_in_database(client, context, user_id: str, user_email: str, user_password: str, profile_id: str):
    # adiciona o usuário na base de dados (condição anterior ao teste)
    client,context['access_token'] =  pass_user_profile(client, user_id, user_email, user_password,)
    return context
@given(
    parsers.cfparse(
        'ele ja assistiu os videos de id "{video_id}" da série "{serie_name}"',
    )
)
def mock_videos_in_database(client, context, video_id: str, serie_name: str):
    response = client.post(
        '/history/register_access_video/', params={"n_video_id" :int(video_id)},
        headers={'Authorization' : f'Bearer {context["access_token"]}'})
    assert response.status_code == 201
    context['serie_name'] = serie_name
    return context

@when(
    parsers.cfparse(
    'o usuário envia uma requisição GET para "{get_url}"'
    ),target_fixture="context"
)
def send_get_history_movie(client, context, get_url: str):
    response = client.get(
        get_url, headers={'Authorization' : f'Bearer {context["access_token"]}'})
    context["response"] = response
    return context

@then(
    parsers.cfparse('recebo o status da resposta "{cod_resp}"'),
    target_fixture="context"
)
def check_code_movie_get(client, context, cod_resp :str):
    assert context["response"].status_code == int(cod_resp)
    return context
@then(
    parsers.cfparse(
    'o JSON da resposta deve conter uma lista com as séries assistidas'),
    target_fixture="context"
)
def check_type_return(client, context):
    assert type(context['response'].json()) == type([])
    context['serie_list'] = context['response'].json()
    return context
@then(
    parsers.cfparse(
    'na série "{serie_name}" o episódio atual é o "{ep_atual}" e o próximo "{next_ep}"'),
    target_fixture="context"
)
def check_serie(client, context, serie_name:str, ep_atual:str, next_ep:str):
    for serie in context['response'].json():
        if serie['name'] == serie_name:
            assert serie['last_episode']['name'] == ep_atual
            assert serie['next_episode']['name'] == next_ep
    return context

