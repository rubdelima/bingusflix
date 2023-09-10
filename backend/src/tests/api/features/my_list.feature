Feature: Minha lista

    Scenario: Add an item to my list
        Given nao ha filme com titulo "Star Wars" na minha lista
        When o usuario envia uma requisicao POST para "/my-list/movie" com adult "false", backdrop_path "/4iQzWyPH.jpg", genre_ids "[35, 1075]", id "12", original_language "en", original_title "Star Wars", overview "Princess Leia is captured...", popularity "7360.0", poster_path "/btI2o6.jpg", release_date "1977-05-25", title "Star Wars", video "false", vote_average "8.2", vote_count "108544"
        Then o status da reposta deve ser "201"
        And a reposta deve conter o titulo "Star Wars"

    Scenario: remove an item from my list
        Given o filme com titulo "Star Wars" esta na minha lista
        When o usuario envia uma requisicao DELETE para "/my-list"
        Then o status da reposta deve ser "200"