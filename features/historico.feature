Scenario: Retomar série a partir do próximo episódio
Given eu estou logado como "usuario comum" com login "rnl2" e senha "rubinho123"
And eu estou na página "Histórico"
And eu estou na seção "Séries"
And a série "Stranger Things" não está listada como "finalizada"
And o episódio "8" da temporada “4” está como visto
When eu seleciono a série "Stranger Things"
And eu sigo em "Continuar"
Then a série "Stranger Things" é reproduzida a partir do e:pisódio "9" da 4ª temporada
