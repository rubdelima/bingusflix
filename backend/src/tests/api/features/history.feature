Feature: Histórico de um Profile

Scenario: Inserção de um Filme que está presente no Banco de Dados
    Given um profile de id "1" do usuário com id "1" e e-mail "felipe@gmail.com" e senha "senha123" está cadastrado no sistema
    When o usuário envia uma requisição POST para "/history/register_access_video/" com o video "8"
    Then recebo o status da resposta "201"
    And o JSON da resposta deve conter dados relacionados ao video "8"