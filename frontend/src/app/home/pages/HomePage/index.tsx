import Row from "../../components/Row/index.js";
import Banner from "../../components/Banner/index.js";
import Nav from "../../components/Nav/index.js";
import categories, {getMovies, getMovie} from "../../api.js";
import "./index.css";
import { fetchToken } from "../../components/auth.js";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import IndieRow from "../../components/IndieRow/index.js";
import axios from 'axios';
import React from "react";


function Home() {

    const navigate = useNavigate();

    const [historyMovies, setHistoryMovies] = React.useState([]);
    const [historyTv, setHistoryTv] = React.useState([]);
    const [historyAll, setHistoryAll] = React.useState([]);

    useEffect(() => {
      if (!fetchToken()) {
        navigate('/home');
      }
    }, []);

    const getLastSeensRow = async () => {
      const token = localStorage.getItem("token");
      const config = { headers: { Authorization: `Bearer ${token}`,},};
      const response = await axios.get('http://localhost:8000/history/videos/', config);
      console.log("Historico: ", response);
      setHistoryTv(response.data.tv);
      setHistoryMovies(response.data.movie);
      setHistoryAll(response.data.all);
    }

    useEffect(() => {getLastSeensRow();}, []);

    return (
      <div className="Home">

        <Nav />
        <Banner />
        <h2 className="homeHead">Assistidos Recentemente</h2>
        <IndieRow videoArray={historyAll} tipo={"homePage"}/>
        {categories.map((category) => {
            return (
                <Row 
                key={category.name}
                title={category.title}
                path={category.path}
                isLarge={category.isLarge}
                tipo={category.tipo}
            />
            );
        })}
      </div>
    );
  }

export default Home;