const API_KEY = "634aea3498138161f7c175397bc5a836";

const categories = [
    {
        name: "suspense_tv",
        title: "Séries de suspense",
        path: `/discover/tv?api_key=${API_KEY}&with_genres=9648`,
        isLarge: false
    },
    {
        name: "suspense_movies",
        title: "Filmes de suspense",
        path: `/discover/movie?api_key=${API_KEY}&with_genres=53`,
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