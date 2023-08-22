Feature: Divisão por gêneros

    Scenario: Ver um filme de ação
        Given: Um filme com id “1” está cadastrado no banco de dados para ação
        When: Um usuário faz uma requisição GET para “/acao/1”
        Then: O status da resposta deve ser “200”
        And: O JSON da resposta deve conter as informações do filme com id “1”

    Scenario: Filme de ação não cadastrado
        Given: Nenhum filme com id “15” está cadastrado no banco de dados para ação
        When: Um usuário faz uma requisição GET para “/acao/15”
        Then: O status da resposta deve ser “404”
        And: a mensagem de erro deve ser “Franchise not found”
