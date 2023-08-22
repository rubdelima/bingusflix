Feature: Users api

	Scenario: Create a user
		Given o banco nao possui conta cadastrada com email "hfm@email.com"
		When uma requisição POST for enviada para "/users/" com o corpo da requisição sendo um JSON com o nome "Hugo", sobrenome "Felix", email "hfm@email.com", senha "hfm321", data de nascimento "2003-02-01", plano "true", perfil ativo "1"
		Then o status da resposta deve ser "201"
		And o JSON da resposta deve conter o email "hfm@email.com"

	# Scenario: Get a user by id
	# 	Given ha um usuario com id "1" e nome "Hugo" cadastrado no banco de dados
	# 	When uma requisição "GET" for enviada para "/users/1"
	# 	Then o status da resposta deve ser "200"
	# 	And o JSON da resposta deve conter id "1" e nome "Hugo"

	Scenario: Get all users
		Given ha dois usuario cadastrados no banco de dados, um com id "1" e nome "Hugo" e outro com id "2" e nome "Frederick"
		When uma requisição GET for enviada para "/users"
		Then o status da resposta deve ser "200"
		And o JSON da resposta deve conter uma lista de usuarios
		And o usuario com id "1" e nome "Hugo" está na lista
		And o usuario com id "2" e nome "Frederick" tambem está na lista

	Scenario: Update a user
		Given ha um usuario com id "1" e nome "Hugo" cadastrado no banco de dados
		When uma requisição PUT for enviada para "/users/1" com o corpo da requisição sendo um JSON com o nome "Hugo", sobrenome "Felix", email "hfm@email.com", senha "speedwagon", data de nascimento "2003-02-01", plano "True", perfil ativo "1"
		Then o status da resposta deve ser "200"
		And o usuario cadastrado no banco deve ter a senha "speedwagon"
		
	Scenario: Delete a user
		Given ha um usuario com id "1" e nome "Hugo" cadastrado no banco de dados
		When uma requisição DELETE for enviada para "/users/1"
		Then o status da resposta deve ser "200"