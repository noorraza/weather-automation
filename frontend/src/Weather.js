import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Weather.css';

const Weather = () => {
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // This effect will run once when the component is first rendered.
    const fetchWeather = async () => {
      try {
        // Make GET request to the Flask API
        const response = await axios.get('http://127.0.0.1:5000/weather');
        setWeather(response.data);  // Store the weather data
        setLoading(false);           // Set loading to false once data is fetched
      } catch (error) {
        setError('Error fetching weather data.');
        setLoading(false);           // Set loading to false if there's an error
      }
    };

    fetchWeather();  // Call the function to fetch data
  }, []);  // Empty dependency array means this effect runs once, when the component mounts.

  // Render UI based on loading, error, and weather states
  if (loading) {
    return <div>Loading...</div>;  // Show loading message while data is being fetched
  }

  if (error) {
    return <div>{error}</div>;  // Show error message if data fetch fails
  }

  // If weather data is available, render it
  return (
    <div className="weather-container">
      <h1>Weather in {weather.city}</h1>
      <p>Description: {weather.description}</p>
      <p>Temperature: {weather.temperature}°C</p>
      <p>Feels Like: {weather.feels_like}°C</p>
      <p>Humidity: {weather.humidity}%</p>
      <p>Wind Speed: {weather.wind_speed} m/s</p>
      <p>Pressure: {weather.pressure} hPa</p>
    </div>
  );
};

export default Weather;
