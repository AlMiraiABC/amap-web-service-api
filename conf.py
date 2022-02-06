# access key created at https://console.amap.com/dev/key/app
import os


ACCESS_KEY = os.getenv('AMAP_WS_ACCESS_KEY', '')

# root url for all request url
BASE_URL = "https://restapi.amap.com/v3"
