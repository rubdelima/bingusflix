import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "./Nav.css";

function Nav() {
  const [show, setShow] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/home');
  }

  const handleProfiles = () => {
    navigate('/profiles')
  }

  const handleProfileClick = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const handleHistory = () =>{
      navigate('/history');
  }

  const handleHomePage = () =>{
    navigate('/home-page');
  }

  useEffect(() => {
    window.addEventListener('scroll', () => {
      setShow(window.scrollY > 100);
    });
  }, []);

  return (
    <div className={`nav-container ${show && 'nav-container-black'}`}>
      <img
        className='nav-logo'
        src='/imgs/bingusflix_logo.png'
        alt='BingusFlix'
        onClick={handleHomePage}
      ></img>
      <div className='buttons-nav-container'>
        <button className='buttons-nav'>Em Alta</button>
        <button className='buttons-nav'>Filmes</button>
        <button className='buttons-nav'>Séries</button>
        <button className='buttons-nav'>Últimos Assistidos</button>
        <button className='buttons-nav'>Histórico</button>
      </div>
      <div className='profile-click' onClick={handleProfileClick}>
        <img
          className='nav-avatar'
          src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPsVAeFlYeYOEUzb3TV1ML91_LPkkFML5lRQcMdr9nQu2CqO-WzT-RLmkM5_cOKvkaBkI&usqp=CAU'
          alt='User'
        ></img>
      </div>

      {isModalOpen && (
        <div className='modal'>
          <div className='modal-content'>
            <span className='close' onClick={closeModal}>
              X
            </span>
            <button className='profile-button' >Conta</button>
            <button className='profile-button' onClick={handleProfiles}>Perfis</button>
            <button className='profile-button' onClick={handleLogout}>Logout</button>
            <button className='profile-button' onClick={handleHistory}>Histórico</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Nav;