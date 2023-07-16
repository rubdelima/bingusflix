	Scenario: Encontar um filme no histórico com sucesso
		Given eu estou logado como "usuario comum" com e-mail "rnl2@cin.ufpe.br", senha "rubinho123" e nome "Fred"
		And eu estou na página "Histórico"
		And eu estou na seção "Filmes"
		When eu pesquiso "Toy Story 3" ma barra de busca do histórico
		Then o filme "Toy Story 3" é exibido.
