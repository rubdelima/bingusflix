from pytest_bdd import scenario, given, when, then, parsers
from src.schemas.user import UserDB
from src.api.my_list import my_list_db as db
from src.api.users import database as db1

def pass_user_profile(client, user_id, user_email, user_psw ):
    db1.clear()
    db1.append(UserDB(
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
    scenario_name='Add an item to my list',
    feature_name='../features/my_list.feature'
)
def test_add_item_to_my_list():
    """Tests the add item to my list route"""

@given(
    parsers.cfparse(
        'nao ha filme com titulo "{movie_title}" na minha lista'
    )
)
def remove_movie_from_my_list(client, context, movie_title: str):
    """Removes a movie from my list"""
    client, context['access_token'] =  pass_user_profile(client, 1, "hfm@email.com", "hfm123")
    db = {}

@when(
    parsers.cfparse(
        'o usuario envia uma requisicao POST para "{my_list_url}" com adult "{movie_adult}", backdrop_path "{movie_backdrop}", genre_ids "{movie_genre_ids}", id "{movie_id}", original_language "{movie_original_lang}", original_title "{movie_original_title}", overview "{movie_overview}", popularity "{movie_popularity}", poster_path "{movie_poster}", release_date "{movie_release}", title "{movie_title}", video "{movie_video}", vote_average "{movie_vote_avg}", vote_count "{movie_vote_count}"'
    )
)
def add_movie_to_my_list(client, context, my_list_url, movie_adult, movie_backdrop, movie_genre_ids, movie_id, movie_original_lang, movie_original_title, movie_overview, movie_popularity, movie_poster, movie_release, movie_title, movie_video, movie_vote_avg, movie_vote_count):
    """Adds a movie to my list"""
    movie_adult = True if movie_adult.lower() == 'true' else False
    movie_video = True if movie_video.lower() == 'true' else False
    movie_genre_ids = movie_genre_ids.strip('][').split(', ')
    for idx, id in enumerate(movie_genre_ids):
        movie_genre_ids[idx] = int(id)
        
    response = client.post(
        my_list_url,
        headers={'Authorization' : f'Bearer {context["access_token"]}'},
        json={
            'adult': movie_adult,
            'backdrop_path': movie_backdrop,
            'genre_ids': movie_genre_ids,
            'id': int(movie_id),
            'original_language': movie_original_lang,
            'original_title': movie_original_title,
            'overview': movie_overview,
            'popularity': float(movie_popularity),
            'poster_path': movie_poster,
            'release_date': movie_release,
            'title': movie_title,
            'video': movie_video,
            'vote_average': float(movie_vote_avg),
            'vote_count': int(movie_vote_count)
        }
    )
    context["response"] = response
    return context

@then(
    parsers.cfparse(
        'o status da reposta deve ser "{status_code}"'
    ), target_fixture='context'
)
def check_status_code(context, status_code: int):
    """Checks the response status code"""
    assert context["response"].status_code == int(status_code)
    return context

@then(
    parsers.cfparse(
        'a reposta deve conter o titulo "{movie_title}"'
    ), target_fixture='context'
)
def check_movie_title(context, movie_title: str):
    """Checks if the response contains the movie title"""
    assert context["response"].json()["title"] == movie_title
    return context