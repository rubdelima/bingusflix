Scenario: Procura de um filme no histórico com falha
Given eu estou logado como "usuario comum" com e-mail "rnl2@cin.ufpe.br" e senha "rubinho123"
And eu estou na página "Histórico"
And eu estou na seção "Filmes"
When eu pesquiso "Vingadores: Guerra Infinita", na barra de busca do histórico
Then nenhum filme correspondente é exibido nos resultados da pesquisa
E eu recebo a mensagem "o filme não foi encontrado no histórico".
