import { Box } from "@mui/material";
import React, { useState, useEffect } from "react"
import styles from "./index.module.css"

const ImageCarousel = () => {
  const [imageIndex, setImageIndex] = useState(0);
  const imagesUrl = [
    'https://image.tmdb.org/t/p/original/rLb2cwF3Pazuxaj0sRXQ037tGI1.jpg',
    'https://image.tmdb.org/t/p/original/2Cpg8hUn60PK9CW9d5SWf605Ah8.jpg',
    'https://image.tmdb.org/t/p/original/rRcNmiH55Tz0ugUsDUGmj8Bsa4V.jpg',
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      // Increment the imageIndex, or reset it to 0 if it exceeds the number of images
      setImageIndex((prevIndex) => (prevIndex + 1) % imagesUrl.length);
    }, 2000); // Change image every 1000 milliseconds (1 second)

    return () => clearInterval(interval); // Cleanup the interval on component unmount
  }, [imagesUrl]);

  return (
    <Box>
      <img
        src={imagesUrl[imageIndex]}
        alt={`Image ${imageIndex + 1}`}
        style={{ maxWidth: '100%' }}
      />
    </Box>
  );
};

export default ImageCarousel;
