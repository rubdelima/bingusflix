import styles from "./index.module.css";
import { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { fetchToken } from '../../components/auth';

function Account_recovery() {


    const navigate = useNavigate(); 
    const [email, setEmail] = useState("");
    const [new_password, setNewPassword] = useState("");
    const [confirm_password, setConfirmPassword] = useState("");
    const [error_message, setErrorMessage] = useState("");
    const [success_message, setSuccessMessage] = useState("");


    useEffect(() => {
        if (fetchToken()) {
          navigate('/logged');
        }
    }, []);

    function handleRegisterClick() {
        navigate('/users');
    }

    function handleLoginClick() {
        navigate('/login'); 
    }

    async function handleSubmit(event) {
        event.preventDefault();
    
        if (new_password !== confirm_password) {
            setErrorMessage("As senhas não coincidem");
            setSuccessMessage("");
            return;
        }
        
        try {
            const response = await axios.put('http://localhost:8000/account_recovery', {
                email: email, 
                new_password: new_password,
                confirm_password: confirm_password
            });
            
            console.log(response.status);
            setSuccessMessage("Sua senha foi alterada com sucesso!");
            setErrorMessage("");
        } catch (error) {
            console.error(error);
            setErrorMessage("Não foi possível alterar sua senha");
        }
    }
    

  return (
    <div className={styles.container}>
        <h1 className={styles.topText}>Bingusflix</h1>
        <div className={styles.centralizedBox}>
            <h2 className={styles.topBoxTest}>Recuperação de conta</h2>
            <form onSubmit={handleSubmit}>
                <div className="input-container"><input
                    type="email"
                    placeholder="exemplo@email.com"
                    className={styles.emailInputField}
                    value = {email}
                    onChange = {(e) => setEmail(e.target.value)}
                    required
                    />
                </div>
                <div className="input-container"><input
                    type="password"
                    placeholder="nova senha"
                    className={styles.passwordInputField}
                    value = {new_password}
                    onChange = {(e) => setNewPassword(e.target.value)}
                    required
                    />
                </div>
                <div className="input-container"><input
                    type="password"
                    placeholder="confirmar senha"
                    className={styles.passwordInputField}
                    value={confirm_password}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    required
                    />
                </div>
                {error_message && <p className={styles.error}>{error_message}</p>}
                {success_message && <p className={styles.success}>{success_message}</p>}
                <button type ="submit" className={styles.confirmButton}>Confirmar</button>
            </form>
            <div className={styles.accountRecoveryButtonsContainer}>
                <button className={styles.textButton} onClick={handleRegisterClick}>Cadastre-se</button>
                <button className={styles.textButton} onClick={handleLoginClick}>Entrar</button>
            </div>
        </div>
    </div>
  );
}

export default Account_recovery;
