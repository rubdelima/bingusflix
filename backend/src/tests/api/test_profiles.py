from src.conftest import unit_test_client


def test_create_profile(client: unit_test_client):
    login_response = client.post(
        '/login/',
        data={
            'username': 'fal5@examle.com',
            'password': 'string',
        }
    )

    print(login_response.json())

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