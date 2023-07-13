In this feature you can create profiles to your account, so each profile will have its own preferences, like age rating,
language, favorite movies, among others.

Cenário: criação bem sucedida de um perfil
Dado que eu estou na página “criação e manuntenção de perfis” logado como “usuário comum” com login “rnl2” e senha “rubinho123”
E eu vejo “2” perfis criados: usuário “rnl2” com nome “Amanda”, usuário “rnl2” com nome “Rubens” e usuário “rnl2” com nome “adicionar perfil”
E eu vejo a opção “gerenciar perfis”
Quando eu seleciono “adicionar perfil”
E eu preencho “nome” com “Neiva”
E eu preencho “classificação etária” com “18”
E eu preencho “lingua” com “português”
E eu seleciono “salvar”
Então eu vejo uma mensagem de “sucesso”
E vejo “3” perfis criados: usuário “rnl2” com nome “Amanda”, usuário “rnl2” com nome “Rubens” e usuário “rnl2” com nome “Neiva”

Cenário: edição de um perfil
Dado que eu estou na página “criação e manuntenção de perfis” logado como “usuario comum” com login “rnl2” e senha “rubinho123”
E eu vejo “3” perfis criados: usuário “rnl2” com nome “Amanda”, usuário “rnl2” com nome “Rubens” e usuário “rnl2” com nome “Neiva”
E eu vejo a opção “gerenciar perfis”
Quando eu seleciono “gerenciar perfis”
E eu seleciono “Neiva”
E eu preencho “nome” com “Fred”
E eu preencho “classificação etária” com “14”
E eu preencho “lingua” com “português”
E eu seleciono “salvar”
Então eu vejo uma mensagem de “sucesso”
E vejo “3” perfis criados: usuário “rnl2” com nome “Amanda”, usuário “rnl2” com nome “Rubens” e usuário “rnl2” com nome “Fred”