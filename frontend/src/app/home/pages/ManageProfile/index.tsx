import styles from "./index.module.css"
import { useState, useEffect } from "react"
import { useNavigate } from 'react-router-dom';
import axios from 'axios'


function ManageProfile() {

    const navigate = useNavigate();

    const [nickname, setNickname] = useState("");
    const [age, setAge] = useState("");
    const [language, setLanguage] = useState("");
    const [error_message, setErrorMessage] = useState("");
    const [success_message, setSuccessMessage] = useState("");

    async function handleSubmit(event) {
        event.preventDefault();

        const token = localStorage.getItem('token');
        const config = {headers: {Authorization: `Bearer ${token}`}};

        try {
            const get_response = await axios.get(`http://127.0.0.1:4000/users/${Number(token)}`);
            
            const response = await axios.put(`http://127.0.0.1:8000/profiles/${get_response.data.active_profile}`, {
                nickname: nickname,
                pg: age,
                language: language
            }, config);

            console.log(response.status);
            setErrorMessage("");
            setSuccessMessage("Perfil alterado com sucesso!");
        } catch (error) {
            console.error(error);
            setErrorMessage("Não foi possível alterar seu perfil");
        }
    }

    const handleTitleClick = () => {
        navigate('/home-page');
    }

    return (
        <div className={styles.container}>
            <h1 className={styles.topText}
            onClick={() => handleTitleClick()}>BingusFlix</h1>

            <div className={styles.centralizedBox}>
                <h2 className={styles.topBoxText}>Gerenciar Perfis</h2>

                <div className={styles.formContainer}>
                    <form onSubmit={handleSubmit} className={styles.formRow}>
                        <img className={styles.formImg} src="/imgs/profile.jpeg" alt="profile image"/>

                        <div className={styles.inputBoxes}>
                            <input className={styles.formInputName} type="text"
                            placeholder="Digite o nome do perfil"
                            value = {nickname}
                            onChange = {(e) => setNickname(e.target.value)}
                            required/>

                            <input className={styles.formInputAge} type="text" 
                            placeholder="Digite a idade do perfil"
                            value = {age}
                            onChange = {(e) => setAge(e.target.value)}
                            required/>

                            <input className={styles.formInputLanguage} type="text" 
                            placeholder="Digite a lingua do perfil"
                            value = {language}
                            onChange = {(e) => setLanguage(e.target.value)}
                            required/>

                            {error_message && <p className={styles.errorMessage}>{error_message}</p>}
                            {success_message && <p className={styles.success}>{success_message}</p>}

                            <button 
                            type="submit" 
                            className={styles.confirmButton}>
                                Atualizar
                            </button>

                        </div>

                    </form>
                </div>


            </div>
        </div>
    )
}

export default ManageProfile