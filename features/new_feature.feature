	Scenario: Cennário so para a questão
		Given Eu tenho que implementar uma nova feature
		When eu crio a nova feature
		Then eu realizo um commit na branch dev
	Scenario: Agora mais outra questão
		Given Eu tenho que fazer a questão 14
		When eu crio a nova feature
		Then eu faço um commit dela
		When eu tenho que editar novamente
		Then eu realizo um novo commit
