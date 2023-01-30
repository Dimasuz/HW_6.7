import requests

# response = requests.post('http://127.0.0.1:5000/users/',
#                         json={'name': 'user_8',
#                               'email': 'user_8@em.em',
#                               'password': '123',
#                               }
#                         )
#
#
# print(response.status_code)
# # print(response.json())
# print(response.text)

response = requests.get(f'http://127.0.0.1:5000/users/2/')

print(response.status_code)
print(response.text)

response = requests.post('http://127.0.0.1:5000/adv/',
                        json={'title': 'title_1',
                              'descr': 'descr_1',
                              'user_id': 2,
                              'password': '321',
                              }
                        )


print(response.status_code)
print(response.json())
print(response.text)

response = requests.patch('http://127.0.0.1:5000/adv/1/',
                        json={'descr': 'descr_1_patch1',
                              'user_id': 2,
                              'password': '321',
                              }
                        )


print(response.status_code)
print(response.json())
print(response.text)


response = requests.delete('http://127.0.0.1:5000/users/1/',
                        json={'user_id': 1,
                              'password': '123',
                              }
                        )

print(response.status_code)
print(response.json())

#
# response = requests.delete('http://127.0.0.1:5000/users/2/')
#
# print(response.status_code)
# print(response.text)


# response = requests.get('http://127.0.0.1:5000/user/')
#
# print(response.status_code)
# print(response.text)