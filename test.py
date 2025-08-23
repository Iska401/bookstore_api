import requests


url = 'http://127.0.0.1:5000/'
response = requests.post(url + 'register', json={'username': 'Iskander_2013',
                                    'password': 'jork7447'})
# response = requests.post(url, json={'title': 'иска',
#                                     'description': 'about the richest and smartest person ever',
#                                     'price': 21})

# response = requests.post(url + 'login', json={'username': 'Iskander_2011',
#                                             'password': 'jork7447'})

print(response.json())


print(requests.get(url))