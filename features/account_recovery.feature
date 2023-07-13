Feature: Account Recovery
As a usuário
I want to solicitar recuperação da minha conta
So that eu posso alterar a senha e voltar a acessar o sistema

Scenario: usuário solicita recuperação de conta
	
Given eu estou na página de "Login"
When eu seleciono a opção "Esqueci minha senha"
Then eu sou encaminhado para a página "Recuperação de conta"

Scenario: usuário altera sua senha por meio da recuperação de conta
	
Given eu estou na página "Recuperação de conta"
And existe um usuário cadastrado no sistema com o e-mail "felipe@gmail.com" e a senha "netflix123"
When eu preencho o campo de "Email" com "felipe@gmail.com"
And eu preencho o campo "Nova senha" com "hbo123"
And eu preencho o campo "Confirmar senha" com "hbo123"
Then eu recebo a mensagem de confirmação "Sua senha foi alterada"
And eu estou na página de "Login"
And existe um usuário cadastrado no sistema com o e-mail "felipe@gmail.com" e a senha "hbo123"


Scenario: e-mail inválido na recuperação de conta
	
Given eu estou na página "Recuperação de conta"
And o sistema não tem um usuário cadastrado com o e-mail "frederick@gmail.com"
When eu preencho o campo de "Email" com "felipe@gmail.com"
And eu preencho o campo "Nova senha" com "hbo123"
And eu preencho o campo "Confirmar senha" com "hbo123"
Then eu recebo a mensagem de erro "Usuário não encontrado"
And eu estou na página de "Recuperação de conta"