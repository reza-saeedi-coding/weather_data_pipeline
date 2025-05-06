from datetime import datetime
def transform_weather_data(city: str, raw_data: dict) -> dict:
    return {
        "city": city,
        "temperature_c": raw_data["main"]["temp"],
        "humidity_percent": raw_data["main"]["humidity"],
        "weather_description": raw_data["weather"][0]["description"],
        "timestamp": datetime.utcnow().isoformat()
    }
