# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from urllib import parse
from scrapy.http import HtmlResponse
import json
import pdb   

import random
#from usecookie.items import ToolItem 
from urllib.parse import quote
import re
import sys
sys.path.append(r"/opt/jupyter/scrapy/usecookie/usecookie/spiders/")
import mytool as xianyu_url





class TestcookieSpider(scrapy.Spider):
   #下载城市链接
    name = "andtest"
    
    def start_requests(self):
        
        items = []
        
                    
        for i in range(100):
            wp = i
            catid = 50456012
            divisionId = 110105
            start_urls=xianyu_url.xian_url(wp,catid,divisionId)
            
            print('最终url＋＋＋',start_urls)
            yield scrapy.Request(url=start_urls, method='GET', callback=self.parse_json)
     
            
            

        
        
    def parse_json(self, response):
        
        
        a = re.sub('[\r\n\t]', '', response.body_as_unicode())
        a=a.rstrip(")")
        jop = json.loads(a.lstrip("jsonp143("))
        jo_keys = jop.keys()
        print('jo_keys',jo_keys)
        json_pages = jop['totalPage']
        print('json_pages',json_pages)
