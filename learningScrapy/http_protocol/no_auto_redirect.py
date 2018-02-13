from urllib.request import HTTPRedirectHandler
from urllib.request import build_opener

class RedirectHandler(HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        result = HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        result.status = code
        result.newurl = result.geturl()
        return result

opener = build_opener(RedirectHandler)
opener.open('http://www.zhihu.cn')