# Weather Automation Project

This project automates the process of sending daily weather updates via **SMS** and **email** using the **OpenWeatherMap API** and **Twilio API**. Every morning at 7:00 AM, you receive a text message and an email with the current weather forecast for the day, along with a brief summary for the next day.

## Project Overview

The project consists of:
- **Python backend**: Fetches weather data from OpenWeatherMap, processes it, and sends notifications.
- **Twilio API**: Sends **SMS notifications** to your phone.
- **Email Notifications**: Sends weather updates directly to your email.
- **GitHub**: Used for version control and collaboration.

## Key Features
- Fetches weather data from **OpenWeatherMap API**.
- Sends **SMS notifications** via **Twilio** every morning at a scheduled time.
- Sends **email notifications** with the weather summary.
- **Environment variables** securely manage sensitive information like API keys and credentials.

## Tech Stack
- Python
- OpenWeatherMap API
- Twilio API
- SMTP (for email notifications)
- GitHub (version control)

## Setup and Usage
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/weather-automation.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your environment variables for OpenWeatherMap, Twilio, and email credentials (use `.env` or another secure method).
4. Run the Python script to start fetching weather data and sending notifications.

## Conclusion

This project demonstrates how to combine Python, external APIs, and automation to streamline your daily routine with both SMS and email notifications.

---

**Note**: Make sure to keep your API keys and credentials secure and avoid pushing them to public repositories.

