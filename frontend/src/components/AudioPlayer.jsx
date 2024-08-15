import React from 'react';

const AudioPlayer = ({ videoId }) => {
  return (
    <div className="w-full flex justify-center items-center">
      <iframe
        width="300"
        height="150"
        src={`https://www.youtube.com/embed/${videoId}?autoplay=0`}
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
        title="YouTube Audio Player"
      ></iframe>
    </div>
  );
};

export default AudioPlayer;