import React, {useEffect} from 'react';
import "./Nav.css";

function Nav() {

  const [show, setShow] = React.useState(false);

  useEffect(() => {
    window.addEventListener("scroll", () => {
      setShow(window.scrollY > 100);
    });
  }, []);

  return (
    <div className={`nav-container ${show && "nav-container-black"}`}>
    <img 
      className='nav-logo' 
      src='/imgs/bingusflix_logo.png' 
      alt='BingusFlix'
    ></img>
    <div className='buttons-nav-container'>
      <button className='buttons-nav'>Em Alta</button>
      <button className='buttons-nav'>Filmes</button>
      <button className='buttons-nav'>Séries</button>
      <button className='buttons-nav'>Últimos Assistidos</button>
      <button className='buttons-nav'>Histórico</button>
    </div>
    <img
      className='nav-avatar'
      src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPsVAeFlYeYOEUzb3TV1ML91_LPkkFML5lRQcMdr9nQu2CqO-WzT-RLmkM5_cOKvkaBkI&usqp=CAU'
      alt='User'
    ></img>
  </div>
  );
}

export default Nav;