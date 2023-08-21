from src.conftest import unit_test_client

from src.api.users import database as db
from src.api.profiles import database_profiles as db_p

from src.schemas.user import UserDB
from src.schemas.profile import ProfileDB

db.clear()
db_p.clear()

db.append(UserDB(
        id=int(1),
        name="fred",
        surname="lopes",
        email="fal5@examle.com",
        birthdate="2000-01-01",
        plan=True,
        passwd="string"
    ))

db_p.append(ProfileDB(
        nickname="fred",
        pg=16,
        language="pt-br",
        id_profile=1,
        id_user=1
))


def test_add_favorite(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    access_token = login_response.json()['access_token']
    
    response = client.post(
        '/favorites/',
        json={
            'id_video': 1,
        },
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == 201
    assert response.json() == {
        'id_video': 1,
        'id_user': 1,
        'id_profile': 1,
        'id_favorite': 1,
    }


def test_add_favorite2(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    access_token = login_response.json()['access_token']
    
    response = client.post(
        '/favorites/',
        json={
            'id_video': 2,
        },
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == 201
    assert response.json() == {
        'id_video': 2,
        'id_user': 1,
        'id_profile': 1,
        'id_favorite': 2,
    }


def test_get_favorites(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    access_token = login_response.json()['access_token']

    response = client.get(
        '/favorites/',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == 200
    assert response.json() == {
        'favorites': [
            {
                'id_video': 1,
                'id_user': 1,
                'id_profile': 1,
                'id_favorite': 1,
            },
            {
                'id_video': 2,
                'id_user': 1,
                'id_profile': 1,
                'id_favorite': 2,
            },
        ]
    }


def test_get_favorite(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    access_token = login_response.json()['access_token']

    response = client.get(
        '/favorites/1',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == 200
    assert response.json() == {
        'id_video': 1,
        'id_user': 1,
        'id_profile': 1,
        'id_favorite': 1,
    }