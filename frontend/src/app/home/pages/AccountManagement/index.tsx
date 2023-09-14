import styles from "./index.module.css";
import { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { fetchToken } from '../../components/auth';

function Account_recovery() {    
    const navigate = useNavigate(); 
    const [password, setPassword] = useState("");
    const [new_password, setNewPassword] = useState("");
    const [confirm_password, setConfirmPassword] = useState("");
    const [error_message, setErrorMessage] = useState("");
    const [success_message, setSuccessMessage] = useState("");

    const id = fetchToken();

    useEffect(() => {
        if (!id) {
          navigate('/home');
        }
      }, []);

    ///console.log(id);

    async function handleDeleteClick() {
        const response = await axios.delete('http://127.0.0.1:8000/users/' + Number(id));
        localStorage.removeItem('token');
        navigate('/home');
    }

    function handleGoBackClick() {
        navigate('/home-page'); 
    }

    async function handleSubmit(event) {
        event.preventDefault();
        
        const res = await axios.get(`http://localhost:4000/users/${Number(id)}`);
        let curr_passwd = res.data["passwd"];
        
        if (new_password !== confirm_password) {
            setErrorMessage("As senhas não coincidem");
            setSuccessMessage("");
            return;
        }
        

        if (password !== curr_passwd) {
            setErrorMessage("Senha incorreta");
            setSuccessMessage("");
            return;
        }

        
        res.data["passwd"] = new_password;
        console.log(res.data);
        try {
            const response = await axios.put(`http://127.0.0.1:8000/users/${Number(id)}`, res.data);
            
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
            <h2 className={styles.topBoxTest}>Gerenciamento de Conta</h2>
            <form onSubmit={handleSubmit}>
                <div className="input-container"><input
                    data-cy="senha-atual"
                    type="password"
                    placeholder="Sua senha atual"
                    className={styles.passwordInputField}
                    value = {password}
                    onChange = {(e) => setPassword(e.target.value)}
                    required
                    />
                </div>
                <div className="input-container"><input
                    data-cy="nova-senha"
                    type="password"
                    placeholder="nova senha"
                    className={styles.passwordInputField}
                    value = {new_password}
                    onChange = {(e) => setNewPassword(e.target.value)}
                    required
                    />
                </div>
                <div className="input-container"><input
                    data-cy="conf-senha"
                    type="password"
                    placeholder="confirmar senha"
                    className={styles.passwordInputField}
                    value={confirm_password}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    required
                    />
                </div>
                {error_message && <p className={styles.error}>{error_message}</p>}
                {success_message && <p data-cy="success-message" className={styles.success}>{success_message}</p>}
                <button data-cy="criar conta" type="submit" className={styles.confirmButton}>Confirmar</button>
            </form>
            <div  className={styles.accountRecoveryButtonsContainer}>
                <button data-cy="deletar conta" className={styles.textButton} onClick={handleDeleteClick}>Deletar Conta</button>
                <button className={styles.textButton} onClick={handleGoBackClick}>Voltar</button>
            </div>
        </div>
    </div>
  );
}

export default Account_recovery;
