from flask import Flask, jsonify
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Ottawa"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city, api_key):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

@app.route("/weather", methods=["GET"])
def weather():
    weather_data = get_weather(CITY, API_KEY)
    
    # We can format the data to return only useful details
    formatted_data = {
        "city": weather_data.get("name"),
        "description": weather_data["weather"][0]["description"],
        "temperature": weather_data["main"]["temp"],
        "feels_like": weather_data["main"]["feels_like"],
        "humidity": weather_data["main"]["humidity"],
        "wind_speed": weather_data["wind"]["speed"],
        "pressure": weather_data["main"]["pressure"],
    }
    
    return jsonify(formatted_data)

if __name__ == "__main__":
    app.run(debug=True)
