from http.client import HTTPConnection
from urllib.parse import urlencode

conn = None
try:
    params = urlencode({'name':'qiye', 'age':'23'})
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }
    conn = HTTPConnection("www.zhihu.com", 80, timeout=3)
    conn.request("POST", "/login", params, headers)
    response = conn.getresponse()
    print(response.getheaders())
    print(response.status)
    print(response.read())
except Exception as e:
    print(e)
finally:
    if conn:
        conn.close()