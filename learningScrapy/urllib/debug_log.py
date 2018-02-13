from urllib.request import build_opener, HTTPHandler, HTTPSHandler, install_opener, urlopen

httphd = HTTPHandler(debuglevel=1)
httpshd = HTTPSHandler(debuglevel=1)
opener = build_opener(httphd, httpshd)

install_opener(opener)
data = urlopen("http://edu.51cto.com")