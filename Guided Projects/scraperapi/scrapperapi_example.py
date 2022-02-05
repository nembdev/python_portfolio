import requests
from urllib.parse import urlencode
import config  # api_key


# r = requests.get("http://api.scraperapi.com", params=payload)


payload = {
    "api_key": config.api_key,
    "url": "https://www.g2.com/",
    "render": "true",
}

r = requests.get("http://api.scraperapi.com", params=urlencode(payload))

print(r.text)
