import requests

res = requests.get("http://192.168.32.114:3000/api/main")
print(res.json())

