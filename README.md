# Amap Web Service API

[![CircleCI](https://circleci.com/gh/AlMiraiABC/amap-web-service-api/tree/master.svg?style=svg)](https://circleci.com/gh/AlMiraiABC/amap-web-service-api/tree/master)
[![codecov](https://codecov.io/gh/AlMiraiABC/amap-web-service-api/branch/master/graph/badge.svg?token=N1B41OI6EX)](https://codecov.io/gh/AlMiraiABC/amap-web-service-api)

API wrapper for [amap web service](https://lbs.amap.com/api/webservice/summary)

## Supported

||api|fun|
-|-|-
||[geo](https://lbs.amap.com/api/webservice/guide/api/georegeo#geo)||
|√|[re geo](https://lbs.amap.com/api/webservice/guide/api/georegeo#regeo)|regeo|
||[direction](https://lbs.amap.com/api/webservice/guide/api/direction)||
||[direction 2.0](https://lbs.amap.com/api/webservice/guide/api/newroute)||
||[district](https://lbs.amap.com/api/webservice/guide/api/district)||
||[poi](https://lbs.amap.com/api/webservice/guide/api/search)||
||[poi 2.0](https://lbs.amap.com/api/webservice/guide/api/newpoisearch)||
||[traffic incident](https://lbs.amap.com/api/webservice/guide/api/Traffic-incident)||
|√|[ip](https://lbs.amap.com/api/webservice/guide/api/ipconfig#ip)|ip|
||[ip 2.0](https://lbs.amap.com/api/webservice/guide/api/ipconfig#t4)||
||[static map](https://lbs.amap.com/api/webservice/guide/api/staticmaps)||
||[coor convert](https://lbs.amap.com/api/webservice/guide/api/convert)||
|√|[weather](https://lbs.amap.com/api/webservice/guide/api/weatherinfo)|baseWeatherInfo, allWeatherInfo|
||[input suggests](https://lbs.amap.com/api/webservice/guide/api/inputtips)||
||[traffic status](https://lbs.amap.com/api/webservice/guide/api/trafficstatus)||
||[grasp road](https://lbs.amap.com/api/webservice/guide/api/grasproad)||

## See Also

* err code: <https://lbs.amap.com/api/webservice/guide/tools/info>
* weather code: <https://lbs.amap.com/api/webservice/guide/tools/weather-code>

## Usage

### Prepare

1. Regist an amap account.
2. Create an app in console.
3. Add a key and select `Web Service`.
4. Copy created key.
5. Clone this repository.
6. Create file named `.env` and input below:

    ```env
    AMAP_WS_ACCESS_KEY=<copied key>
    ```

7. Install [docker desktop](https://www.docker.com/products/docker-desktop)([wsl2](https://docs.microsoft.com/windows/wsl/) is recommended).

### Run

1. Open this repository in vscode.
2. Install extension `ms-vscode-remote.remote-containers`
3. Open remote window and select `Reopen in Container`
