import requests

postdata = {'key':'value'}
r = requests.post('http://www.xxxxxx.com/login', data=postdata)
print(r.content)