import requests

url ="https://httpbin.org/get"
r=requests.get(url)
print(r.status_code)
