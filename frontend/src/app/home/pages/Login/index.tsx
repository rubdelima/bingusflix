import styles from "./index.module.css";
import { useNavigate } from 'react-router-dom';
  
  
function Login() {

    const navigate = useNavigate(); 

    function handleForgotPasswordClick() {
        navigate('/account_recovery'); 
    }


  return (
    <div className={styles.container}>
        <h1 className={styles.topText}>Bingusflix</h1>
        <div className={styles.centralizedBox}>
            <h2 className={styles.topBoxTest}>
                <link href="https://fonts.googleapis.com/css?family=Anonymous+Pro&display=swap" rel="stylesheet"></link>Login
            </h2>
            <div className="input-container"><input
                type="email"
                placeholder="exemplo@email.com"
                className={styles.emailInputField}/>
            </div>
            <div className="input-container"><input
                type="password"
                placeholder="senha"
                className={styles.passwordInputField}/>
            </div>
            <button className={styles.loginButton}>Entrar</button>
            <div className={styles.loginButtonsContainer}>
                <button className={styles.textButton}>Cadastre-se</button>
                <button className={styles.textButton} onClick={handleForgotPasswordClick}>Esqueceu a senha?</button>
            </div>
        </div>
    </div>
  );
}

export default Login;
