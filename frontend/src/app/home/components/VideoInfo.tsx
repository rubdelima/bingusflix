import React, {useEffect}  from 'react';
import './VideoInfo.css';
import IndieRow from './IndieRow';
import {getSerieDetails, getSeasonDetails} from '../api';

function VideoInfo({ movie, onClose }) {
    console.log("filme selecionado: ",movie);

    const [serie, setSerie] = React.useState(null);
    const [selectedSeason, setSelectedSeason] = React.useState(null);

    const [arraySeason, setSelectedArraySeason] = React.useState(null);
    
    const fetchSerieInfo = async (_video_id) =>{
        try {
            const data = await getSerieDetails(_video_id);
            setSerie(data);
        } catch (e){
            console.log('fetchSerieInfo error: ', e);
        }
    };

    const fetchSelectedArraySeason = async (seasonIndex) =>{
        try {
            console.log("Palao", movie.id, seasonIndex)
            const data = await getSeasonDetails(movie.id, seasonIndex);
            console.log(data?.episodes);
            setSelectedArraySeason(data?.episodes);
        } catch (e){
            console.log('fetchSelectedArraySeason error: ', e);
        }
    }

    useEffect(() => {fetchSerieInfo(movie.id);}, []);
    
    return (
        <div className='video-info-overlay'>
            <div className='video-info-content'>
                <button className='button-close' onClick={onClose}>X</button>
                <header
                style={{
                    backgroundSize: "cover",
                    backgroundImage: `url("https://image.tmdb.org/t/p/original${movie?.backdrop_path}")`,
                    roundPosition: "center-center",
                    width: "100%",
                    height: "100%"
                }}
                >
                    <div className='cover-overlay'></div>
                    <div className='info-content'>
                        <h1 className="info-title">
                            {movie?.title || movie?.name || movie?.original_name}
                        </h1>
                        <div className='info-button-container'>
                            <button className="info-button">Assistir</button>
                            <button className="info-button">Minha Lista + </button>
                        </div>    
                        <div className="info-description">
                            <h3>{movie?.overview}</h3>
                            {movie.media_type === 'tv' &&
                                <div className='select-season'>
                                    <select
                                    className='select-season'
                                      value={selectedSeason ? selectedSeason.name : ""}
                                      onChange={(e) => {
                                        const selectedName = e.target.value;
                                        const selected = serie.seasons.find(
                                          (season) => season.name === selectedName
                                        );
                                        const selectedIndex = serie.seasons.findIndex(
                                            (season) => season.name === selectedName
                                          );
                                        setSelectedSeason(selected);
                                        fetchSelectedArraySeason(selectedIndex);
                                      }}
                                    >
                                      <option value="">Selecione uma temporada</option>
                                      {serie?.seasons.map((season) => (
                                        <option key={season.id} value={season.name}>
                                          {season.name}
                                        </option>
                                      ))}
                                    </select>
                              </div>
                            }
                            
                        </div>
                        
                    </div>{selectedSeason && arraySeason && (
                                <IndieRow videoArray={arraySeason} isLarge={true}/>
                            )}
                </header>
            </div>
        </div>
    );
}

export default VideoInfo;