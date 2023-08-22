Feature: Profiles

    Scenario: Criação bem sucedida de um profile
    Given um usuário com id "1" com e-mail "fal5@gmail.com" e senha "senha123" está logado no sistema
    And esse usuário possui "0" profiles
    When o usuário envia uma requisição POST para "/profiles" com nickname "fred", pg "16" e language "pt-br"
    Then o status da resposta deve ser "201"
    And o JSON da resposta deve conter o nickname "fred", pg "16", language "pt-br", id_user "1" e id_profile "1"

    Scenario: Criação má sucedida de um profile
    Given um usuário com id "2" com e-mail "fnls@gmail.com", senha "senha123" e plan "False" está logado no sistema
    And esse usuário possui "3" profiles
    When o usuário envia uma requisição POST para "/profiles" com nickname "neiva", pg "18" e language "en-us"
    Then o status da resposta deve ser "403"
    And o detail da resposta deve ser "Você atingiu o limite de perfis para seu plano (comum)"

    # Scenario: Remoção bem sucedida de um profile
    # Given um usuário com id "1" com e-mail "fal5@gmail.com" e senha "senha123" está logado no sistema
    # And esse usuário possui "2" profiles
    # When o usuário envia uma requisição DELETE para "/profiles/2"
    # Then o status da resposta deve ser "200"
    # And esse usuário possui "1" profiles

    # Scenario: Remoção má sucedida de um profile
    # Given um usuário com id "1" com e-mail "fal5@gmail.com" e senha "senha123" está logado no sistema
    # And esse usuário possui "1" profiles
    # When o usuário envia uma requisição DELETE para "/profiles/1"
    # Then o status da resposta deve ser "403"
    # And o detail da resposta deve ser "Você não pode deletar seu único profile"
    # And esse usuário possui "1" profiles

    # Scenario: Modificação bem sucedida de um profile
    # Given um usuário com id "1" com e-mail "fal5@gmail.com" e senha "senha123" está logado no sistema
    # And esse usuário possui "1" profiles
    # When o usuário envia uma requisição PUT para "/profiles/1" com nickname "felipe", pg "18" e language "pt-br"
    # Then o status da resposta deve ser "201"
    # And o JSON da resposta deve conter o nickname "felipe", pg "18", language "pt-br", id_user "1" e id_profile "1"

    # Scenario: Listagem bem sucedida dos profiles de um usuario
    # Given um usuário com id "2" com e-mail "fnls@gmail.com", senha "senha123" e plan "True" está logado no sistema
    # And esse usuário possui "3" profiles: nickname "felipe", pg "18", language "pt-br", nickname "neiva", pg "18", language "pt-br" e nickname "lima", pg "18", language "pt-br"
    # When o usuário envia uma requisição GET para "/profiles"
    # Then o status da resposta deve ser "200"
    # And o JSON da resposta deve conter: nickname "felipe", pg "18", language "pt-br", nickname "neiva", pg "18", language "pt-br" e nickname "lima", pg "18", language "pt-br"

    # Scenario: Listagem bem sucedida de um profile especifico do usuário
    # Given um usuário com id "2" com e-mail "fnls@gmail.com", senha "senha123" e plan "True" está logado no sistema
    # And esse usuário possui "3" profiles: nickname "felipe", pg "18", language "pt-br", nickname "neiva", pg "18", language "pt-br" e nickname "lima", pg "18", language "pt-br"
    # When o usuário envia uma requisição GET para "/profiles/1"
    # Then o status da resposta deve ser "200"
    # And o JSON da resposta deve conter nickname "felipe", pg "18" e language "pt-br"
