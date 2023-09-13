import React, { useEffect, useRef } from 'react';
import { getMovies } from '../api.js';
import './IndieRow.css';

const imageHost = 'https://image.tmdb.org/t/p/original/';

function IndieRow({ videoArray, isLarge }) {
    const scrollContainerRef = useRef(null);

    const [videoDict, getVideoData] = React.useState(null);

    const fetchVideoData = async () => {

    };
  
    // Função para rolagem
    const scrollLeft = () => {
        if (scrollContainerRef.current) {
            const scrollContainer = scrollContainerRef.current;
            const newPosition = scrollContainer.scrollLeft - 800; // Altere o valor para ajustar o quanto deseja rolar
            scrollToSmoothly(scrollContainer, newPosition, 500); // Chamada da função de rolagem suave
        }
    };

    const scrollRight = () => {
        if (scrollContainerRef.current) {
            const scrollContainer = scrollContainerRef.current;
            const newPosition = scrollContainer.scrollLeft + 800; // Altere o valor para ajustar o quanto deseja rolar
            scrollToSmoothly(scrollContainer, newPosition, 500); // Chamada da função de rolagem suave
        }
    };

    const scrollToSmoothly = (element, to, duration) => {
        const start = element.scrollLeft;
        const change = to - start;
        let currentTime = 0;
        const increment = 20;

        const animateScroll = () => {
            currentTime += increment;
            const val = Math.easeInOutQuad(currentTime, start, change, duration);
            element.scrollLeft = val;
            if (currentTime < duration) {
                requestAnimationFrame(animateScroll);
            }
        };

        animateScroll();
    };

    Math.easeInOutQuad = (t, b, c, d) => {
        t /= d / 2;
        if (t < 1) return (c / 2) * t * t + b;
        t--;
        return (-c / 2) * (t * (t - 2) - 1) + b;
    };

    
    const [selectedMovie, setSelectedMovie] = React.useState(null);

    const handleMovieClick = (movieId) => {
      console.log("selected movie: " , movieId);
      setSelectedMovie(movieId);
      console.log(selectedMovie);
    };

    const handleCloseModal = () => {
      setSelectedMovie(null);
    };
    
    return (
        <div className='indie-row-container'>
            <div className='row-cards-container'>
                <button className='scroll-button left-button' onClick={scrollLeft}>
                    &lt;
                </button>
                {console.log("Video Array: ", videoArray)}
                <div className='row-cards' ref={scrollContainerRef}>
                    {videoArray?.map((movie) => {
                        return (
                            <div className="movie-card-content"
                                key={movie.id}
                                onClick={() => handleMovieClick(movie)}
                            >
                                <img
                                    className={isLarge ? "movie-image-large" :"movie-image"}
                                    src={`${imageHost}${movie?.still_path || movie?.movie.backdrop_path ||  movie?.poster_path}`}
                                    alt={movie.name}
                                />
                                <div className="movie-card-overlay">
                                    <div className="movie-title">{movie?.title || movie?.name || movie?.original_name}</div>
                                </div>
                            </div>
                        );
                    })}
                </div>
                <button className='scroll-button right-button' onClick={scrollRight}>
                    &gt;
                </button>
            </div>
        </div>
    );
    
}

export default IndieRow;
