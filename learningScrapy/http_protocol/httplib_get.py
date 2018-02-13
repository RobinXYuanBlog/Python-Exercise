import http.client

conn = None
try:
    conn = http.client.HTTPConnection('www.zhihu.com')
    conn.request("GET", "/")
    response = conn.getresponse()
    print(response.status, response.reason)
    print('-' * 40)
    headers = response.getheaders()
    for h in headers:
        print(h)
    print('-' * 40)
    print(response.msg)
except Exception as e:
    print(e)
finally:
    if conn:
        conn.close()

