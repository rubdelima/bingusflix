import Row from "../../components/Row.js";
import Banner from "../../components/Banner.js";
import Nav from "../../components/Nav.js";
import categories from "../../api.js";
import "./index.css";
import { fetchToken } from "../../components/auth.js";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function Home() {

    const navigate = useNavigate();

    useEffect(() => {
      if (!fetchToken()) {
        navigate('/home');
      }
    }, []);

    return (
      <div className="Home">
        <Nav />
        <Banner />
        {categories.map((category) => {
            return (
                <Row 
                key={category.name}
                title={category.title}
                path={category.path}
                isLarge={category.isLarge}
            />
            );
        })}
      </div>
    );
  }

export default Home;