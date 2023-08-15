from src.conftest import unit_test_client


def test_create_user(client: unit_test_client):
    response = client.post(
        '/users/',
        json={
            'name': 'alice',
            'surname': 'barbosa',
            'email': 'abm@cin.ufpe.br',
            'passwd': 'amb123',
            'birthdate': '2000-04-03',
            'plan': False,
        },
    )

    assert response.status_code == 201


def test_read_users(client: unit_test_client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'name': 'alice',
                'surname': 'barbosa',
                'email': 'abm@cin.ufpe.br',
                'birthdate': '2000-04-03',
                'plan': False,
                'id': 1,
            }
        ]
    }


def test_update_user(client: unit_test_client):
    response = client.put(
        '/users/1',
        json={
            'name': 'hugo',
            'surname': 'felix',
            'email': 'hfm@email.com',
            'passwd': 'speedwagon',
            'birthdate': '2000-04-03',
            'plan': False,
        },
    )
    
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'hugo',
        'surname': 'felix',
        'email': 'hfm@email.com',
        'birthdate': '2000-04-03',
        'plan': False,
    }


def test_delete_user(client: unit_test_client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {
        'status_code': 200,
        'message': 'User deleted',
        'data': None,
    }
