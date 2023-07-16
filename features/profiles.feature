Feature: Profiles
As a usuário
I want to criar vários perfis
So that eu possa dividir minha conta com amigos


Scenario: criação bem sucedida de um perfil

Given eu estou logado como “usuário comum” com login “rnl2@gmail.com” e senha “rubinho123”
And eu estou na página “criação e manuntenção de perfis”
And eu vejo “2” perfis criados: usuário “rnl2@gmail.com” com nome “Amanda”, usuário “rnl2@gmail.com” com nome “Rubens” e usuário “rnl2@gmail.com” com nome “adicionar perfil”
And eu vejo a opção “gerenciar perfis”
When eu seleciono “adicionar perfil”
And eu preencho “nome” com “Neiva”
And eu preencho “classificação etária” com “18”
And eu preencho “lingua” com “português”
And eu seleciono “salvar”
Then eu vejo uma mensagem de “sucesso”
And vejo “3” perfis criados: usuário “rnl2@gmail.com” com nome “Amanda”, usuário “rnl2@gmail.com” com nome “Rubens” e usuário “rnl2@gmail.com” com nome “Neiva”


Scenario: edição de um perfil:

Given eu estou logado como “usuario comum” com login “rnl2@gmail.com” e senha “rubinho123”
And eu estou na página “criação e manuntenção de perfis”
And eu vejo “3” perfis criados: usuário “rnl2@gmail.com” com nome “Amanda”, usuário “rnl2@gmail.com” com nome “Rubens” e usuário “rnl2@gmail.com” com nome “Neiva”
And eu vejo a opção “gerenciar perfis”
When eu seleciono “gerenciar perfis”
And eu seleciono “Neiva”
And eu preencho “nome” com “Fred”
And eu preencho “classificação etária” com “14”
And eu preencho “lingua” com “português”
And eu seleciono “salvar”
Then eu vejo uma mensagem de “sucesso”
And vejo “3” perfis criados: usuário “rnl2@gmail.com” com nome “Amanda”, usuário “rnl2@gmail.com” com nome “Rubens” e usuário “rnl2@gmail.com” com nome “Fred”


Scenario: remoção de um perfil bem sucedida

Given eu estou logado como “usuario comum” com login “rnl2@gmail.com” e senha “rubinho123”
And eu estou na página “criação e manuntenção de perfis”
And eu vejo “3” perfis criados: usuário “rnl2@gmail.com” com nome “Amanda”, usuário “rnl2@gmail.com” com nome “Rubens” e usuário “rnl2@gmail.com” com nome “Fred”
And eu vejo a opção “gerenciar perfis”
When eu seleciono “gerenciar perfis”
And eu seleciono “Amanda”
And eu seleciono “remover” e “confirmar”
Then eu vejo uma mensagem de “sucesso”
And vejo “3” perfis criados: usuário “rnl2@gmail.com” com nome “Rubens”, usuário “rnl2@gmail.com” com nome “Fred” e usuário “rnl2@gmail.com” com nome “adicionar perfil”


Scenario: criação má sucedida de um perfil

Given eu estou logado como “usuário comum” com login "rnl2@gmail.com" e senha “rubinho123”
And eu estou na página “criação e manuntenção de perfis”
And eu vejo “2” perfis criados: usuário "rnl2@gmail.com" com nome “Amanda”, usuário "rnl2@gmail.com" com nome “Rubens” e usuário "rnl2@gmail.com" com nome “adicionar perfil”
And eu vejo a opção “gerenciar perfis”
When eu seleciono “adicionar perfil”
And eu preencho “nome” com “”
And eu preencho “classificação etária” com “”
And eu preencho “lingua” com “português”
And eu seleciono “salvar”
Then eu vejo uma mensagem de “erro” 
And eu vejo “2” perfis criados: usuário "rnl2@gmail.com" com nome “Amanda”, usuário "rnl2@gmail.com" com nome “Rubens” e usuário "rnl2@gmail.com" com nome “adicionar perfil”


Scenario: remoção de um perfil má sucedida

Given eu estou logado como “usuario comum” com login "rnl2@gmail.com" e senha “rubinho123”
And eu estou na página “criação e manuntenção de perfis” 
And eu vejo “3” perfis criados: usuário "rnl2@gmail.com" com nome “Amanda”, usuário "rnl2@gmail.com" com nome “Rubens” e usuário "rnl2@gmail.com" com nome “Fred”
And eu vejo a opção “gerenciar perfis”
When eu seleciono “gerenciar perfis”
And eu seleciono “”
And eu seleciono “remover” e “confirmar”
Then eu vejo uma mensagem de “erro”
And eu vejo “3” perfis criados: usuário "rnl2@gmail.com" com nome “Amanda”, usuário "rnl2@gmail.com" com nome “Rubens” e usuário "rnl2@gmail.com" com nome “Fred”
And eu vejo a opção "gerenciar perfis"


Scenario: alteração da língua de um perfil bem sucedida

Given eu estou logado como “usuario comum” com login "rnl2@gmail.com" e senha “rubinho123”
And eu estou na página “criação e manuntenção de perfis” 
And eu vejo “3” perfis criados: usuário "rnl2@gmail.com" com nome “Amanda”, usuário "rnl2@gmail.com" com nome “Rubens” e usuário "rnl2@gmail.com" com nome “Neiva”
And eu vejo a opção “gerenciar perfis”
When eu seleciono “gerenciar perfis”
And eu seleciono “Neiva”
And eu preencho “lingua” com “inglês”
And eu seleciono “salvar”
Then eu vejo uma mensagem de “sucesso”
And vejo “3” perfis criados: usuário "rnl2@gmail.com" com nome “Amanda”, usuário "rnl2@gmail.com" com nome “Rubens” e usuário "rnl2@gmail.com" com nome “Neiva”
And eu vejo os textos em "inglês"
