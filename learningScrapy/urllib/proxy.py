from urllib.request import ProxyHandler, build_opener, HTTPHandler, install_opener, urlopen

def use_proxy(proxy_addr, url):
    proxy = ProxyHandler({'http':proxy_addr})
    opener = build_opener(proxy, HTTPHandler)
    install_opener(opener)
    data = urlopen(url).read().decode('utf-8')
    return data

proxy_addr = "191.102.122.3:65301"
data = use_proxy(proxy_addr, "http://www.bing.com")
print(len(data))