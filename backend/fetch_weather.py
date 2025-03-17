import requests

API_KEY = "79ff95a0f0222d6aa309b8876233a6f9"
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
