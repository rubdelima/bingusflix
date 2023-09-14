Feature: Login
  As a usuário
  I want to logar na minha conta
  So that eu posso acessar o sistema

Scenario: login bem sucedido de um usuário
  Given o usuário está na página "login"
  When o usuário preenche o campo de "email" com "felipe@gmail.com"
  And preenche o campo de "senha" com "netflix123"
  And clica na opção "Entrar"
  Then o usuário é direcionado para a "home-page"

Scenario: e-mail não cadastrado no sistema
  Given o usuário está na página "login"
  When o usuário preenche o campo de "email" com "frederick@gmail.com"
  And preenche o campo de "senha" com "netflix123"
  And clica na opção "Entrar"
  Then o usuário recebe a mensagem de erro "Usuário ou senha incorretos"
  And o usuário continua na página "login"

Scenario: senha incorreta
  Given o usuário está na página "login"
  When o usuário preenche o campo de "email" com "felipe@gmail.com"
  And preenche o campo de "senha" com "hbo123"
  And clica na opção "Entrar"
  Then o usuário recebe a mensagem de erro "Usuário ou senha incorretos"
  And o usuário continua na página "login"
