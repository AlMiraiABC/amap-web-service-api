
import requests
import json
from conf import GaoDeConf


class GaoDe:
    def __init__(self, base_url: str = GaoDeConf["BASE_URL"], key=GaoDeConf["KEY"]) -> None:
        self.base_url = base_url
        self.key = key

    def __basereq(self, path: str, ps: dict) -> str:
        url = self.base_url+path
        params = {
            "key": self.key
        }
        params.update(ps)
        response = requests.get(
            url=url, params=params,
            verify=False
        )
        if response.status_code == 200:
            return response.text

    def ip(self, ip: str):
        path = "/ip"
        params = {
            "ip": ip
        }
        return self.__basereq(path, params)

    def regeo(self, lat: float, lon: float):
        path = "/geocode/regeo"
        params = {
            "output": "json",
            "location": f"{lon},{lat}"
        }
        return self.__basereq(path, params)

    def baseWeatherInfo(self, city: str) -> str:
        return self.__weather(city, 'base')

    def allWeatherInfo(self, city: str) -> str:
        return self.__weather(city, 'all')

    def __weather(self, city: str, ext: str):
        path = "/weather/weatherInfo"
        params = {
            "city": city,
            "extensions": ext,
            "output": "JSON"
        }
        return self.__basereq(path, params)
