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
    print(f'Whencontext : {context}')
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