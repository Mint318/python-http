import requests


url="http://192.168.1.129:84/index.html"

r=requests.options(url)
print(r.headers)
# print(r.headers["Allow"])
# print(r.headers['Public'])
result=r.headers['Public']
if result.find("PUT") and result.find("MOVE"):
    print(result)
    print("exist iis put vul")
else:
    print("not exist")