from src.conftest import unit_test_client

def test_account_recovery(client: unit_test_client):
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
    response = client.put(
        '/account_recovery/',
        json={
            'email': 'cpv@gmail.com',
            'new_password': 'cpv345',
            'confirm_password': 'cpv345'
        },
    )

    assert response.status_code == 200
    assert response.json()["email"] == 'cpv@gmail.com'
    assert response.json()["new_password"] == 'cpv345'

    # remover o usuário adicionado no teste

    client.delete(
        '/users/1'
    )