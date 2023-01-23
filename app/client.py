import requests
from config import API_URL


response = requests.post('http://127.0.0.1:5000/adv/',
                        json={'title': '1th',
                              'descr': 'advertisements_1',
                              'user_id': '1',}
                        )


print(response.status_code)
print(response.json())

# response = requests.get('http://127.0.0.1:5000/users/2/')
#
# print(response.status_code)
# print(response.json())
