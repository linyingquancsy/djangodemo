import requests

res = requests.post('http://127.0.0.1:8000', data={'speak': "5"})
print(res.text)
