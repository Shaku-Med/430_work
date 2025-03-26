import os
from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import pytz

# This is for securing our API key.
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# API_KEY = "" 
# For security reasons, I've prevented the .env key or file from being in the code. Done by [Mohamed Amara]
API_KEY = os.getenv("API_KEY")

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        weather_response = requests.get(base_url, params=params)
        forecast_response = requests.get(forecast_url, params=params)
        
        weather_response.raise_for_status()
        forecast_response.raise_for_status()
        
        weather_data = weather_response.json()
        forecast_data = forecast_response.json()

        # Get timezone and current time
        timezone_offset = weather_data.get("timezone", 0)
        city_time = datetime.utcfromtimestamp(weather_data["dt"] + timezone_offset)
        formatted_time = city_time.strftime("%Y-%m-%d %H:%M:%S")

        return {
            "weather": weather_data,
            "forecast": forecast_data["list"][:5],
            "time": formatted_time
        }
    except requests.exceptions.RequestException:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather(city)
    return render_template("index.html", data=weather_data)

@app.route("/api/weather", methods=["GET"])
def api_weather():
    city = request.args.get("city")
    if city:
        weather_data = get_weather(city)
        if weather_data:
            return jsonify(weather_data)
        return jsonify({"error": "Could not fetch weather data"}), 400
    return jsonify({"error": "City not provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
