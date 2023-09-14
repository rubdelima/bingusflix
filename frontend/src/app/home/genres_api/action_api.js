const API_KEY = "634aea3498138161f7c175397bc5a836";

const categories = [
    {
        name: "action_tv",
        title: "Séries de ação",
        path: `/discover/tv?api_key=${API_KEY}&with_genres=10759`,
        isLarge: false
    },
    {
        name: "action_movies",
        title: "Filmes de ação",
        path: `/discover/movie?api_key=${API_KEY}&with_genres=28`,
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