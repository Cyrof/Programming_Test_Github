import requests

proxies = {'https':'47.254.75.151:8181' , 'http':'47.254.75.151:8181'}

url = 'https://www.whatismyip.com/'

resp=requests.get(url, proxies=proxies)

print(resp.json)
print(resp.text)