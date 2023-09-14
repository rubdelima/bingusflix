import React, {useEffect} from 'react';
import categories, {getMovies, getMovie} from "../../api.js";
import "./Banner.css";

function Banner() {
    const [movie, setMovie] = React.useState({});

    
    const fetchRandomMovie = async () => {
        try{
            const topTreading =  categories.find(
                (category) => category.name === "trending");
            const data = await getMovies(topTreading.path);
            const movies = data?.results;
            const randomIndex = Math.floor(Math.random() *movies.length);
            setMovie(movies[randomIndex]);
        }catch(e){
            console.log("error in Banner-fetchRandomMovie", e);
        }
    }

    useEffect(() => {
      fetchRandomMovie()
    }, []);

    function truncate(str) {
        try{
            if (str.length < 0) return ""
            return str?.length > 200? str.substring(0, 200) + "…" : str;
        }catch (e){
            console.log("Error in truncate", e)
            return "";
        }
    }
    

  return (
    <header 
    className='banner-container' 
    style={{
        backgroundSize: "cover",
        backgroundImage: `url("https://image.tmdb.org/t/p/original${movie?.backdrop_path}")`,
        roundPosition: "center-center",
    }}
    >
        <div className='banner-gradient'></div>
        <div className="banner-content">
            <h1 className="banner-title">
                {movie?.title || movie?.name || movie?.original_name}
            </h1>
            <div className='banner-button-container'>
                <button className="banner-button">Assistir</button>
                <button className="banner-button">Minha Lista + </button>
            </div>    
            <div className="banner-description">
                <h3>{truncate(movie?.overview)}</h3>
            </div>
        </div>
    </header>
  )
}

export default Banner