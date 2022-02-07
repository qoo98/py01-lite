import sys
import requests

url = sys.argv[1]
res = requests.get(url)
if res.status_code != 200:
    print(res.status_code)
else:
    print(res.text.count(sys.argv[2]))
    
