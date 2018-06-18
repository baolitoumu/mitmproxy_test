import scrapy
import json
from urllib.parse import quote
class example(scrapy.Spider):
    name = "test2"
    
    def start_requests(self):
        f = open("city.txt") 
        s = json.load(f)
        s = s["city"]
        q= '代购'
        pages=[]
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \
                       Safari/537.36 SE 2.X MetaSr 1.0'
        headers = {'User-Agent': user_agent }
        for i in s:
            #time.sleep(500)
            
            url ='https://s.2.taobao.com/list/list.htm?_input_charset=utf8&q='+q+'&divisionId='+i["code"]
            page= scrapy.Request(url, headers=headers,meta={}, method='GET', callback=self.parse)
            
            pages.append(page)
        return pages
    def parse(self, response): 
        for page_url in response.xpath("//*[@class='sub-category']/@href").extract():
            
            page_url = response.urljoin(page_url)
            yield scrapy.Request(page_url, callback=self.parse)
    def parse_url(self, response): 
        for page_url in response.xpath("//*[@class='J_HiddenAreaContent clearfix']/li/a/@href").extract():
            a = response.xpath("//*[@class='J_HiddenAreaContent clearfix']/li/a/@title").extract()
            print(a)
            page_url = response.urljoin(page_url)
            yield scrapy.Request(url=page_url, callback=self.parse)
