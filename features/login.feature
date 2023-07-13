Feature: Login
As a usuário
I want to logar na minha conta
So that eu posso acessar o sistema

Scenario: login bem sucedido de um usuário
	
Given eu estou na página de "Login"
And existe um usuário cadastrado no sistema com o e-mail "felipe@gmail.com" e a senha "netflix123"
When eu preencho o campo de "Email" com "felipe@gmail.com"
And eu preencho o campo "senha" com "netflix123"
Then eu sou encaminhado para a página "Inicial" do sistema
And eu estou logado com email "felipe@gmail.com"  e senha "netflix123"

Scenario: e-mail não cadastrado no sistema
	
Given eu estou na página de "Login"
And o sistema não tem um usuário cadastrado com o e-mail "frederick@gmail.com"
When eu preencho o campo de "Email" com "frederick@gmail.com"
And eu preencho o campo "senha" com "netflix123"
Then eu recebo a mensagem de erro "Credenciais inválidas"
And eu estou na página de "Login"

Scenario: senha incorreta
	
Given eu estou na página de "Login"
And existe um usuário cadastrado no sistema com o e-mail "felipe@gmail.com" e a senha "netflix123"
When eu preencho o campo de "Email" com "felipe@gmail.com"
And eu preencho o campo "senha" com "hbo123"
Then eu recebo a mensagem de erro "Credenciais inválidas"
And eu estou na página de "Login"