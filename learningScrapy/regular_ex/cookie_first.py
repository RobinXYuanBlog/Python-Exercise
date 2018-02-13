import urllib.request
import urllib.parse
import http.cookiejar

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q"
postdata = urllib.parse.urlencode({
    "username": "weisuen",
    "password": "aA123456"
}).encode('utf-8')

req = urllib.request.Request(url, postdata)

req.add_header('User-Agent',
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5")
cjar = http.cookiejar.CookieJar()

opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(cjar)
)

urllib.request.install_opener(opener)

file = opener.open(req)
data = file.read()

file = open("/Users/robinxyuan/Downloads/cookie.html", "wb")
file.write(data)
file.close()

url2 = "http://bbs.chinaunix.net/"
data2 = urllib.request.urlopen(url2).read()
fhandle = open("/Users/robinxyuan/Downloads/chinaunix.html", "wb")
fhandle.write(data2)
fhandle.close()