import requests

url="https://icanhazdadjoke.com/"

res=requests.get(url ,headers={"Accept":"application/json"})

# print(type(res.text))
data=res.json()
print(type(data))
print(data["joke"])