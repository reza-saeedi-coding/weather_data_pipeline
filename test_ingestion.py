from datetime import datetime
from storage.json_writer import save_to_json
from processing.transformer import transform_weather_data
import requests
from ingestion.weather_data_ingestor import fetch_weather_data
API_KEY = "e03b0727d0a90a059e78bebfdef4dbd0"
cities = ["Amsterdam", "Hamburg", "Berlin", "Prague", "Vienna", "Budapest"]
all_weather_data = []
for city in cities:
    print(f"Getting weather data for {city}...")
    data = fetch_weather_data(city, API_KEY)
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    transformed = transform_weather_data(city,data)
    all_weather_data.append(transformed)
    save_to_json(all_weather_data, "data/weather_data.json")
    print(transformed)