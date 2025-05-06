import requests
def fetch_weather_data(city_name: str, api_key: str) -> dict:
     url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
     try:
          response = requests.get(url)
          response.raise_for_status()
          return response.json()
     except requests.RequestException as e:
           print(f"Error fetching data: {e}")
           return