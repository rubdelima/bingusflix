Feature: Login
As a usuário
I want to logar na minha conta
So that eu posso acessar o sistema

Scenario: login bem sucedido de um usuário
	
Given eu não estou logado com nenhum usuário do sistema
And eu estou na página de “Login”
And existe um usuário cadastrado no sistema com o e-mail “felipe@gmail.com” e a senha “netflix123”
When eu preencho o campo de “Email” com “felipe@gmail.com”
And eu preencho o campo “Senha” com “netflix123”
And eu clico no botão “Entrar”
Then eu sou encaminhado para a página "Inicial" do sistema
And eu estou logado com email “felipe@gmail.com”  e senha “netflix123”

Scenario: e-mail não cadastrado no sistema
	
Given eu não estou logado com nenhum usuário do sistema
And eu estou na página de “Login”
And não existe um usuário cadastrado no sistema com o e-mail “felipe@gmail.com”
When eu preencho o campo de “Email” com “felipe@gmail.com”
And eu preencho o campo “Senha” com “netflix123”
And eu clico no botão “Entrar”
Then eu recebo uma mensagem de erro informando que o e-mail não está cadastrado na plataforma
And eu não estou logado com nenhum usuário do sistema
And eu estou na página de “Login”

Scenario: senha incorreta
	
Given eu não estou logado com nenhum usuário do sistema
And eu estou na página de “Login”
And existe um usuário cadastrado no sistema com o e-mail “felipe@gmail.com” e senha “netflix123”
When eu preencho o campo de “Email” com “felipe@gmail.com”
And eu preencho o campo “Senha” com “hbo123”
And eu clico no botão “Entrar”
Then eu recebo uma mensagem de erro informando que a senha digitada está incorreta
And eu não estou logado com nenhum usuário do sistema
And eu estou na página de “Login”