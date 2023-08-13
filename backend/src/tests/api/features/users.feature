Feature: Users api

Scenario: Create a user
	Given o banco nao possui conta cadastrada com email "hfm@email.com"
	When uma requisição POST for enviada para "/api/tests" com o corpo da requisição sendo um JSON com o nome "Hugo"
	And sobrenome "Felix"
	And email "hfm@email.com"
	And senha "hfm321"
	And data de nascimento "01/02/2003"
	And plano "comum"
	Then o status da resposta deve ser "200"
    And o JSON da resposta deve conter o email "hfm@email.com" 

  Scenario: Obter user por ID
    Given ha um usuario com id "1" e nome "Hugo" cadastrado no banco de dados
	When uma requisição "GET" for enviada para "/users/1"
	Then o status da resposta deve ser "200"
    And o JSON da resposta deve conter id "123" e nome "Hugo"

  Scenario: Obter todos os usuarios
    Given o UserService retorna uma lista de usuarios
    When uma requisição "GET" for enviada para "/users"
    Then o status da resposta deve ser "200"
    And o JSON da resposta deve ser uma lista de usuarios 
    And o usuario com id "1" e nome "Hugo" está na lista
    And o usuario com id "2" e nome "Frederick" está na lista

  Scenario: Atualizar um usuario
    Given ha um usuario com id "1" e nome "Hugo" cadastrado no banco de dados
	When uma requisição "PUT" for enviada para "/users/1" com o corpo da requisição sendo um JSON com o nome "Rubens"
	And sobrenome "Nascimento"
	And email "hfm@email.com"
	And senha "hfm321"
	And data de nascimento "01/02/2003"
	And plano "comum"
	Then o status da resposta deve ser "200"
	And o JSON da resposta deve conter id "1" e nome "Rubens"
