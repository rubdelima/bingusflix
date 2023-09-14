Feature: User Management
As um usuário
I want to ser capaz de me cadastrar no sistema
So that eu possa ser capaz de atualizar e deletar minhas informações

Scenario: Cadastro bem sucedido de um usuário
  Given o usuário está na página "home"
  When clica na opção "criar conta"
  And o usuário preenche o campo de "nome" com "Hugo"
  And preenche o campo de "sobrenome" com "felix"
  And preenche o campo de "email" com "hfm@email.com"
  And preenche o campo de "senha" com "hfm123"
  And preenche o campo de "data de nascimento" com "2003-02-01"
  And clica na opção "criar conta"
  Then o usuário é direcionado para a "login"

Scenario: Atualizacão de senha da conta
  Given o usuário de id "2" está logado
  And o usuário está na página "account-management"
  When o usuário preenche o campo de "senha-atual" com "brenosabemto"
  And preenche o campo de "nova-senha" com "cpvsabemais"
  And preenche o campo de "conf-senha" com "cpvsabemais"
  And clica na opção "criar conta"
  Then o usuário recebe a mensagem de confirmação "Sua senha foi alterada com sucesso!"

Scenario: Exclusão de conta
  Given o usuário de id "3" está logado
  And o usuário está na página "account-management"
  When clica na opção "deletar conta"
  Then o usuário é direcionado para a pagina "home"


