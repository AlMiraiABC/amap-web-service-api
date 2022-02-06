from unittest import TestCase
import json

from gaode import GaoDe

ip = "114.247.50.2"
lat = "39.91488908"
lon = "116.40387397"
city = "110101"


class GaoDeTest(TestCase):

    def setUp(self) -> None:
        self.gaode = GaoDe()
        return super().setUp()

    def test_ip(self):
        content = self.gaode.ip(ip)
        print(content)
        self.__success(content)

    def test_regeo(self):
        content = self.gaode.regeo(lat, lon)
        print(content)
        self.__success(content)

    def test_baseWeatherInfo(self):
        content = self.gaode.baseWeatherInfo(city)
        print(content)
        self.__success(content)

    def test_allWeatherInfo(self):
        content = self.gaode.allWeatherInfo(city)
        print(content)
        self.__success(content)

    def __success(self, content):
        c = json.loads(content)
        self.assertEquals('1', c['status'])
        self.assertEquals('OK', c['info'])
        self.assertEquals('10000', c['infocode'])
