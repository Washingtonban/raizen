import os
import requests


class OpenWeatherMapGateway:

    def __init__(self):
        self.api_key = os.getenv('OPEN_WEATHER_MAP_API_KEY')
        self.base_url = os.getenv('OPEN_WEATHER_MAP_BASE_URL')

    def get_weather_by_city(self, city_name, units="metric"):
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": units
        }
        response = requests.get(self.base_url, params=params)
        return response.json()
