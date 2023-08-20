Scenario: Encontrar uma série fora dos 10 primeiros itens
	Given eu estou logado como "usuario comum" com e-mail "rnl2@cin.ufpe.br" e senha "rubinho123"
	And eu estou na página "Visto Recentemente"
	And eu vejo os 10 primeiros itens
	And eu não encontro a série "The Mandalorian"
	When eu seleciono a opção "Avançar Página"
	Then 10 novos itens são exibidos
	And eu vejo a série "The Mandalorian".
