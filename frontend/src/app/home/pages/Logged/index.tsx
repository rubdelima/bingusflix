// PÁGINA CRIADA APENAS PARA TESTAR O LOGIN E O LOGOUT //


import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import { fetchToken } from '../../components/auth';

function Logged() {
    

    const navigate = useNavigate();

    useEffect(() => {
        if (!fetchToken()) {
          navigate('/login');
        }
    }, []);

    function handleLogOutClick() {
        localStorage.removeItem("token");
        navigate("/login");
    }

    return (
        <div className="container">
            <button onClick={handleLogOutClick}>LogOut</button>
        </div>
    );
}

export default Logged;