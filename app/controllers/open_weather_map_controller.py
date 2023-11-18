import json

from app.gatways.services.open_weather_map import OpenWeatherMapGateway


class OpenWeatherMapController:

    def __init__(self):
        self.open_weather_map_gateway = OpenWeatherMapGateway()

    def read(self, city: str) -> json:
        result = self.open_weather_map_gateway.get_weather_by_city(city)
        return result
