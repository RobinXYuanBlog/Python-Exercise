from urllib.request import Request, urlopen, quote

url_no_wd = "http://www.baidu.com/s?wd="
key_word = "hello"
key_word_ch = "你好"

# Not Complete
# url = url_no_wd + key_word
# req = Request(url)
# data = urlopen(req).read()
# fhandle = open("/Users/robinxyuan/Downloads/baidu_hello.html", "wb")
# fhandle.write(data)
# fhandle.close()


# Complete

key_code = quote(key_word_ch)
url = url_no_wd + key_code
req = Request(url)
data = urlopen(req).read()
