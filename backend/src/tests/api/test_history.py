from src.conftest import unit_test_client
from src.schemas.user import UserDB
from src.schemas.videos import get_video
from src.api.users import database as db
import json

def pass_user_profile(client, videos:dict={}):
    db.clear()
    db.append(UserDB(
        id=int(1),
        name="Nome",
        surname="Sobrenome",
        email="example@example.com",
        birthdate="2000-01-01",  
        plan=True,
        passwd="pass123"
    ))
    login_response = client.post(
        '/login/',
        data = {
            "username" : "example@example.com",
            "password" : "pass123"
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
    if 'videos' in videos:
        for video in videos['videos']:
            response = client.post(
                '/history/register_access_video/', params={"n_video_id" :video},
                headers={'Authorization' : f'Bearer {access_token}'})
    
    return client, access_token

# Teste para por algum fime no histórico
def test_put_on_history(client: unit_test_client):
    client, access_token = pass_user_profile(client)
    response = client.post(
        '/history/register_access_video/', params={"n_video_id" :8},
        headers={'Authorization' : f'Bearer {access_token}'})
    assert response.status_code == 201
    response_dict = response.json()
    expected_dict = json.loads(get_video(int(8))[0].model_dump_json())
    for key in response_dict.keys():
        assert response_dict[key] == expected_dict[key]



# Teste para checar o histórico
def test_get_history(client: unit_test_client):
    client, access_token = pass_user_profile(client, {'videos' : [8]})
    response = client.get('/history/', headers={'Authorization' : f'Bearer {access_token}'})
    assert response.status_code == 200
    j_response = response.json()
    try:
        del j_response['videos'][0]["watched_at"]
        assert j_response == {
              "videos": [
                    {
                      "id": 8,
                      "name": "Star Wars - O Império Contra-Ataca",
                      "duration": "02:00:00",
                      "gender": "Adventure",
                      "year": 1980,
                      "classification": 10,
                      "sinopse": "Após os Planos da Estrela da Morte serem pegos surge uma nova esperança",
                    }
                ]
            }
    except:
        assert 1 == 0

