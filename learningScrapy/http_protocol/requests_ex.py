import requests

payload = {'Keywords':'blog.qiyeboy', 'pageindex':1}
r = requests.get('http://zzl.cnblogs.com/s/blogpost', params=payload)
print(r.url)