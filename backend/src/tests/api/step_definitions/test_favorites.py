from pytest_bdd import scenario, given, when, then, parsers
from src.schemas.user import UserDB
from src.schemas.profile import ProfileDB
from src.schemas.favorite import FavoriteDB

from src.api.users import database as db
from src.api.profiles import database_profiles as db_p
from src.api.favorites import database_favorites as db_f

def login_user_profile(client, user_email: str, user_password: str, user_id: str, profile_id: str):
    db.clear()
    db_p.clear()

    db.append(UserDB(
        id=int(user_id),
        name="Nome",
        surname="Sobrenome",
        email=user_email,
        birthdate="2000-01-01",  
        plan=True,
        passwd=user_password
    ))

    db_p.append(ProfileDB(
        nickname= "Nickname",
        pg= 16,
        language= "pt-BR",
        id_user= int(user_id),
        id_profile= int(profile_id)
    ))
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
    scenario_name="Adição bem sucedida de um favorite",
    feature_name="../features/favorites.feature"
)
def test_successful_favorite_addition():
    """Test the successful addition of a favorite"""

@given(
    parsers.cfparse(
        'um usuário com id "{user_id}", e-mail "{user_email}", senha "{user_password}" está logado no sistema com o perfil com id "{profile_id}"')
)
def mock_user_in_database(client, context, user_id: str, user_email: str, user_password: str, profile_id: str):
    client, context["access_token"] = login_user_profile(client, user_email, user_password, user_id, profile_id)

    return context

@given(
    parsers.cfparse('esse usuário possui "{n_favorites}" favoritos')
)
def mock_favorites_in_database(context, n_favorites: str):
    db_f.clear()
    
    return context

@when(
    parsers.cfparse('o usuário envia uma requisição POST para "{favorites_url}" com id do vídeo "{video_id}"'), target_fixture="context"
)
def send_favorite_addition_request(client, context, favorites_url: str, video_id: str):
    response = client.post(
        favorites_url, 
        json={
            "id_video": int(video_id),
        },
        headers={'Authorization': f'Bearer {context["access_token"]}'}, 
    )
    context["response"] = response

    return context

@then(
    parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context"
)
def check_favorite_addition_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)

    return context

@then(
    parsers.cfparse('o JSON da resposta deve conter o id do vídeo "{video_id}", o id do usuário "{user_id}", o id do perfil "{profile_id}" e o id do favorito "{favorite_id}"'), target_fixture="context"
)
def check_favorite_addition_response_json(context, video_id: str, user_id: str, profile_id: str, favorite_id: str):
    expected_favorite_response = {
        "id_video": int(video_id),
        "id_user": int(user_id),
        "id_profile": int(profile_id),
        "id_favorite": int(favorite_id)
    }

    assert context["response"].json() == expected_favorite_response

    return context


@scenario(
    scenario_name="Remover um favorite",
    feature_name="../features/favorites.feature"
)
def test_favorite_removal():
    """Test the removal of a favorite"""

@given(
    parsers.cfparse(
        'um usuário com id "{user_id}", e-mail "{user_email}", senha "{user_password}" está logado no sistema com o perfil com id "{profile_id}"')
)
def mock_user_in_database(client, context, user_id: str, user_email: str, user_password: str, profile_id: str):
    client, context["access_token"] = login_user_profile(client, user_email, user_password, user_id, profile_id)

    context["user_id"] = user_id
    context["profile_id"] = profile_id

    return context

@given(
    parsers.cfparse('esse usuário possui "{n_favorites}" favoritos')
)
def mock_favorites_in_database(context, n_favorites: str):
    db_f.clear()
    for i in range(int(n_favorites)):
        db_f.append(FavoriteDB(
            id_video= i+1,
            id_user= int(context["user_id"]),
            id_profile= int(context["profile_id"]),
            id_favorite= i+1
        ))
    
    return context

@when(
    parsers.cfparse('o usuário envia uma requisição DELETE para "{favorites_url}"'), target_fixture="context"
)
def send_favorite_removal_request(client, context, favorites_url: str):
    response = client.delete(
        favorites_url, 
        headers={'Authorization': f'Bearer {context["access_token"]}'}, 
    )
    context["response"] = response

    return context

@then(
    parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context"
)
def check_favorite_removal_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)

    return context

@then(
    parsers.cfparse('esse usuário possui "{n_favorites}" favoritos'), target_fixture="context"
)
def check_favorite_removal_response_json(context, n_favorites: str):
    assert len(db_f) == int(n_favorites)

    return context


@scenario(
    scenario_name="Mostra todos os favorites de um usuário",
    feature_name="../features/favorites.feature"
)
def test_show_all_favorites():
    """Test the show all favorites"""

@given(
    parsers.cfparse(
        'um usuário com id "{user_id}", e-mail "{user_email}", senha "{user_password}" está logado no sistema com o perfil com id "{profile_id}"')
)
def mock_user_in_database(client, context, user_id: str, user_email: str, user_password: str, profile_id: str):
    client, context["access_token"] = login_user_profile(client, user_email, user_password, user_id, profile_id)

    context["user_id"] = user_id
    context["profile_id"] = profile_id

    return context

@given(
    parsers.cfparse('esse usuário possui "{n_favorites}" favoritos: favorito com id "{id_favorite1}" e vídeo "{id_video1}" e favorito com id "{id_favorite2}" e vídeo "{id_video2}"')
)
def mock_favorites_in_database(context, n_favorites: str, id_favorite1: str, id_video1: str, id_favorite2: str, id_video2: str):
    db_f.clear()
    db_f.append(FavoriteDB(
        id_video= int(id_video1),
        id_user= int(context["user_id"]),
        id_profile= int(context["profile_id"]),
        id_favorite= int(id_favorite1)
    ))
    db_f.append(FavoriteDB(
        id_video= int(id_video2),
        id_user= int(context["user_id"]),
        id_profile= int(context["profile_id"]),
        id_favorite= int(id_favorite2)
    ))

    return context

@when(
    parsers.cfparse('o usuário envia uma requisição GET para "{favorites_url}"'), target_fixture="context"
)
def send_favorite_show_all_request(client, context, favorites_url: str):
    response = client.get(
        favorites_url, 
        headers={'Authorization': f'Bearer {context["access_token"]}'}, 
    )
    context["response"] = response
    return context

@then(
    parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context"
)
def check_favorite_show_all_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)

    return context

@then(
    parsers.cfparse('o JSON da resposta deve conter: o id do vídeo "{video1_id}" e o id do favorito "{favorite1_id}", com id do usuário "{user1_id}" e o id do perfil "{profile1_id}", e o id do vídeo "{video2_id}" e id do favorito "{favorite2_id}", com id do usuário "{user2_id}" e o id do perfil "{profile2_id}"'), target_fixture="context"
)
def check_favorite_show_all_response_json(context, video1_id: str, favorite1_id: str, user1_id: str, profile1_id: str, video2_id: str, favorite2_id: str, user2_id: str, profile2_id: str):
    expected_response = {
        'favorites': [
            {
                'id_video': int(video1_id),
                'id_user': int(user1_id),
                'id_profile': int(profile1_id),
                'id_favorite': int(favorite1_id),
            },
            {
                'id_video': int(video2_id),
                'id_user': int(user2_id),
                'id_profile': int(profile2_id),
                'id_favorite': int(favorite2_id),
            },
        ]
    }

    assert context["response"].json() == expected_response

    return context