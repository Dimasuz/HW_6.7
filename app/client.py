import requests


response = requests.patch('http://127.0.0.1:5000/adv/5/',
                        json={'title': '2nfsnlkneklcnlked',
                              'descr': 'adv_1',
                              }
                        )


print(response.status_code)
print(response.json())

response = requests.get('http://127.0.0.1:5000/adv/2/')

print(response.status_code)
print(response.json())
# print(response.text)

# response = requests.delete('http://127.0.0.1:5000/adv/3/')
#
# print(response.status_code)
# print(response.json())