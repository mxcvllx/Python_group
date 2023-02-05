import json

import requests

KEY = "R7PdST1zLADXga7Cx1xR3Sqn2gmPvSpl"
url = f"https://api.freecurrencyapi.com/v1/latest?apikey=YOUR-APIKEY{KEY}"

resp = requests.get(url)


with open('weather.json', 'w') as f:
    json.dump(json.loads(resp.text), f)
