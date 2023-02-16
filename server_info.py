import requests


# url="http://192.168.1.129:84/index.html"
url="http://192.168.1.129:90/"
r=requests.get(url)
print(r.headers)
# print("服务器中间件为："+r.headers['Server'])
# print("服务器脚本语言为："+r.headers['X-Powered-By'])
print("服务器中间件为："+r.headers['Server'])