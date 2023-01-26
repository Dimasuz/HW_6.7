import requests

# response = requests.post('http://127.0.0.1:5000/users/',
#                         json={'name': 'user_2',
#                               'email': 'user_2@em.em',
#                               'password': '321',
#                               }
#                         )
#
#
# print(response.status_code)
# print(response.json())
# print(response.text)
#
# response = requests.post('http://127.0.0.1:5000/adv/',
#                         json={'title': 'title_1',
#                               'descr': 'descr_1',
#                               'user_id': 1,
#                               'password': '123',
#                               }
#                         )
#
#
# print(response.status_code)
# print(response.json())
# print(response.text)

# response = requests.patch('http://127.0.0.1:5000/adv/2/',
#                         json={'descr': 'descr_2_patch2',
#                               'user_id': 1,
#                               'password': '321',
#                               }
#                         )
#
#
# print(response.status_code)
# print(response.json())
# print(response.text)


response = requests.delete('http://127.0.0.1:5000/user/1/',
                        json={'user_id': 2,
                              'password': '321',
                              }
                        )

print(response.status_code)
print(response.json())

response = requests.get('http://127.0.0.1:5000/user/1/')

print(response.status_code)
print(response.json())