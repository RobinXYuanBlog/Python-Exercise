import re
from urllib.request import build_opener, install_opener, urlopen

def get_link(url):
    headers = ("User-Agent",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5")
    opener = build_opener()
    opener.addheaders = [headers]
    install_opener(opener)
    file = urlopen(url)
    data = str(file.read())
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    link = list(set(link))
    return link

url = "http://blog.csdn.net/"
linklist = get_link(url)

for link in linklist:
    print(link[0])