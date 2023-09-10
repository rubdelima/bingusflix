import React from 'react';
import './VideoInfo.css';
import Banner from "./Banner.tsx";

function VideoInfo({ movieId, onClose }) {
    return (
        <div className='video-info-overlay'>
            <div className='video-info-content'>
                {/* Conteúdo da janela, como título, descrição, vídeo, etc. */}
                <h2>Detalhes do Filme</h2>
                <p>Descrição do filme...</p>
                <Banner />
                <button onClick={onClose}>Fechar</button>
            </div>
        </div>
    );
}

export default VideoInfo;