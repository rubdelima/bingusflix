Feature: My list
As a usuário
I want to adicionar filmes e series na minha lista
So that eu possa adicionar filmes e series que eu pretenda assitir numa lista de acesso rápido

Scenario: Adicionando itens na lista
Given eu estou logado como "usuário comum" com login "hfm@email.com" e senha "hfm123"
And eu estou na página "inicial"
And nao há o filme ou serie "Barbie" na lista
When eu seleciono "adicionar filme na lista" no filme "Barbie"
Then eu vejo o filme ou serie "Barbie" na minha lista
And eu continuo na página inicial

Scenario: Removendo itens da lista
Given eu estou logado como "usuário comum" com login "hfm@email.com" e senha "hfm123"
And eu estou na página "inicial"
And a lista tem o filme ou serie "Barbie"
When eu vejo a opção "remover intem da lista" no filme "Barbie" na minha lista
And eu seleciono "remover item da lista"
Then eu não vejo o filme "Barbie" na minha lista
And eu continuo na página "inicial"