import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { fetchToken } from '../../components/auth';
import styles from './index.module.css'; // Adjust the import path based on your project structure

const API_URL = 'http://127.0.0.1:8000'; // Define your API URL

function AccountRecovery() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  useEffect(() => {
    if (fetchToken()) {
      navigate('/home-page');
    }
  }, [navigate]);

  const handleRegisterClick = () => {
    navigate('/users');
  };

  const handleLoginClick = () => {
    navigate('/login');
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (newPassword !== confirmPassword) {
    setErrorMessage("As senha não coincidem");
      setSuccessMessage('');
      return;
    }

    try {
      const response = await axios.put(`${API_URL}/account_recovery`, {
        email,
        new_password: newPassword,
        confirm_password: confirmPassword,
      });

      console.log(response.status);
      setSuccessMessage('Sua senha foi alterada com sucesso!');
      setErrorMessage('');
    } catch (error) {
      console.error(error);
      setErrorMessage('Não foi possível alterar sua senha');
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.topText}>Bingusflix</h1>
      <div className={styles.centralizedBox}>
        <h2 className={styles.topBoxTest}>Recuperação de conta</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-container">
            <input
              data-cy="email"
              type="email"
              placeholder="exemplo@email.com"
              className={styles.emailInputField}
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="input-container">
            <input
              data-cy="nova-senha"
              type="password"
              placeholder="nova senha"
              className={styles.passwordInputField}
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
              required
            />
          </div>
          <div className="input-container">
            <input
              data-cy="confirmar-senha"
              type="password"
              placeholder="confirmar senha"
              className={styles.passwordInputField}
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </div>
          {errorMessage && (
            <p data-cy="error-message" className={styles.error}>
              {errorMessage}
            </p>
          )}
          {successMessage && (
            <p data-cy="success-message" className={styles.success}>
              {successMessage}
            </p>
          )}
          <button data-cy="Confirmar" type="submit" className={styles.confirmButton}>
            Confirmar
          </button>
        </form>
        <div className={styles.accountRecoveryButtonsContainer}>
          <button className={styles.textButton} onClick={handleRegisterClick}>
            Cadastre-se
          </button>
          <button className={styles.textButton} onClick={handleLoginClick}>
            Entrar
          </button>
        </div>
      </div>
    </div>
  );
}

export default AccountRecovery;
