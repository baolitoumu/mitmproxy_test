<<<<<<< HEAD
# -*-*-
# 感谢骚男 『挖掘机强森 (QQ: 615918332)』 指正
# -*-*-
=======

>>>>>>> 06358bc514df5927e9199c4d1b943c01944207ad

#! -*- encoding:utf-8 -*-




class ProxyMiddleware(object):
    def process_request(self, request, spider):
<<<<<<< HEAD
       # request.meta['proxy'] = "https://proxy.baibianip.com:8000"
       
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth           
        
        
=======
        request.meta['proxy'] = "proxy.baibianip.com:8000"
        #request.meta["proxy"] = proxyServer
        #request.headers["Proxy-Authorization"] = proxyAuth           
>>>>>>> 06358bc514df5927e9199c4d1b943c01944207ad
