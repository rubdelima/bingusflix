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
def mock_user_in_database(user_email: str, user_password: str):
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
        'um usuário envia uma requisição PUT para "{account_recovery_url}" com email "{user_email}" e nova senha "{new_password}" e confirmação de senha "{confirm_password}"'
    ),
    target_fixture="context"
)
def send_account_recovery_request(client, context, account_recovery_url: str, user_email: str, new_password: str, confirm_password: str):
    response = client.put(account_recovery_url, json={"email": user_email, "new_password": new_password, "confirm_password": confirm_password})
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_account_recovery_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)
    return context

@then(
    parsers.cfparse(
        'o JSON da resposta deve conter o usuário com email "{user_email}" e senha "{new_password}"'
    ),
    target_fixture="context"
)
def check_account_recovery_response_user(context, user_email: str, new_password: str):
    expected_response = {"email": user_email, "new_password": new_password, "confirm_password": new_password}
    assert context["response"].json() == expected_response
    return context
