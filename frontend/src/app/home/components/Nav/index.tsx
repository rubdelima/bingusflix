import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "./Nav.css";

function Nav() {
  const [show, setShow] = useState(false);
  const [isModalOpenGender, setIsModalOpenGender] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/home');
  }

  const handleProfiles = () => {
    navigate('/profiles')
  }

  const handleAccount = () => {
    navigate('/account-management')
  }

  const handleProfileClick = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setIsModalOpenGender(false);
  };


  const handleGenderClick = () => {
    setIsModalOpenGender(true);
  }

  const handleComedyClick = () => {
    navigate('/comedia');
  }

  const handleActionClick = () => {
    navigate('/acao');
  }

  const handleFicctionClick = () => {
    navigate('/ficcao');
  }

  const handleRomanceClick = () => {
    navigate('/romance');
  }

  const handleSuspenseClick = () => {
    navigate('/suspense');
  }

  const handleLogoClick = () => {
    navigate('/home-page');
  }

  const handleHistoryClick = () => {
    navigate('/history');
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
        onClick={handleLogoClick}
      ></img>
      <div className='buttons-nav-container'>
        <button className='buttons-nav'>Em Alta</button>
        <button className='buttons-nav'>Filmes</button>
        <button className='buttons-nav'>Séries</button>
        <button className='buttons-nav'>Últimos Assistidos</button>
        <button className='buttons-nav'>Histórico</button>
        <div className='gender-click' onClick={handleGenderClick}>
          <button data-cy='Gêneros' type='submit' className='buttons-nav'>Gêneros</button>
        </div>
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
<<<<<<< HEAD:frontend/src/app/home/components/Nav.tsx
            <button className='profile-button' onClick={handleAccount}>Conta</button>
            <button className='profile-button' onClick={handleProfiles}>Perfis</button>
            <button className='profile-button' onClick={handleLogout}>Logout</button>
=======
            <button className='popup-button' >Conta</button>
            <button className='popup-button' onClick={handleProfiles}>Perfis</button>
            <button className='popup-button' onClick={handleLogout}>Logout</button>
            <button className='popup-button' onClick={handleHistoryClick}>Histórico</button>
>>>>>>> 73058bc415233dc1711ec1c70e7e3aa1b3865833:frontend/src/app/home/components/Nav/index.tsx
          </div>
        </div>
      )}

      {isModalOpenGender && (
              <div className='modal'>
                <div className='modal-content'>
                  <span className='close' onClick={closeModal}>
                    X
                  </span>
                  <button data-cy='Ação' type='submit' className='popup-button' onClick={handleActionClick}>Ação</button>
                  <button className='popup-button' onClick={handleComedyClick}>Comédia</button>
                  <button className='popup-button' onClick={handleRomanceClick}>Romance</button>
                  <button className='popup-button' onClick={handleSuspenseClick}>Suspense</button>
                  <button className='popup-button' onClick={handleFicctionClick}>Ficção</button>
                </div>
              </div>
      )}
    </div>
  );
}

export default Nav;