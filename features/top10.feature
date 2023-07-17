Feature: Top 10 
As a usuário 
I want to ver destacademente os filmes e as séries mais assistidas do momento 
So that eu consigo assistir as melhores séries e filmes do momento 

Scenario: Ver detalhes de um filme que está no "Filmes Em alta" 
Given eu estou logado na como um "usuário comum" com login "cpv@email.com" senha "cainho123" e com o perfil "Caio" 
And eu estou no topo da página "inicial" 
And eu vejo o tópico "Filmes Em alta" 
When clico em um dos "filmes" que faz parte desse tópico 
Then estarei vendo os detalhes deste "filme" 

Scenario: Ver detalhes de uma série que está no "Séries Em alta" 
Given eu estou logado na como um "usuário comum" com login "cpv@email.com" senha "cainho123" e com o perfil "Caio" 
And eu estou no topo da página "inicial" 
And eu vejo o tópico "Séries Em alta" 
When clico em uma dessas "séries" que faz parte desse tópico 
Then estarei vendo os detalhes desta "série" 
