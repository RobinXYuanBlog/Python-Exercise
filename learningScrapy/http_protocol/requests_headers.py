import requests

r = requests.get('http://www.baidu.com')
if r.status_code == requests.codes.ok:
    print(r.status_code)
    print(r.headers)
    print(r.headers.get('content-type'))
    print(r.headers['content-type'])
else:
    r.raise_for_status()

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.baidu.com', headers=headers)
print(r.content)