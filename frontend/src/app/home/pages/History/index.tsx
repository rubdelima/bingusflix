import Row from "../../components/Row/index.js";
import Banner from "../../components/Banner/index.js";
import Nav from "../../components/Nav/index.js";
import "./index.css";
import { fetchToken } from "../../components/auth.js";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import React from "react";
import axios from 'axios';
import VideoInfo from "../../components/VideoInfo/index.js";

function History() {
    const navigate = useNavigate();

    const [selectedButton, setSelectedButton] = React.useState("Todos");
    const [historyMovies, setHistoryMovies] = React.useState([]);
    const [historyTv, setHistoryTv] = React.useState([]);
    const [historyAll, setHistoryAll] = React.useState([]);
    const [selectedArray, setSelectedArray] = React.useState([]);

    useEffect(() => {
      getLastSeensRow();
    }, []);

    useEffect(() => {
      // Atualize selectedArray quando qualquer um dos arrays de histórico mudar
      setSelectedArray(() => {
        switch(selectedButton){
          case "Series" : return historyTv;
          case "Filmes" : return historyMovies;
          case "Todos"  : return historyAll;
          default: return [];
        }
      });
    }, [selectedButton, historyAll, historyMovies, historyTv]);

    const getLastSeensRow = async () => {
      const token = localStorage.getItem("token");
      const config = { headers: { Authorization: `Bearer ${token}`,},};
      const response = await axios.get('http://127.0.0.1:8000/history/videos/', config);
      console.log("Historico: ", response);
      setHistoryTv(response.data.tv);
      setHistoryMovies(response.data.movie);
      setHistoryAll(response.data.all);
    }

    useEffect(() => {
      if (!fetchToken()) {
        navigate('/home');
      }
    }, []);

    const [selectedMovie, setSelectedMovie] = React.useState(null);

    const handleMovieClick = (movieId) => {
      setSelectedMovie(movieId);
      console.log(selectedMovie);
    };

    const handleCloseModal = () => {
      setSelectedMovie(null);
    };

    return (
      <div className="History">
        <Nav />
        <Banner />
        <div className="select-history-container">
          <button className={(selectedButton === "Todos") ? 'history-button-selected' :'history-button'} 
                  data-cy='Todos'
                  onClick={() => setSelectedButton("Todos")}>Todos</button>
          <button className={(selectedButton === "Filmes") ? 'history-button-selected' :'history-button'}
                  data-cy='Filmes'
                  onClick={() => setSelectedButton("Filmes")}>Filmes</button>
          <button className={(selectedButton === "Series") ? 'history-button-selected' :'history-button'}
                  data-cy='Series'
                  onClick={() => setSelectedButton("Series")}>Series</button>
        </div>
        <div>
          {selectedArray.map((video) => {
            return(
              <div className="history-row"
              onClick={() => handleMovieClick(video)}>
                <img className="image-history" src={`https://image.tmdb.org/t/p/original/${video.backdrop_path}`} alt="" />
                <h1 className="name-video-history" data-cy='Videos' >{video.title || video.name}</h1>
              </div>
            )
          })}
          <div>
          {selectedMovie !== null && (
                <VideoInfo movie={selectedMovie} onClose={handleCloseModal}/>
          )}
          </div>
        </div>
      </div>
    );
  }

export default History;
