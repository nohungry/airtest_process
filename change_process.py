import requests
import json

session = requests.session()

url = "http://egame.uat.kk168-01.com/api/v2/auth/login"

header = {
            # 'X-Requested-With': "XMLHttpRequest",
            # 'Accept': 'application/json, text/javascript, */*; q=0.01',
            "content-type": 'application/json; charset=utf-8',
            'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }

payload = {
    "username": "norman001",
    "password": "000000"
}
r = session.request("POST", url=url, headers=header, data=json.dumps(payload))

pass