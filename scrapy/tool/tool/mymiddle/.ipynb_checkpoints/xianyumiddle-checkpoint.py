# -*-*-
# 感谢骚男 『挖掘机强森 (QQ: 615918332)』 指正
# -*-*-

#! -*- encoding:utf-8 -*-

import base64

# 代理服务器
proxyServer = "http-dyn.abuyun.com:9020"

# 代理隧道验证信息
proxyUser = "HM844386HX628USD"
proxyPass = "4875782637CE16FB"

# for Python2
    #proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)

    # for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")



class ProxyMiddleware(object):
    def process_request(self, request, spider):
       # request.meta['proxy'] = "https://proxy.baibianip.com:8000"
       
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth           
        
        
