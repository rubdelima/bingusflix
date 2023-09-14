import requests

API_KEY = "634aea3498138161f7c175397bc5a836"

categories = [
    {
        "name": "action_tv",
        "title": "Séries de ação",
        "path": f"/discover/tv?api_key={API_KEY}&with_genres=10759"
    },
    {
        "name": "action_movies",
        "title": "Filmes de ação",
        "path": f"/discover/movie?api_key={API_KEY}&with_genres=28"
    },
    {
        "name": "comedy_tv",
        "title": "Séries de comédia",
        "path": f"/discover/tv?api_key={API_KEY}&with_genres=35&include_adult=false"
    },
    {
        "name": "comedy_movies",
        "title": "Filmes de comédia",
        "path": f"/discover/movie?api_key={API_KEY}&with_genres=35&include_adult=false"
    },
    {
        "name": "ficction_tv",
        "title": "Séries de ficcção científica",
        "path": f"/discover/tv?api_key={API_KEY}&with_genres=10765"
    },
    {
        "name": "ficction_movies",
        "title": "Filmes de ficcção científica",
        "path": f"/discover/movie?api_key={API_KEY}&with_genres=878"
    },
    {
        "name": "romance_tv",
        "title": "Séries de romance",
        "path": f"/discover/tv?api_key={API_KEY}&with_genres=10749&include_adult=false"
    },
    {
        "name": "romance_movies",
        "title": "Filmes de romance",
        "path": f"/discover/movie?api_key={API_KEY}&with_genres=10749&include_adult=false"
    },
    {
        "name": "suspense_tv",
        "title": "Séries de suspense",
        "path": f"/discover/tv?api_key={API_KEY}&with_genres=9648"
    },
    {
        "name": "suspense_movies",
        "title": "Filmes de suspense",
        "path": f"/discover/movie?api_key={API_KEY}&with_genres=53"
    },
    {
        "name": "trending_tv",
        "title": "Séries em alta",
        "path": f"/trending/tv/week?api_key={API_KEY}&language=pt-BR"
    },
    {
        "name": "trending_movies",
        "title": "Filmes em alta",
        "path": f"/trending/movie/week?api_key={API_KEY}&language=pt-BR"
    }
]

def get_movies(path):
    try:
        url = f"https://api.themoviedb.org/3{path}"
        response = requests.get(url)
        return response.json()
    except Exception as error:
        print("error getMovies:", error)

"""if __name__ == "__main__":
    for category in categories:
        movie_data = get_movies(category["path"])
        print(f"{category['title']} Data:")
        print(movie_data)"""


