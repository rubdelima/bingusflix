Feature: Favorites

    Scenario: Adição bem sucedida de um favorite
        Given um usuário com id "1", e-mail "fal5@gmail.com", senha "senha123" está logado no sistema com o perfil com id "1"
        And esse usuário possui "0" favoritos
        When o usuário envia uma requisição POST para "/favorites" com id do vídeo "1"
        Then o status da resposta deve ser "201"
        And o JSON da resposta deve conter o id do vídeo "1", o id do usuário "1", o id do perfil "1" e o id do favorito "1"
    
    # Scenario: Remove um favorite
    #     Given um usuário com id "1", e-mail "fal5@gmail.com", senha "senha123" está logado no sistema com o perfil com id "1"
    #     And esse usuário possui "2" favoritos
    #     When o usuário envia uma requisição DELETE para "/favorites/1"
    #     Then o status da resposta deve ser "200"
    #     And esse usuário possui "1" favoritos
    
    # Scenario: Mostra todos os favorites de um usuário
    #     Given um usuário com id "1", e-mail "fal5@gmail.com", senha "senha123" está logado no sistema com o perfil com id "1"
    #     And esse usuário possui "2" favoritos: favorito com id "1" e vídeo "20" e favorito com id "2" e vídeo "12"
    #     When o usuário envia uma requisição GET para "/favorites"
    #     Then o status da resposta deve ser "200"
    #     And o JSON da resposta deve conter o id do vídeo "20", o id do usuário "1", o id do perfil "1" e o id do favorito "1" e o id do vídeo "12", o id do usuário "1", o id do perfil "1" e o id do favorito "2"