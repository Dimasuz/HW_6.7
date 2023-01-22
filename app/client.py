import requests
from config import API_URL

# respones = requests.post(API_URL, )

respones = requests.get(API_URL)

print(respones.text)
