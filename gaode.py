
from email.mime import base
from typing import Dict
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
        }.update(ps)
        response = requests.get(
            url=url, params=params,
            verify=False
        )
        if response.status_code == 200:
            return response.content

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
            "location": f"{lat},{lon}"
        }
        content = self.__basereq(path, params)
        resp = json.loads(content)
        # print(type(resp))
        result = resp["regeocode"]["addressComponent"]
        dic = {}
        dic["country"] = result["country"]
        dic["province"] = result["province"]
        dic["city"] = result["city"]
        dic["citycode"] = result["citycode"]
        dic["district"] = result["district"]
        dic["adcode"] = result["adcode"]
        dic["township"] = result["township"]
        dic["towncode"] = result["towncode"]
        return json.dumps(dic)

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
