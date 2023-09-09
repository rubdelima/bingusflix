from src.conftest import unit_test_client

def test_login(client: unit_test_client):
    client.post(
        '/users/',
        json={
            'name': 'Caio',
            'surname': 'Possidio',
            'email': 'cpv@gmail.com',
            'passwd': 'cpv123',
            'birthdate': '2001-01-01',
            'plan': False,
        },
    )
    response = client.post(
        '/login/',
        data={
            'username': 'cpv@gmail.com',
            'password': 'cpv123'
        },
    )

    assert response.status_code == 200
    assert response.json()["access_token"] == '1'