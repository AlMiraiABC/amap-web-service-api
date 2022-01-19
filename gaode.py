
import requests
from conf import BASE_URL, ACCESS_KEY


class GaoDe:
    """
    Amap web service APIs

    See
    ----------
    - Usage: https://lbs.amap.com/api/webservice/summary
    - ErrCode: https://lbs.amap.com/api/webservice/guide/tools/info
    """

    def __init__(self, base_url: str = BASE_URL, key=ACCESS_KEY) -> None:
        """
        Create a :class:`GaoDe` instance with specified configs.

        :param base_url: Root url for all requests, use `GaoDeConf.BASE_URL` by default.
        :param key: API access key, use `GaoDeConf.KEY` by default.
        """
        self.base_url = base_url
        self.key = key

    def __basereq(self, path: str, ps: dict) -> str:
        """
        Send a request to :param:`path` with params merged in :param:`ps`

        :param path: Relative url path of `base_url`
        :param ps: Request params, will be merged in default params

        :return: Response if status_code is `200` or else None.
        """
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
        """
        Get location from :param:`ip`

        See
        -------------
        https://lbs.amap.com/api/webservice/guide/api/ipconfig#ip
        """
        path = "/ip"
        params = {
            "ip": ip
        }
        return self.__basereq(path, params)

    def regeo(self, lat: float, lon: float):
        """
        Get location from latitude and longitude

        See
        ----------
        https://lbs.amap.com/api/webservice/guide/api/georegeo/#regeo
        """
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
