Feature: Histórico de um Profile

Scenario: Inserção de um Filme que está presente no Banco de Dados
    Given um profile de id "1" do usuário com id "1" e e-mail "felipe@gmail.com" e senha "senha123" está cadastrado no sistema
    When o usuário envia uma requisição POST para "/history/register_access_video/" com o video "8"
    Then recebo o status da resposta "201"
    And o JSON da resposta deve conter dados relacionados ao video "8"

Scenario: Obter todo o histórico de um Profile
    Given um profile de id "1" do usuário com id "1" e e-mail "felipe@gmail.com" e senha "senha123" está cadastrado no sistema
    And ele tem os videos de "1" a "12" no seu histórico
    When o usuário envia uma requisição GET para "/history/"
    Then recebo o status da resposta "200"
    And o JSON da resposta deve conter uma lista com dados relacionados a todos os 12 videos assistidos

Scenario: Obter o histórico de filmes um Profile
    Given um profile de id "1" do usuário com id "1" e e-mail "felipe@gmail.com" e senha "senha123" está cadastrado no sistema
    And ele tem os filmes "8" e "9" no seu histórico
    When o usuário envia uma requisição GET para "/history/movies/"
    Then recebo o status da resposta "200"
    And o JSON da resposta deve conter uma lista com os filmes "8" e "9"

Scenario: Obter infos de um filme do historico
    Given um profile de id "1" do usuário com id "1" e e-mail "felipe@gmail.com" e senha "senha123" está cadastrado no sistema
    And ele tem os filmes "10" e "9" no seu histórico
    When o usuário envia uma requisição GET para "/history/movies/Inception/"
    Then recebo o status da resposta "200"
    And o JSON da resposta deve conter informacões sobre o filme "10" como name "Inception".

Scenario: Obter infos das séries do histórico
    Given um profile de id "1" do usuário com id "1" e e-mail "felipe@gmail.com" e senha "senha123" está cadastrado no sistema
    And ele ja assistiu os videos de id "1" da série "Breaking Bad"
    When o usuário envia uma requisição GET para "/history/series/"
    Then recebo o status da resposta "200"
    And o JSON da resposta deve conter uma lista com as séries assistidas
    And na série "Breaking Bad" o episódio atual é o "1 - O Inicio de Tudo" e o próximo "2 - O Segundo Episodio"