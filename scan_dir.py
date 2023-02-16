import requests
import  sys

url=sys.argv[1]
# dic  = sys.argv[2]

# url="http:/127.0.0.1/dvwa/"
with open("dir.txt","r") as f:
    for line in f.readlines():
        line=line.strip()
        r=requests.get(url+line)
        if r.status_code==200:
            print("url:"+r.url+" exist")