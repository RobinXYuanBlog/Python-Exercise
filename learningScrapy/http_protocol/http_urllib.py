from urllib.request import urlopen, Request
from urllib.parse import urlencode

# response = urlopen('http://www.zhihu.com')
# html = response.read()
# print(html)

# Could also be separated into 2 steps

# request = Request('http://www.zhihu.com')
# response = urlopen(request)
# html = response.read()
# print(html)

# POST

# url = 'http://www.xxxxxx.com/login'
# postdata = {
#     'username': 'qiye',
#     'password': 'qiye_pass'
# }
#
# data = urlencode(postdata).encode('utf-8')
# req = Request(url, data)
# response = urlopen(req)
# html = response.read()

# Add headers

url = 'http://www.xxxxxx.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer = 'http://www.xxxxxx.com/'
postdata = {
    'username': 'qiye',
    'password': 'qiye_pass'
}

# Add user_agent, referer to headers
headers = {'User-Agent':user_agent, 'Referer':referer}
data = urlencode(postdata).encode('utf-8')
req = Request(url, data, headers)
response = urlopen(req)
html = response.read()


