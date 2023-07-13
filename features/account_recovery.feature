Feature: Account Recovery
As a usuário
I want to solicitar recuperação da minha conta
So that eu posso alterar a senha e voltar a acessar o sistema

Scenario: usuário solicita recuperação de conta
	
Given eu não estou logado com nenhum usuário do sistema
And eu estou na página de “Login”
When eu clico no botão “Esqueci minha senha”
Then eu sou encaminhado para a página “Recuperação de conta”

Scenario: usuário altera sua senha por meio da recuperação de conta
	
Given eu não estou logado com nenhum usuário do sistema
And eu estou na página de “Recuperação de conta”
And existe um usuário cadastrado no sistema com o e-mail “felipe@gmail.com” e senha “netflix123”
When eu preencho o campo “Email” com “felipe@gmail.com” 
And eu preencho o campo “Nova senha” com “hbo123”
And eu preencho o campo “Confirmar senha” com “hbo123”
And eu clico no botão “Confirmar”
Then eu recebo uma mensagem de confirmação informando que a senha foi alterada
And existe um usuário cadastrado no sistema com o e-mail “felipe@gmail.com” e senha “hbo123”

Scenario: e-mail inválido na recuperação de conta
	
Given eu não estou logado com nenhum usuário do sistema
And eu estou na página de “Recuperação de conta”
And não existe um usuário cadastrado no sistema com o e-mail “felipe@gmail.com”
When eu preencho o campo “Email” com “felipe@gmail.com” 
And eu preencho o campo “Nova senha” com “hbo123”
And eu preencho o campo “Confirmar senha” com “hbo123”
And eu clico no botão “Confirmar”
Then eu recebo uma mensagem de erro informando que o e-mail não está cadastrado na plataforma
And não existe um usuário cadastrado no sistema com o e-mail “felipe@gmail.com”
