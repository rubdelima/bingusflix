import styles from "./index.module.css";
import { useState } from "react";
import { useNavigate } from 'react-router-dom';

function Account_recovery() {

  const navigate = useNavigate(); 
  const [email, setEmail] = useState("");
  const [new_password, setNewPassword] = useState("");
  const [confirm_password, setConfirmPassword] = useState("");
  const [error_message, setErrorMessage] = useState("");
  const [success_message, setSuccessMessage] = useState("");

    function handleLoginClick() {
        navigate('/login'); 
    }

    function handleSubmit(event) {
        event.preventDefault();

        if (new_password != confirm_password) {
            setErrorMessage("As senhas não coincidem");
            setSuccessMessage("");
            return;
        }
        else {
            setSuccessMessage("Sua senha foi alterada com sucesso!");
            setErrorMessage("");
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
                <button className={styles.textButton}>Cadastre-se</button>
                <button className={styles.textButton} onClick={handleLoginClick}>Entrar</button>
            </div>
        </div>
    </div>
  );
}

export default Account_recovery;
