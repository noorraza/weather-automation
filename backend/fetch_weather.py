from flask import Flask, jsonify
import requests
from dotenv import load_dotenv
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Ottawa"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city, api_key):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Change to 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

if __name__ == "__main__":
    weather_data = get_weather(CITY, API_KEY)
    print(weather_data)
