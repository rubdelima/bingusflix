Feature: Historico
  As a usuário
  I want to ver meu historico

Scenario: Consulta do Historico de Filmes
  Given o usuário de id "1" está logado
  And o usuário está na página "history"
  When o usuário clica em "Filmes"
  Then é exibido uma lista de "Videos" com "Barbie"

Scenario: Consulta do Historico de Series
  Given o usuário de id "1" está logado
  And o usuário está na página "history"
  When o usuário clica em "Series"
  Then é exibido uma lista de "Videos" com "One Piece"

Scenario: Consulta do Historico Geral
  Given o usuário de id "1" está logado
  And o usuário está na página "history"
  When o usuário clica em "Todos"
  Then é exibido uma lista de "Videos" com "Barbie"