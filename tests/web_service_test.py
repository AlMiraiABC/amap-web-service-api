from unittest import TestCase
import json

from amap_api.web_service import WebService

ip = "114.247.50.2"
lat = "39.91488908"
lon = "116.40387397"
city = "110101"


class WebServiceTest(TestCase):

    def setUp(self) -> None:
        self.ws = WebService()
        return super().setUp()

    def test_ip(self):
        content = self.ws.ip(ip)
        print(content)
        self.__success(content)

    def test_regeo(self):
        content = self.ws.regeo(lat, lon)
        print(content)
        self.__success(content)

    def test_weather_actual(self):
        content = self.ws.weather_actual(city)
        print(content)
        self.__success(content)

    def test_weather_forecast(self):
        content = self.ws.weather_forecast(city)
        print(content)
        self.__success(content)

    def __success(self, content):
        c = json.loads(content)
        self.assertEquals('1', c['status'])
        self.assertEquals('OK', c['info'])
        self.assertEquals('10000', c['infocode'])
