import requests

url="https://www.baidu.com"

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

r=requests.get(url,headers=headers)

print(r.request.headers)

