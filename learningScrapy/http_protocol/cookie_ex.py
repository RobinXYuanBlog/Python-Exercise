from urllib.request import urlopen, build_opener, HTTPCookieProcessor, Request
from http.cookiejar import CookieJar

# cookie = CookieJar()
# opener = build_opener(HTTPCookieProcessor(cookie))
# response = opener.open('http://www.zhihu.com')
# for item in cookie:
#     print(item.name + ':' + item.value)


# Self add cookie

opener = build_opener()
opener.addheaders.append(('Cookie', 'email=' + "xxxxxx@163.com"))
req = Request("http://www.zhihu.com")
response = opener.open(req)
print(response.headers)
retdata = response.read()

