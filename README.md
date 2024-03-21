
# BingusFlix
![](https://github.com/rubdelima/bingusflix/blob/main/frontend/public/imgs/bingusflix_logo.png?raw=true)

Um projeto da classe de Engenharia de Software e Sistemas da UFPE. Nosso projeto consiste em emular um site de serviço de streaming de filmes e séries.

A project from the Software and Systems Engineering class at UFPE. Our project consists of emulating a movie and series streaming service website.

## Principais bibliotecas / Main libraries:
* Backend:  Uvicorn, FastAPT (python)
* Frontend: React.js (npm)
* Database: JsonServer (npm)

## Como executar?
### Database
1. Utilize o comando `npm install json-server` para instalar o json server.
2. Para iniciar o Banco de Dados utlize:
```shell
json-server -p 4000 -w .\backend\src\db\db.json  
```

1. Use the `npm install json-server` command to install json server.
2. To start the Database use:
```shell
json-server -p 4000 -w .\backend\src\db\db.json
```

### Backend
1. Para iniciar o backend é preciso ter o python3 intalado, ao menos na versão 3.10, e o pip também instalado.
2. Após ter o python e pip instalados vá no diretório `./backend/` e rode o seguinte comando para instalar as dependências do backend:
`pip install -r requirements.txt`
3. Com as dependências instaladas execute o comando: `python3 -m uvicorn src.main:app --reload` para iniciar o backend no fastAPI. Os dados podem ser vistos em `localhost:8000/docs/`

1. To start the backend you need to have python3 installed, at least version 3.10, and pip also installed.
2. After having python and pip installed, go to the `./backend/` directory and run the following command to install the backend dependencies:
`pip install -r requirements.txt`
3. With the dependencies installed, run the command: `python3 -m uvicorn src.main:app --reload` to start the backend in fastAPI. Data can be seen at `localhost:8000/docs/`

### Frontend
1. Vá para o diretório `./frontend/`
2. Execute o comando `npm install` para instalar todas as dependências
3. Vá para o diretório `/src/` e execute o comando `npm run dev` para iniciar a aplicação.

### Frontend
1. Go to the `./frontend/` directory
2. Run the `npm install` command to install all dependencies
3. Go to the `/src/` directory and run the `npm run dev` command to start the application.

## Imagens do Projeto
### Homepage
![](https://github.com/rubdelima/bingusflix/blob/main/images/homepage-1.png?raw=true)

![](https://github.com/rubdelima/bingusflix/blob/main/images/homepage-2.png?raw=true)

![](https://github.com/rubdelima/bingusflix/blob/main/images/homepage-3.png?raw=true)

### Login
![](https://github.com/rubdelima/bingusflix/blob/main/images/login.png?raw=true)

### Sign UP
![](https://github.com/rubdelima/bingusflix/blob/main/images/sign-up.png?raw=true)

### On Boarding
![](https://github.com/rubdelima/bingusflix/blob/main/images/onBoarding.png?raw=true)

### Profiles
![](https://github.com/rubdelima/bingusflix/blob/main/images/profiles.png?raw=true)