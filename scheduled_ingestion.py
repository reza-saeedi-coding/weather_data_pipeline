# ingestion_loop.py

import time
import os
from ingestion.weather_data_ingestor import fetch_weather_data
from processing.transformer import transform_weather_data
from storage.json_writer import save_to_json

API_KEY = os.getenv("API_KEY") or "e03b0727d0a90a059e78bebfdef4dbd0"

cities = ["Amsterdam", "Hamburg", "Berlin", "Prague", "Vienna", "Budapest"]

while True:
    print("⏰ Starting new hourly ingestion cycle...")
    all_weather_data = []

    for city in cities:
        print(f"📡 Fetching data for {city}...")
        raw = fetch_weather_data(city, API_KEY)
        if raw:
            transformed = transform_weather_data(city, raw)
            all_weather_data.append(transformed)
            print(f"✅ Data for {city}: {transformed}")
        else:
            print(f"❌ Failed to fetch data for {city}")

    save_to_json(all_weather_data, "data/historical_weather.json")
    print("📝 Data saved! Sleeping for 1 hour...\n")

    time.sleep(60)  # Sleep for 1 hour
