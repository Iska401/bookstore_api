import requests


url = 'http://127.0.0.1:5000/catalog'

response = requests.post(url, json=[{'title': 'rich father, poor father', 'img_path': 'gay/erik', 'price': 123, 'amount': 52}])
print(response.json())

print(requests.get(url).json())