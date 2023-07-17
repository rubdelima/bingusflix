Cenário: Escolher o gênero ação
Dado que eu estou logado na como um “usuário comum” com login “cpv@email.com” senha “cainho123” e com o perfil “Caio” 
E eu estou na seção “gêneros”
E eu vejo os “genêros”: “ação”, “ficção científica”, “comédia”, “romance” e “suspense”
Quando eu escolho “gênero” “ação”
Então eu estou na página do gênero “ação”

Cenário: Assistir um filme/série do gênero ação
Dado que eu estou logado na como um “usuário comum” com login “cpv@email.com” senha “cainho123” e com o perfil “Caio” 
E existe um “filme” cadastrado com o nome “O resgate” e do gênero “ação”
E existe um “série” cadastrado com o nome “Narcos” e do gênero “ação” 
E eu estou na seção “gêneros”
Quando eu escolho a opção “ação” 
Então eu entro numa página que contém o filme “O resgate” e a série “Narcos” do gênero “ação”
