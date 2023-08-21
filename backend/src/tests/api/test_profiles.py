from src.conftest import unit_test_client

from src.api.users import database as db
from src.schemas.user import UserDB

db.append(UserDB(
        id=int(1),
        name="fred",
        surname="lopes",
        email="fal5@examle.com",
        birthdate="2000-01-01",
        plan=True,
        passwd="string"
    ))


def test_create_profile(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    access_token = login_response.json()['access_token']
    
    response = client.post(
        '/profiles/',
        json={
            'nickname': 'fred',
            'pg': 16,
            'language': 'pt-br',
        },
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == 201
    assert response.json() == {
        'nickname': 'fred',
        'pg': 16,
        'language': 'pt-br',
        'id_profile': 1,
        'id_user': 1,
    }


def test_create_profile2(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    access_token = login_response.json()['access_token']
    
    response = client.post(
        '/profiles/',
        json={
            'nickname': 'fred',
            'pg': 16,
            'language': 'pt-br',
        },
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == 201
    assert response.json() == {
        'nickname': 'fred',
        'pg': 16,
        'language': 'pt-br',
        'id_profile': 2,
        'id_user': 1,
    }


def test_get_profiles(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    access_token = login_response.json()['access_token']

    response = client.get(
        '/profiles/',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == 200
    assert response.json() == {
        'profiles': [
            {
                'nickname': 'fred',
                'pg': 16,
                'language': 'pt-br',
                'id_profile': 1,
                'id_user': 1,
            },
            {
                'nickname': 'fred',
                'pg': 16,
                'language': 'pt-br',
                'id_profile': 2,
                'id_user': 1,
            }
        ]
    }


def test_get_profile(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    access_token = login_response.json()['access_token']

    response = client.get(
        '/profiles/1',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == 200
    assert response.json() == {
        'nickname': 'fred',
        'pg': 16,
        'language': 'pt-br',
        'id_profile': 1,
        'id_user': 1,
    }


def test_delete_profile(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    access_token = login_response.json()['access_token']

    response = client.delete(
        '/profiles/1',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == 200
    assert response.json() == {
        'nickname': 'fred',
        'pg': 16,
        'language': 'pt-br',
        'id_profile': 1,
        'id_user': 1,
    }


def test_put_profile(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    access_token = login_response.json()['access_token']

    response = client.put(
        '/profiles/1',
        json={
            'nickname': 'neiva',
            'pg': 18,
            'language': 'en',
        },
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == 200
    assert response.json() == {
        'nickname': 'neiva',
        'pg': 18,
        'language': 'en',
        'id_profile': 1,
        'id_user': 1,
    }
