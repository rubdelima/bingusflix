Feature: Gender division 
As a usu rio 
I want to poder escolher um gˆnero de filme/s‚rie 
So that eu consigo escolher qual irei assistir entre os filmes/s‚ries desse gˆnero 
Scenario: 
Escolher o gˆnero a‡Æo  
Given eu estou logado na como um "usu rio comum" com login "cpv@email.com" senha "cainho123" e com o perfil "Caio" 
And eu estou na se‡Æo "gˆneros" 
And eu vejo os "gˆneros": "a‡Æo", "fic‡Æo cient¡fica", "com‚dia", "romance" e "suspense" 
When eu escolho "gˆnero" "a‡Æo" 
Then eu estou na p gina do gˆnero "a‡Æo" 
ECHO est  ativado.
Scenario: Assistir um filme/s‚rie do gˆnero a‡Æo 
Given eu estou logado na como um "usu rio comum" com login "cpv@email.com" senha "cainho123" e com o perfil "Caio" 
And existe um "filme" cadastrado com o nome "O resgate" e do gˆnero "a‡Æo" 
And existe um "s‚rie" cadastrado com o nome "Narcos" e do gˆnero "a‡Æo" 
And eu estou na se‡Æo "gˆneros" 
When eu escolho a op‡Æo "a‡Æo" 
Then eu entro numa p gina que cont‚m o filme "O resgate" e a s‚rie "Narcos" do gˆnero "a‡Æo" 
