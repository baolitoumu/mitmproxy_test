import scrapy
from scrapy import Selector
from urllib import parse
from scrapy.http import HtmlResponse
import json
import pdb   

import random

from urllib.parse import quote
import re
import sys
sys.path.append(r"/opt/jupyter/scrapy/tool/tool/spiders/")
import xianyupy as xianyu_url
q='代购'
q = quote(q.encode("gbk"))
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \
                       Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent': user_agent }


                      
                    


class example(scrapy.Spider):
   #下载城市链接
    name = "ip"
    
    def start_requests(self):
        
        items = []
        
                    
        for i in range(50):
            
            start_urls = 'https://www.iplocation.net'
            
            print('最终url＋＋＋',start_urls)
            yield scrapy.Request(url=start_urls, meta = {'dont_redirect': False},dont_filter = True,callback=self.parse_json)  
     
            
            

        
        
    def parse_json(self, response):
        #a = response.body
        #print(a)
        
        a = response.xpath("//span[@style='font-weight: bold; color:green;']/text()").extract()
        print(a)
        #a = response.xpath('//tbody/tr/th/span').extract()
        #print(a)