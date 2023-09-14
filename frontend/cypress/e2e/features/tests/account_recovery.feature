Feature: Account Recovery
  As a usuário
  I want to solicitar recuperação da minha conta
  So that eu posso alterar a senha e voltar a acessar o sistema

Scenario: usuário solicita recuperação de conta
	
  Given o usuário está na página "login"
  When o usuário clica no botão "Esqueceu sua senha?"
  Then o usuário é direcionado para a página "account_recovery"

Scenario: usuário altera sua senha por meio da recuperação de conta
	
  Given o usuário está na página "account_recovery"
  When o usuário preenche o campo de "email" com "felipe@gmail.com"
  And preenche o campo de "nova-senha" com "hbo123"
  And preenche o campo de "confirmar-senha" com "hbo123"
  And clica na opção "Confirmar"
  Then o usuário recebe a mensagem de confirmação "Sua senha foi alterada com sucesso!"


Scenario: e-mail inválido na recuperação de conta
	
  Given o usuário está na página "account_recovery"
  When o usuário preenche o campo de "email" com "frederick@gmail.com"
  And preenche o campo de "nova-senha" com "hbo123"
  And preenche o campo de "confirmar-senha" com "hbo123"
  And clica na opção "Confirmar"
  Then o usuário recebe a mensagem de erro "Não foi possível alterar sua senha"

Scenario: confirmação senha diferente da nova senha
	
  Given o usuário está na página "account_recovery"
  When o usuário preenche o campo de "email" com "felipe@gmail.com"
  And preenche o campo de "nova-senha" com "hbo123"
  And preenche o campo de "confirmar-senha" com "amazon123"
  And clica na opção "Confirmar"
  Then o usuário recebe a mensagem de erro "As senha não coincidem"