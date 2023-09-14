import styles from "./index.module.css"
import { useState, useEffect } from "react"
import { useNavigate } from 'react-router-dom';
import axios from 'axios';


function Profiles() {
    const navigate = useNavigate();
    const [profileList, setProfileList] = useState([]);

    const getUserProfiles = async () => {
        const token = localStorage.getItem('token');
        const config = {headers: {Authorization: `Bearer ${token}`}};

        try {
            const response = await axios.get('http://localhost:8000/profiles', config);
            
            setProfileList(response.data.profiles);
        } catch(e) {
            console.log('erro:', e);
        }
    };

    useEffect(() => {
        getUserProfiles();

    }, []);

    const handleProfileClick = async (profile) => {
        const id = profileList[0].id_user

        let get_response = await axios.get(`http://localhost:4000/users/${id}`);
    
        get_response.data.active_profile = profile.id_profile

        const put_response = await axios.put(`http://localhost:8000/users/${id}`, get_response.data)

        navigate('/home-page');
    };

    const handleManage = () => {
        navigate('/manage_profile');
    }

    const handleTitleClick = () => {
        navigate('/home-page');
    }


    return (
        <div className={styles.container}>
            <h1 className={styles.topText}
            onClick={() => handleTitleClick()}>BingusFlix</h1>

            <div className={styles.centralizedBox}>
                <h2 className={styles.topBoxText}>Profiles</h2>

                <div className={styles.profileSection}>
                    {profileList?.map((profile) => {
                        return (
                            <div className={styles.profile} 
                            key={profile.id_profile}
                            onClick={() => handleProfileClick(profile)}>
                                <img src="/imgs/profile.jpeg" 
                                alt="profile image"/>
                                <div className={styles.profileName}>{profile.nickname}
                                </div>
                            </div>
                    )})}
                </div>

                <div className={styles.bottomPage}>
                    <div className={styles.bottomLeftText}>Plano <span className={styles.bottomLeftTextColored}>Comum</span></div>
                    <button className={styles.manageButton}
                    onClick={handleManage}>Gerenciar</button>
                </div>
            </div>
        </div>
    )
}

export default Profiles