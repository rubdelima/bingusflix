Feature: Recuperação de conta

Scenario: Usuário altera sua senha por meio da recuperação de conta
Given um usuário com email "felipe@gmail.com" e senha "senha123" está cadastrado no sistema
When um usuário envia uma requisição PUT para "/account_recovery" com email "felipe@gmail.com" e nova senha "senha456" e confirmação de senha "senha456"
Then o status da resposta deve ser "200"
And o JSON da resposta deve conter o usuário com email "felipe@gmail.com" e senha "senha456"

Scenario: E-mail inválido na recuperação de conta
Given que nenhum usuário com email "fred@gmail.com" está cadastrado no sistema
When um usuário envia uma requisição PUT para "/account_recovery" com email "fred@gmail.com" e nova senha "novasenha" e confirmação de senha "novasenha"
Then o status da resposta deve ser "404"
And a mensagem de erro deve ser "User not found"

Scenario: Confirmação de senha diferente da nova senha
Given que um usuário com email "felipe@gmail.com" e senha "senha123" está cadastrado no sistema
When o usuário envia uma requisição PUT para "/account_recovery" com email "felipe@gmail.com", nova senha "senha456" e confirmação de senha "senha789"
Then o status da resposta deve ser "400"
And a mensagem de erro deve ser "Passwords do not match"
