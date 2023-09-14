Feature: Gender Division
    As a usuário
    I want to ver uma página para um gênero específico
    So that eu consigo ver os filmes e séries desse gênero

Scenario: Acessar a página de um gênero
    Given o usuário de id "1" está logado
    And o usuário está na página "home-page"
    When clica no botão "Gêneros"
    And clica no botão "Ação"
    Then o usuário é direcionado para a "acao"