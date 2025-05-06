import time
from ingestion.weather_data_ingestor import fetch_weather_data
from processing.transformer import transform_weather_data
from storage.json_writer import save_to_json
API_KEY = "e03b0727d0a90a059e78bebfdef4dbd0"

cities = [
    "Amsterdam",
    "Hamburg",
    "Berlin",
    "Prague",
    "Vienna",
    "Budapest"
]
while True:
    print("New Data Collection....")
    all_weather_data =[]
    for city in cities:
        print(f"Fetching data for {city}....")
        raw = fetch_weather_data(city, API_KEY)
        transformed = transform_weather_data(city, raw)
        print(transformed)
        all_weather_data.append(transformed)
        save_to_json(all_weather_data, "data/historical_weather.json")
        print("Saved data to historical_weather.json DONE!!!")
    time.sleep(3600)
