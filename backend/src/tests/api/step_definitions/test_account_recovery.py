from pytest_bdd import scenario, given, when, then, parsers
from src.schemas.user import UserDB
from src.api.users import database as db

@scenario(
    scenario_name="Usuário altera sua senha por meio da recuperação de conta",
    feature_name="../features/account_recovery.feature"
)
def test_successful_account_recovery():
    pass

@given(
    parsers.cfparse(
        'um usuário com email "{user_email}" e senha "{user_password}" está cadastrado no sistema'
    )
)
def mock_user_in_database(user_email: str, user_password: str): # adiciona o usuário na base de dados (condição anterior ao teste)
    db.clear()
    db.append(UserDB(
        id=1,
        name="Nome",
        surname="Sobrenome",
        email=user_email,
        birthdate="2000-01-01",  
        plan=True,
        passwd=user_password
    ))

@when(
    parsers.cfparse(
        'um usuário envia uma requisição PUT para "{account_recovery_url}" com email "{user_email}" e nova senha "{new_password}" e confirmação de senha "{confirm_password}"' # envia um put para a rota de recuperação de conta com o email, a nova senha e a confirmação da senha
    ),
    target_fixture="context"
)
def send_account_recovery_request(client, context, account_recovery_url: str, user_email: str, new_password: str, confirm_password: str):
    response = client.put(account_recovery_url, json={"email": user_email, "new_password": new_password, "confirm_password": confirm_password})
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context") 
def check_account_recovery_response_status_code(context, status_code: str): # verifica se o código de status da resposta é 200
    assert context["response"].status_code == int(status_code) 
    return context

@then(
    parsers.cfparse(
        'o JSON da resposta deve conter o usuário com email "{user_email}" e senha "{new_password}"'
    ),
    target_fixture="context"
)
def check_account_recovery_response_user(context, user_email: str, new_password: str):
    expected_response = {"email": user_email, "new_password": new_password} # verifica se o JSON da resposta contém o email do usuário, a nova senha e confirmação da senha
    print(expected_response)
    assert context["response"].json() == expected_response
    return context



@scenario(
    scenario_name="E-mail inválido na recuperação de conta",
    feature_name="../features/account_recovery.feature"
)
def test_invalid_email_account_recovery():
    pass

@given(parsers.cfparse('que nenhum usuário com email "{user_email}" está cadastrado no sistema')) 
def clear_database(user_email: str): # para garantir que não exista nenhum usuário cadastrado no sistema
    db.clear()

@when(
    parsers.cfparse(
        'um usuário envia uma requisição PUT para "{account_recovery_url}" com email "{user_email}" e nova senha "{new_password}" e confirmação de senha "{confirm_password}"' 
    ),
    target_fixture="context"
)
def send_account_recovery_request(client, context, account_recovery_url: str, user_email: str, new_password: str, confirm_password: str):
    response = client.put(account_recovery_url, json={"email": user_email, "new_password": new_password, "confirm_password": confirm_password}) # envia um put para a rota de recuperação de conta com o email, a nova senha e a confirmação da senha
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context") 
def check_account_recovery_response_status_code(context, status_code: str): # verifica se o código de status da resposta é 404
    assert context["response"].status_code == int(status_code)
    return context

@then(
    parsers.cfparse('a mensagem de erro deve ser "{error_message}"'), 
    target_fixture="context"
)
def check_account_recovery_response_error_message(context, error_message: str): # verifica se a mensagem de erro é "User not found"
    assert context["response"].json()["detail"] == error_message
    return context



@scenario(
    scenario_name="Confirmação de senha diferente da nova senha",
    feature_name="../features/account_recovery.feature"
)
def test_passwords_do_not_match_account_recovery():
    pass

@given(parsers.cfparse('que um usuário com email "{user_email}" e senha "{user_password}" está cadastrado no sistema'))
def mock_user_in_database(user_email: str, user_password: str): # adiciona o usuário na base de dados (condição anterior ao teste)
    db.clear()
    db.append(UserDB(
        id=1,
        name="Nome",
        surname="Sobrenome",
        email=user_email,
        birthdate="2000-01-01",  
        plan=True,
        passwd=user_password
    ))

@when(
    parsers.cfparse(
        'o usuário envia uma requisição PUT para "{account_recovery_url}" com email "{user_email}", nova senha "{new_password}" e confirmação de senha "{confirm_password}"'
    ),
    target_fixture="context"
)
def send_account_recovery_request(client, context, account_recovery_url: str, user_email: str, new_password: str, confirm_password: str): # envia um put para a rota de recuperação de conta com o email, a nova senha e a confirmação da senha
    response = client.put(account_recovery_url, json={"email": user_email, "new_password": new_password, "confirm_password": confirm_password})
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context") 
def check_account_recovery_response_status_code(context, status_code: str): # verifica se o código de status da resposta é 400
    assert context["response"].status_code == int(status_code)
    return context

@then(
    parsers.cfparse('a mensagem de erro deve ser "{error_message}"'),
    target_fixture="context"
)
def check_account_recovery_response_error_message(context, error_message: str): # verifica se a mensagem de erro é "Passwords do not match"
    assert context["response"].json()["detail"] == error_message
    return context