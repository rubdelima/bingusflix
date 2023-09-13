import Navbar from '../../components/Navbar';
import ImageCarousel from '../../components/ImageCarousel';
import { fetchToken } from '../../components/auth';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';


const Home = () => {

  const navigate = useNavigate();

    useEffect(() => {
      if (fetchToken()) {
        navigate('/home-page');
      }
    }, []);

  return (
    <>
    <Navbar navTitle={"BINGUSFLIX"}></Navbar>
    <ImageCarousel/>
    </>
  );

};

export default Home;