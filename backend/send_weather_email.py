import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import schedule
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch values from .env
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# OpenWeatherMap API URL
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}"

# Function to get weather data
def get_weather_data():
    response = requests.get(URL)
    data = response.json()

    # Get today's hourly forecast (first 8 data points = next 24 hours)
    hourly_forecast = data['list'][:8]

    today_summary = f"Today's weather in {CITY}:\n"
    for forecast in hourly_forecast:
        time = forecast['dt_txt']
        temp = forecast['main']['temp'] - 273.15  # Convert Kelvin to Celsius
        description = forecast['weather'][0]['description']
        today_summary += f"{time}: {temp:.2f}°C, {description}\n"

    # Tomorrow's forecast
    tomorrow_summary = f"\nTomorrow's forecast:\n"
    tomorrow_data = data['list'][8:16]  # Next day's 8 hourly forecasts
    for forecast in tomorrow_data:
        time = forecast['dt_txt']
        temp = forecast['main']['temp'] - 273.15
        description = forecast['weather'][0]['description']
        tomorrow_summary += f"{time}: {temp:.2f}°C, {description}\n"

    return today_summary + tomorrow_summary

# Function to send email
def send_email():
    weather_info = get_weather_data()

    # Email setup
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = "Your Daily Weather Update Cutu"
    msg.attach(MIMEText(weather_info, 'plain'))

    # Send email securely
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

# Schedule the email every morning at 7 AM
schedule.every().day.at("19:25").do(send_email)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)
