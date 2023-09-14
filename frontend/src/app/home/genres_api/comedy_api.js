const API_KEY = "634aea3498138161f7c175397bc5a836";

const categories = [
    {
        name: "comedy_tv",
        title: "Séries de comédia",
        path: `/discover/tv?api_key=${API_KEY}&with_genres=35&include_adult=false`,
        isLarge: false
    },
    {
        name: "comedy_movies",
        title: "Filmes de comédia",
        path: `/discover/movie?api_key=${API_KEY}&with_genres=35&include_adult=false`,
        isLarge: false
    }
]

export const getMovies = async (path) => {
    try {
        let url= `https://api.themoviedb.org/3${path}`;
        const response = await fetch(url);
        return await response.json();
    }catch (error){
        console.log("error getMovies: ", error);
    }
};

export default categories;