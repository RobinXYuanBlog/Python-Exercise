from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = "http://www.iqianyue.com/mypost/"
# after urlencode, set encoding method is UTF-8
post_data = urlencode({
    "name": "ceo@iqianyue.com",
    "pass": "aA123456"
}).encode('utf-8')

req = Request(url, post_data)
req.add_header('User-Agent',
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5")

data = urlopen(req).read()

fhandle = open("/Users/robinxyuan/Downloads/form_post.html", "wb")
fhandle.write(data)
fhandle.close()