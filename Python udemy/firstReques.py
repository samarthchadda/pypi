import requests

url="https://www.google.com/"
res=requests.get(url)

print(f"Your request to {url} came back with status code {res.status_code}")

# print(res.texts)