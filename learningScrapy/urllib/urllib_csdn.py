from urllib.request import urlopen, build_opener, Request

# Add header
# Way 1 - build_opener()

url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"

headers=("User-Agent",
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5")
opener = build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()

fhandle = open("/Users/robinxyuan/Downloads/csdn_header.html", "wb")
fhandle.write(data)
fhandle.close()

# Way 2 - add_header()

req = Request(url)
req.add_header('User-Agent',
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5")
data = urlopen(req).read()