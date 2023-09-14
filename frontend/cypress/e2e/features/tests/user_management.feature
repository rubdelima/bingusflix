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

Scenario: Exclusão de conta
  Given o usuário de id "1" está logado
  And o usuário está na página "account-management"
  When clica na opção "deletar conta"
  Then o usuário é direcionado para a pagina "home"

Scenario: Atualizacão de senha da conta
  Given eu estou logado como "usuário comum" com login "hfm@email.com" e senha "hfm321"
  And eu estou na página "configuracões da conta"
  When eu seleciono "Alterar senha da conta"
  And eu preencho a senha com "hfm321"
  And eu preencho o "nova senha" com "321hfm" e "confirmação de senha" com "321hfm"
  Then eu recebo a mensagem de "Senha alterada com sucesso"
