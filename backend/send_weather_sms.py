import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch API keys & Twilio credentials
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECEIVER_PHONE_NUMBER = os.getenv("RECEIVER_PHONE_NUMBER")

# OpenWeatherMap API URL
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Function to fetch weather
def get_weather():
    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        weather_summary = f"🌤️ Good evening Cutu! Today's weather in {CITY}: {temp}°C, {description}."
        return weather_summary
    else:
        return "⚠️ Error fetching weather data."

# Function to send SMS
def send_sms():
    weather_message = get_weather()

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=weather_message,
        from_=TWILIO_PHONE_NUMBER,
        to=RECEIVER_PHONE_NUMBER
    )

    print(f"✅ SMS Sent! SID: {message.sid}")

# Run the function
send_sms()
