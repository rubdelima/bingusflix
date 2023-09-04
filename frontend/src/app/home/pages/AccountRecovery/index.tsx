import styles from "./index.module.css";
import { useNavigate } from 'react-router-dom';


function Account_recovery() {

  const navigate = useNavigate(); 

    function handleLoginClick() {
        navigate('/login'); 
    }

  return (
    <div className={styles.container}>
        <h1 className={styles.topText}>Bingusflix</h1>
        <div className={styles.centralizedBox}>
            <h2 className={styles.topBoxTest}>
            <link href="https://fonts.googleapis.com/css?family=Anonymous+Pro&display=swap" rel="stylesheet"></link>Recuperação de conta
            </h2>
            <div className="input-container"><input
                type="email"
                placeholder="exemplo@email.com"
                className={styles.emailInputField}/>
            </div>
            <div className="input-container"><input
                type="password"
                placeholder="nova senha"
                className={styles.passwordInputField}/>
            </div>
            <div className="input-container"><input
                type="password"
                placeholder="confirmar senha"
                className={styles.passwordInputField}/>
            </div>
            <button className={styles.confirmButton}>Confirmar</button>
            <div className={styles.accountRecoveryButtonsContainer}>
                <button className={styles.textButton}>Cadastre-se</button>
                <button className={styles.textButton} onClick={handleLoginClick}>Entrar</button>
            </div>
        </div>
    </div>
  );
}

export default Account_recovery;
