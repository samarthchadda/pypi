import requests

url="https://icanhazdadjoke.com/search"

res=requests.get(url ,
	headers={"Accept":"application/json"},
	params={"term":"cat","limit":1}
	)

# print(type(res.text))
data=res.json()
# print(type(data))
# print(data["joke"])
print(data["results"])