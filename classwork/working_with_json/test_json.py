import json

import requests

KEY = "ZQ48KUlOHW4H7bnsvgNlF02Z06kwKvo"
url = f"https://api.tomorrow.io/v4/weather/forecast?location=newyork&apikey{KEY}"

headers = {"accept": "aplication/json"}

response = requests.get(url, header=headers)

print(resp.text)
