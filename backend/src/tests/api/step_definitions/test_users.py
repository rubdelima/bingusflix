from pytest_bdd import scenario, given, when, then, parsers
from src.api.users import database as db
from src.schemas.user import UserDB

@scenario(
    scenario_name='Create a user',
    feature_name='../features/users.feature'
)
def test_create_user():
    """Tests the creation of a user"""

@given(
    parsers.cfparse(
        'o banco nao possui conta cadastrada com email "{user_email}"'
    )
)
def remove_user_from_database(user_email: str):
    """Removes the user from the database"""
    db.clear()

@when(
    parsers.cfparse(
        'uma requisição POST for enviada para "{login_url}" com o corpo da requisição sendo um JSON com o nome "{user_name}", sobrenome "{user_surname}", email "{user_email}", senha "{user_passwd}", data de nascimento "{user_birthdate}", plano "{user_plan}", perfil ativo "{user_active}"'
    ),
    target_fixture="context"
)
def send_user_post_request(client, context, login_url: str, user_name: str, user_surname: str, user_email: str, user_passwd: str, user_birthdate: str, user_plan: str, user_active: str):
    """Sends a POST request to the login_url with the user_email and user_passwd"""
    user_plan = True if user_plan.lower() == "true" else False
    response = client.post(
        login_url, 
        json={
            "name": user_name,
            "surname": user_surname,
            "email": user_email,
            "passwd": user_passwd,
            "birthdate": user_birthdate,
            "plan": user_plan,
            "active_profile": int(user_active)
        }
    )
    context["response"] = response
    return context

@then(
    parsers.cfparse(
        'o status da resposta deve ser "{status_code}"'
        ), target_fixture="context"
)
def check_user_post_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)
    return context

@then(
    parsers.cfparse(
        'o JSON da resposta deve conter o email "{user_email}"',
    ),
    target_fixture="context"
)
def check_user_post_response_email(context, user_email: str):
    expected_response = "hfm@email.com"
    assert context["response"].json()["email"] == expected_response
    return context


@scenario(
    scenario_name='Get all users',
    feature_name='../features/users.feature'
)
def test_get_user_by_id():
    """Tests the get user route"""

@given(
    parsers.cfparse(
        'ha dois usuario cadastrados no banco de dados, um com id "{user_id1}" e nome "{user_name1}" e outro com id "{user_id2}" e nome "{user_name2}"'
    )
)
def add_users_to_database(client, user_id1: str, user_name1: str, user_id2: str, user_name2: str):
    """Adds a user to the database"""
    db.clear()
    db.append(UserDB(
        id=int(user_id1),
        name=user_name1,
        surname="Felix",
        email="hfm@email.com",
        birthdate="2003-03-21",
        plan=True,
        passwd="hfm321"
    ))
    db.append(UserDB(
        id=int(user_id2),
        name=user_name2,
        surname="ALMEIDA",
        email="fal5@email.com",
        passwd="fal5321",
        birthdate="2003-05-01",
        plan=True,
    ))
    

@when(
    parsers.cfparse(
        'uma requisição GET for enviada para "{users_url}"'
    ),
    target_fixture="context"
)
def send_user_get_request(client, context, users_url: str):
    """Sends a GET request to the users_url"""
    response = client.get(users_url)
    context["response"] = response
    return context

@then(
    parsers.cfparse(
        'o status da resposta deve ser "{status_code}"'
    ),
    target_fixture="context"
)
def check_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)
    return context

@then(
    parsers.cfparse(
        'o JSON da resposta deve conter uma lista de usuarios'
    ),
    target_fixture="context"
)
def check_response_json(context):
    assert type(context["response"].json()["users"]) == list
    return context

@then(
    parsers.cfparse(
        'o usuario com id "{user_id1}" e nome "{user_name1}" está na lista'
    ),
    target_fixture="context"
)
def check_user1_in_json(context, user_id1: str, user_name1: str):
    
    assert context["response"].json()["users"][0].get("id") == int(user_id1)
    assert context["response"].json()["users"][0].get("name") == user_name1
    return context

@then(
    parsers.cfparse(
        'o usuario com id "{user_id2}" e nome "{user_name2}" tambem está na lista'
    ),
    target_fixture="context"
)
def check_user2_in_json(context, user_id2: str, user_name2: str):
    assert context["response"].json()["users"][1].get("id") == int(user_id2)
    assert context["response"].json()["users"][1].get("name") == user_name2
    return context


@scenario(
    scenario_name='Update a user',
    feature_name='../features/users.feature'
)
def test_update_user():
    """Tests the update user route"""

@given(
    parsers.cfparse(
        'ha um usuario com id "{user_id}" e nome "{user_name}" cadastrado no banco de dados'
    )
)
def add_user_to_database(client, user_id: str, user_name: str):
    """Adds a user to the database"""
    db.clear()
    db.append(UserDB(
        id=int(user_id),
        name=user_name,
        email="hfm@email.com",
        surname="Felix",
        birthdate="2003-03-21",
        plan=True,
        passwd="hfm321"
    ))

@when(
    parsers.cfparse(
        'uma requisição PUT for enviada para "{users_url}" com o corpo da requisição sendo um JSON com o nome "{user_name}", sobrenome "{user_surname}", email "{user_email}", senha "{user_passwd}", data de nascimento "{user_birthdate}", plano "{user_plan}", perfil ativo "{user_active}"'
    ),
    target_fixture="context"
)
def send_user_put_request(client, context, users_url: str, user_name: str, user_surname: str, user_email: str, user_passwd: str, user_birthdate: str, user_plan: str, user_active: str):
    """Sends a PUT request to the users_url with the user_email and user_passwd"""
    user_plan = True if user_plan.lower() == "true" else False
    response = client.put(
        users_url, 
        json={
            "name": user_name,
            "surname": user_surname,
            "email": user_email,
            "passwd": user_passwd,
            "birthdate": user_birthdate,
            "plan": user_plan,
            "active_profile": int(user_active)
        }
    )
    context["response"] = response
    return context

@then(
    parsers.cfparse(
        'o status da resposta deve ser "{status_code}"'
    ), target_fixture="context"
)
def check_user_put_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)
    return context

@then(
    parsers.cfparse(
        'o usuario cadastrado no banco deve ter a senha "{user_passwd}"'
    ), target_fixture="context"
)
def check_user_put_response_status_code(context, user_passwd: str):
    assert db[0].passwd == user_passwd
    return context


@scenario(
    scenario_name='Delete a user',
    feature_name='../features/users.feature'
)
def test_delete_user():
    """Tests the delete user route"""

@given(
    parsers.cfparse(
        'ha um usuario com id "1" e nome "Hugo" cadastrado no banco de dados'
    )
)
def add_user_to_database(client):
    """Adds a user to the database"""
    db.clear()
    db.append(UserDB(
        id=1,
        name="Hugo",
        email="hfm@email.com",
        surname="Felix",
        birthdate="2003-03-21",
        plan=True,
        passwd="hfm321"
    ))

@when(
    parsers.cfparse(
        'uma requisição DELETE for enviada para "{users_url}"'
    )
)
def send_user_delete_request(client, context, users_url: str):
    """Sends a DELETE request to the users_url"""
    response = client.delete(users_url)
    context["response"] = response
    return context

@then(
    parsers.cfparse(
        'o status da resposta deve ser "{status_code}"'
    ), target_fixture="context"
)
def check_delete_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)
    return context