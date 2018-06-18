
# -*- coding: utf-8 -*-
# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from scrapy import signals
import random
import base64
from scrapy.http.cookies import CookieJar
import sys
#proxyServer = "http-dyn.abuyun.com:9020"
#proxyUser = "HX030NA367CFH6KD"
#proxyPass = "F83B71E29016C7B6"
#proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")
sys.path.append(r"/opt/jupyter/scrapy/xianyu/xianyu/spiders/")
from xianyuclass.user_agents import agents
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from xianyu.configs import *
from chromProxy import *

class ChromeDownloaderMiddleware(object):

    def __init__(self):
        


     

        

        
        options = webdriver.ChromeOptions()
        PROXY = "http://HX030NA367CFH6KD:F83B71E29016C7B6@proxy.abuyun.com:9020"
        desired_capabilities = options.to_capabilities()
        desired_capabilities['proxy'] = {
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "noProxy": None,
            "proxyType": "MANUAL",
            "class": "org.openqa.selenium.Proxy",
            "autodetect": False
        }
        #options.add_argument("--proxy-server=http://proxy.baibianip.com:8000")
    
        options.add_argument('--headless')  
        options.add_argument('--disable-gpu')  
        options.add_argument("window-size=1024,768")  
        options.add_argument("--no-sandbox")  


        
       # options.add_extension(proxyauth_plugin_path)
        
        

        if CHROME_PATH:
            options.binary_location = CHROME_PATH
        if CHROME_DRIVER_PATH:
            self.driver = webdriver.Chrome(chrome_options=options, executable_path=CHROME_DRIVER_PATH,desired_capabilities = desired_capabilities)  # 初始化Chrome驱动
        else:
            self.driver = webdriver.Chrome(chrome_options=options,desired_capabilities = desired_capabilities)  # 初始化Chrome驱动

    def __del__(self):
        self.driver.close()

    def process_request(self, request, spider):

        
        
        
        try:
            print('Chrome driver begin...')
            
            contant = self.driver.get(request.url)  # 获取网页链接内容
            
            
            return HtmlResponse(url=request.url, body=self.driver.page_source, request=request, encoding='utf-8',status=200)  # 返回HTML数据            
            driver.close()
            
        except TimeoutException:
            return HtmlResponse(url=request.url, request=request, encoding='utf-8', status=500)
        finally:
            print('Chrome driver end...')
