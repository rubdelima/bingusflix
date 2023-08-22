from pytest_bdd import scenario, given, when, then, parsers
from src.schemas.user import UserDB
from src.schemas.profile import ProfileDB
from src.api.users import database as db
from src.api.profiles import database_profiles as db_p


def login_user(client, user_email: str, user_password: str):
    login_response = client.post(
        '/login/',
        data={
            'username': user_email,
            'password': user_password,
        }
    )

    access_token = login_response.json()['access_token']

    return client, access_token


@scenario(
    scenario_name="Criação bem sucedida de um profile",
    feature_name="../features/profiles.feature"
)
def test_successful_profile_creation():
    """Test the successful creation of a profile"""

@given(
    parsers.cfparse(
        'um usuário com id "{user_id}" com e-mail "{user_email}" e senha "{user_password}" está logado no sistema'
    )
)
def mock_log_user_in(client, context, user_id: str, user_email: str, user_password: str):
    db.clear()
    db.append(UserDB(
        id=int(user_id),
        name="Nome",
        surname="Sobrenome",
        email=user_email,
        birthdate="2000-01-01",  
        plan=True,
        passwd=user_password
    ))
    
    client, context['access_token'] = login_user(client, user_email, user_password)

    return context

@given(
    parsers.cfparse(
        'esse usuário possui "{n_profiles}" profiles'
    )
)
def mock_user_profiles(context, n_profiles: str):
    db_p.clear()

    return context

@when(
    parsers.cfparse(
        'o usuário envia uma requisição POST para "{profiles_url}" com nickname "{profile_nick}", pg "{profile_pg}" e language "{profile_language}"'
    ), target_fixture="context"
)
def send_profile_creation_request(client, context, profiles_url: str, profile_nick: str, profile_pg: str, profile_language: str):
    response = client.post(
        profiles_url,
        json={
            'nickname': profile_nick,
            'pg': int(profile_pg),
            'language': profile_language,
        },
        headers={'Authorization': f'Bearer {context["access_token"]}'},
    )

    context["response"] = response
    return context

@then(
    parsers.cfparse(
        'o status da resposta deve ser "{status_code}"'
    ), target_fixture="context"
)
def check_profile_creation_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)

    return context

@then(
    parsers.cfparse(
        'o JSON da resposta deve conter o nickname "{profile_nick}", pg "{profile_pg}", language "{profile_language}", id_user "{profile_id_user}" e id_profile "{profile_id_profile}"'
    ), target_fixture="context"
)
def check_profile_creation_response_json(context, profile_nick: str, profile_pg: str, profile_language: str, profile_id_user: str, profile_id_profile: str):
    expected_response = {
        'nickname': profile_nick,
        'pg': int(profile_pg),
        'language': profile_language,
        'id_user': int(profile_id_user),
        'id_profile': int(profile_id_profile)
    }

    assert context["response"].json() == expected_response

    return context


@scenario(
    scenario_name="Criação má sucedida de um profile",
    feature_name="../features/profiles.feature"
)
def test_unsuccessful_profile_creation():
    """Test the unsuccessful creation of a profile"""

@given(
    parsers.cfparse(
        'um usuário com id "{user_id}" com e-mail "{user_email}", senha "{user_password}" e plan "{plan}" está logado no sistema'
    )
)
def mock_log_user_in(client, context, user_id: str, user_email: str, user_password: str, plan: str):
    if plan == 'True':
        plan = True
    else:
        plan = False

    db.clear()
    db.append(UserDB(
        id=int(user_id),
        name="Nome",
        surname="Sobrenome",
        email=user_email,
        birthdate="2000-01-01",  
        plan=bool(plan),
        passwd=user_password
    ))

    client, context['access_token'] = login_user(client, user_email, user_password)
    
    context['id_user'] = int(user_id)

    return context

@given(
    parsers.cfparse('esse usuário possui "{n_profiles}" profiles')
)
def mock_user_profiles(context, n_profiles: str):
    db_p.clear()

    for i in range(int(n_profiles)):
        db_p.append(ProfileDB(
            nickname= f'nickname{i}',
            pg= 16,
            language= 'pt-br',
            id_user= context['id_user'],
            id_profile= i+1
        ))

    return context

@when(
    parsers.cfparse('o usuário envia uma requisição POST para "{profiles_url}" com nickname "{profile_nick}", pg "{profile_pg}" e language "{profile_language}"'), target_fixture="context"
)
def send_profile_creation_request(client, context, profiles_url: str, profile_nick: str, profile_pg: str, profile_language: str):
    response = client.post(
        profiles_url,
        json={
            'nickname': profile_nick,
            'pg': int(profile_pg),
            'language': profile_language,
        },
        headers={'Authorization': f'Bearer {context["access_token"]}'},
    )

    context["response"] = response
    return context

@then(
    parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context"
)
def check_profile_creation_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)

    return context

@then(
    parsers.cfparse('o detail da resposta deve ser "{detail}"'), target_fixture="context"
)
def check_profile_creation_response_detail(context, detail: str):
    assert context["response"].json()['detail'] == detail

    return context