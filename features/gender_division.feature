Feature: Gender division 
As a usuário 
I want to poder escolher um gênero de filme/série 
So that eu consigo escolher qual irei assistir entre os filmes/séries desse gênero 
Scenario: Escolher o gênero ação  
Given eu estou logado na como um "usuário comum" com login "cpv@email.com" senha "cainho123" e com o perfil "Caio" 
And eu estou na seção "gêneros" 
And eu vejo os "gêneros": "ação", "ficção científica", "comédia", "romance" e "suspense" 
When eu escolho "gênero" "ação" 
Then eu estou na página do "gênero" "açãoo" 

Scenario: Assistir um filme/série do gênero ação 
Given eu estou logado na como um "usuário comum" com login "cpv@email.com" senha "cainho123" e com o perfil "Caio" 
And existe um "filme" cadastrado com o nome "O resgate" e do gênero "ação" 
And existe um "série" cadastrado com o nome "Narcos" e do gênero "ação" 
And eu estou na seção "gêneros" 
When eu escolho a opção "ação" 
Then eu entro numa página que contém o filme "O resgate" e a série "Narcos" do gênero "a‡Æo" 
