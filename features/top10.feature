Feature: Top 10 
As a usu rio 
I want to ver destacademente os filmes e as s‚ries mais assistidas do momento 
So that eu consigo assistir as melhores s‚ries e filmes do momento 
Scenario: Ver detalhes de um filme que est  no "Filmes Em alta" 
Given eu estou logado na como um "usu rio comum" com login "cpv@email.com" senha "cainho123" e com o perfil "Caio" 
And eu estou no topo da p gina "inicial" 
And eu vejo o t¢pico "Filmes Em alta" 
When clico em um dos "filmes" que faz parte desse t¢pico 
Then estarei vendo os detalhes deste "filme" 
ECHO est  ativado.
Scenario: Ver detalhes de uma s‚rie que est  no "S‚ries Em alta" 
Given eu estou logado na como um "usu rio comum" com login "cpv@email.com" senha "cainho123" e com o perfil "Caio" 
And eu estou no topo da p gina "inicial" 
And eu vejo o t¢pico "S‚ries Em alta" 
When clico em uma dessas "s‚ries" que faz parte desse t¢pico 
Then estarei vendo os detalhes desta "s‚rie" 
