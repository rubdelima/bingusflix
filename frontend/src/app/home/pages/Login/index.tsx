import styles from "./index.module.css";
import { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { setToken, fetchToken } from '../../components/auth';

function Login() {
    

    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error_message, setErrorMessage] = useState("");

    useEffect(() => {
        if (fetchToken()) {
          navigate('/logged');
        }
    }, []);


    function handleForgotPasswordClick() {
        navigate('/account_recovery');
    }

    async function handleSubmit(event) {
        event.preventDefault();

        const formData = new FormData();
        formData.append('username', email);
        formData.append('password', password);

        try {
            const response = await axios.post('http://localhost:8000/login', formData);
            setErrorMessage("");
            setToken(response.data.token);
            navigate('/logged');
        } catch (error) {
            console.error(error);
            setErrorMessage("Usuário ou senha incorretos");
}
    }

    return (
        <div className={styles.container}>
            <h1 className={styles.topText}>Bingusflix</h1>
            <div className={styles.centralizedBox}>
                <h2 className={styles.topBoxTest}>Login</h2>
                <form onSubmit={handleSubmit}>
                    <div className={styles.inputContainer}>
                        <input
                            type="email"
                            placeholder="exemplo@email.com"
                            className={styles.emailInputField}
                            name="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>
                    <div className={styles.inputContainer}>
                        <input
                            type="password"
                            placeholder="senha"
                            className={styles.passwordInputField}
                            name="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>
                    {error_message && <p className={styles.error}>{error_message}</p>}
                    <button type="submit" className={styles.loginButton}>Entrar</button>
                </form>
                <div className={styles.loginButtonsContainer}>
                    <button className={styles.textButton}>Cadastre-se</button>
                    <button className={styles.textButton} onClick={handleForgotPasswordClick}>Esqueceu a senha?</button>
                </div>
            </div>
        </div>
    );
}

export default Login;