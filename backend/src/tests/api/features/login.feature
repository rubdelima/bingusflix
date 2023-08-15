Feature: Login de usuário

Scenario: Login bem sucedido de um usuário
Given um usuário com id "1" e e-mail "felipe@gmail.com" e senha "senha123" está cadastrado no sistema
When o usuário envia uma requisição "POST" para "/login" com e-mail "felipe@gmail.com" e senha "senha123"
Then o status da resposta deve ser "200"
And o JSON da resposta deve conter um token de acesso válido com o valor "1" e tipo "bearer"

Scenario: E-mail não cadastrado no sistema
Given nenhum usuário com e-mail "fred@gmail.com" está cadastrado no sistema
When o usuário envia uma requisição "POST" para "/login" com e-mail "fred@gmail.com" e senha "qualquer"
Then o status da resposta deve ser "404"
And a mensagem de erro deve ser "User not found"

Scenario: Senha incorreta
Given um usuário com e-mail "felipe@gmail.com" e senha "senha123" está cadastrado no sistema
When o usuário envia uma requisição "POST" para "/login" com e-mail "felipe@gmail.com" e senha "senha456"
Then o status da resposta deve ser "401"
And a mensagem de erro deve ser "Wrong password"
