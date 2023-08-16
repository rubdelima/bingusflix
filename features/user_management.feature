Feature: User Management
As um usuário
I want to ser capaz de me cadastrar no sistema
So that eu possa ser capaz de atualizar e deletar minhas informações

Scenario: Cadastro bem sucedido de um usuário
Given eu estou na página "criação de conta"
And não há contas criadas anteriormente com email "hfm@email.com"
When eu preencho nome com "Hugo"
And eu preencho sobrenome com "Felix"
And eu preencho email com "hfm@email.com"
And eu preencho senha com "hfm321"
And eu preencho data de nascimento com "01/02/2003"
And eu preencho plano com "comum"
And eu seleciono criar conta
Then eu vejo uma mensagem de "conta criada com sucesso"
And eu sou redirecionado para a página de "login"

Scenario: Exclusão de conta
Given eu estou logado como "usuário comum" com login "hfm@email.com" e senha "hfm321"
And estou na página "configurações da conta"
When eu seleciono "deletar conta"
And eu seleciono "confirmar"
Then na tela "login" eu recebo a mensagem "conta deletada"
And não existe mais no sistema nenhum usuário com login "hfm@email.com"

Scenario: Atualizacão de senha da conta
Given eu estou logado como "usuário comum" com login "hfm@email.com" e senha "hfm321"
And eu estou na página "configuracões da conta"
When eu seleciono "Alterar senha da conta"
And eu preencho a senha com "hfm321"
And eu preencho o "nova senha" com "321hfm" e "confirmação de senha" com "321hfm"
Then eu recebo a mensagem de "Senha alterada com sucesso"

Scenario: Falha na atualizacão de senha da conta
Given eu estou logado como "usuário comum" com login "hfm@email.com" e senha "hfm321"
And eu estou na página "configuracões da conta"
When eu seleciono "Alterar senha da conta"
And eu preencho a senha com "hfm321"
And eu preencho o "nova senha" com "321hfm" e "confirmação de senha" com "123hfm"
Then eu recebo a mensagem de "Senhas não coincidentes"

Scenario: Cadastro mal sucedido de usuário
Given eu estou na pagina "criacão de conta"
And não há contas criadas anteriormente com email "hfm@email.com"
When eu preencho nome com "Hugo"
And eu preencho sobrenome com "Felix"
And eu preencho senha com "hfm321"
And eu preencho data de nascimento com "01/02/2003"
And eu preencho plano com "comum"
And eu seleciono "criar conta"
Then eu vejo uma mensagem de "campo obrigatorio não preenchido"
And eu continuo na página de "criação de conta"
And o cadastro não foi realizado

Scenario: Alteração no nome do usuário
Given eu estou logado como "usuário comum" com login "hfm@email.com" e senha "hfm321"
And eu estou na página "configuracões da conta"
When eu seleciono "Alterar nome"
And eu preencho a senha com "hfm321"
And eu preencho novo nome com "Hugo" e novo sobrenome com "Marques"
Then eu recebo a mensagem de "Nome alterado com sucesso"

Scenario: Criação de usuário no sistema
Given não há contas criadas anteriormente com email "hfm@email.com"
When uma requisicao "POST" for enviada para "/user"