
from mitmproxy import http
from mitmproxy.script import concurrent
from mitmproxy import ctx



def request(flow: http.HTTPFlow) -> None:

    flow.request.host = '104.199.205.163'
    flow.request.port = 8888
    