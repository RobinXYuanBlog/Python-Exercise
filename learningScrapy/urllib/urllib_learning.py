from urllib.request import Request, urlopen, urlretrieve, urlcleanup
from urllib import *
from urllib.request import HTTPError

response = urlopen('http://www.baidu.com')
# data = response.read()
# dataline = response.readline()
# print(data)
# print(response.read().decode('utf-8'))

# Way I
# fhandle = open("/Users/robinxyuan/Downloads/baidu.html", "wb")
# fhandle.write(data)
# fhandle.close()

# Way II
# filename = urlretrieve("http://edu.51cto.com", filename="/Users/robinxyuan/Downloads/51cto.html")
# urlcleanup()

# web page info
info = response.info()
print(info)

# status code
code = response.getcode()
print(code)

# url
url = response.geturl()
print(url)

