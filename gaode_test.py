from hashlib import new
from unittest import TestCase
import json

from gaode import GaoDe

ip="114.247.50.2"
lat = "39.91488908"
lon = "116.40387397"
city = "110101"

class GaoDeTest(TestCase):

    def setUp(self) -> None:
        self.gaode = GaoDe()
        self.content = ''
        return super().setUp()

    def tearDown(self) -> None:
        self.assertEquals(0, json.loads(self.content)['code'])
        return super().tearDown()

    def test_ip(self):
        content =  self.gaode.ip(ip)
        print(content)
    
    def test_regeo(self):
        content = self.gaode.regeo(lat,lon)
        print(content)
    
    def test_baseWeatherInfo(self):
        content = self.gaode.baseWeatherInfo(city)
        print(content)