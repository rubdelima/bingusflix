Scenario: Favoritar um filme/série com sucesso
Given eu logado como “usuario comum” com login “rnl2”, senha “rubinho123” e nome “Fred”
And estou na página “inicial” 
And eu vejo a seção “assistidos recentemente”
And eu vejo “The witcher 3”
And eu vejo “Your lie in april”
And eu vejo “Breaking Bad”
And em cada “obra cinematográfica” eu vejo a opção “opções”
When eu seleciono ”opções” de “breaking bad”
And eu seleciono “Adicionar aos favoritos”
Then eu vejo uma mensagem de “sucesso”
And eu vejo a seção “Favoritos”
And eu vejo “Breaking Bad”