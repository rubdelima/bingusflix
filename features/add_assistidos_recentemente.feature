Scenario: Adicionar um filme à categoria Assistidos Recentemente
	Given eu estou logado como "usuario comum" com e-mail "rnl2@cin.ufpe.br" e senha "rubinho123"
	And eu estou na página "inicial"
	And eu seleciono o filme "Toy Story 3"
	When eu saio da pagina do filme
	And eu seleciono a seção "Assistidos Recentemente"
	Then eu sou direcionado para a página de "assistidos recentemente"
	And eu vejo o filme "Toy Story 3" como o primeiro da lista.
