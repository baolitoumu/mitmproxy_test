
from mitmproxy import http
from mitmproxy.script import concurrent
from mitmproxy import ctx



def request(flow: http.HTTPFlow) -> None:
"""    if flow.request.method == "CONNECT":
        print('flow.request.method == "CONNECT":')
        # If the decision is done by domain, one could also modify the server address here.
        # We do it after CONNECT here to have the request data available as well.
        return
    #address = proxy_address(flow)
    if flow.live:
        flow.live.change_upstream_proxy_server('104.199.205.163:8888')"""
    flow.request.host = '104.199.205.163'
    flow.request.port = '8888'
    