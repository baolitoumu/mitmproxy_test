
from mitmproxy import http
from mitmproxy.script import concurrent
from mitmproxy import ctx



def request(flow):
    proxy='104.155.220.54'
   
    port=8888
    flow.live.change_upstream_proxy_server((proxy,port))