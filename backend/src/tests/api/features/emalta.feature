Scenario: Ver lista de filmes Em alta
    Given: o read_filmesEmAlta retorna uma lista de items
    When: uma requisição GET for enviada para '/filmesEmAlta'
    Then: o status de resposta deve ser '200'
    And: o JSON da resposta deve ser uma lista de itens
    