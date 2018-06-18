import scrapy
from scrapy import Selector
from urllib import parse
from scrapy.http import HtmlResponse
import json
import pdb   

import random
from tool.items import ToolItem 
from urllib.parse import quote
import re
q='代购'
q = quote(q.encode("gbk"))
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \
                       Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent': user_agent }

class example(scrapy.Spider):
   #下载城市链接
    name = "xianyumini2"
    
    def start_requests(self):
        
        items = []
        f = open("city.txt")  
        sj = json.load(f)
        sj = sj["city"]
        
            
            
        
        for i in sj:
            item = ToolItem()
            q = '代购'
            
            city_code = i["code"]  
            url ='https://s.2.taobao.com/list/list.htm?_input_charset=utf8&q='+q+'&divisionId='+city_code
            city_name = i["name"]
            city_name_province = i["province"]
            
            item['word'] = q
            item['city_url'] = url
            item['city_code'] = city_code
            item['city_name'] = city_name
            item['city_name_province'] = city_name_province
            
            items.append(item)
            
        for item in items:
            
            yield scrapy.Request(url=item['city_url'],meta={'item_0':item}, callback=self.parse,dont_filter=True)  
        
    
    def parse(self, response):
        item_1 = response.meta['item_0']
        print("城市分类item",item_1)
        #先定义一个空列表
        items=[]
        #解析返回的网页数据
        #一级分类的url 
        page_url = response.xpath("//*[@class='sub-category']/@href").extract()
        #一级分类的名称
        titles = response.xpath("//*[@class='sub-category']/em/text()").extract()

        for page,title in zip(page_url, titles): 
            item = ToolItem()
            #在循环里对item进行实例化，类型为字典
            #对url进行拼接
            url = response.urljoin(page)
            #items.py中field()中的一级分类url和title
            
            item['word'] = item_1['word']
            item['city_url'] = item_1['city_url']
            item['city_code'] = item_1['city_code']
            item['city_name'] = item_1['city_name']
            item['city_name_province'] = item_1['city_name_province']
 
            item['firstlevel_title'] = title
            item['firstlevel_url'] = url
            items.append(item)
        #此时列表items_1添加了所有获取到的分类cate_url和cate_name所有的元素是字典，每个元素是{'firstlevel_url':'url的连接','firstlevel_title'：获取到的分类名称}
        for item in items:
            
            #对列表遍历，回调parse_item的函数 请求的是每个cate_url meta将这一层的数据传递到下一层
            yield scrapy.Request(url=item['firstlevel_url'],meta={'item_1':item}, callback=self.parse_url,dont_filter=True)  

        
    def parse_url(self, response): 
        ####如果一级类目里面下载不到二级类目的链接，则下载当前城市的区的链接
        #item_1接收上一层的数据
        item_1= response.meta['item_1']
        #再次定义空列表，用来保存上一层的数据和本层的数据
        print("一级分类item",item_1)
        items=[]
        pages =  response.xpath("//html")
        
        
        for i in pages:
            title = i.xpath("//*/div[@class='category-list J_HiddenArea']/ul/li/a/text()").extract()
            page_url = i.xpath("//*/div[@class='category-list J_HiddenArea']/ul/li/a/@href").extract()
            if page_url :
                
#                 print('有分类++++++++++++++++++++++')
#                 print('title爬取第二级类目+++',title)
#                 print("page_url++++",page_url)
                for pages,titles in zip(page_url, title): 
                    item = ToolItem()
                    url = response.urljoin(pages)
                    
                    item['word'] = item_1['word']
                    item['city_url'] = item_1['city_url']
                    item['city_code'] = item_1['city_code']
                    item['city_name'] = item_1['city_name']
                    item['city_name_province'] = item_1['city_name_province']
 
                    item['firstlevel_title'] = item_1['firstlevel_title']
                    item['firstlevel_url'] = item_1['firstlevel_url']
            
                    item['twolevel'] = titles
                    item['twolevel_url'] = url
                    items.append(item)
        
                for item in items:
            #对列表遍历，回调parse_item的函数 请求的是每个cate_url meta将这一层的数据传递到下一层
                    yield scrapy.Request(url=item['twolevel_url'],meta={'item_2':item}, callback=self.parse_url_next,dont_filter=True)  
                
            else:
                print("没有下级目录++++++++++++++++++++++++++++++++")
                print("开始爬当前区url++++++++++++++++++++++++++++++++")
                page_url_last  = i.xpath("//*/div[@class='district-list']/a/span/span[@class='item-num']/../../@href").extract()
                title_last = i.xpath("//*/div[@class='district-list']/a/span/span[@class='item-num']/preceding-sibling::em/text()").extract()
                print('城市目录名称+++',title_last)
                print("开始爬当前城市区url++++",page_url_last)
                
                for pages,titles in zip(page_url_last, title_last): 
                    item = ToolItem()
                    url = response.urljoin(pages)
                    
                    item['word'] = item_1['word']
                    item['city_url'] = item_1['city_url']
                    item['city_code'] = item_1['city_code']
                    item['city_name'] = item_1['city_name']
                    item['city_name_province'] = item_1['city_name_province']
 
                    item['firstlevel_title'] = item_1['firstlevel_title']
                    item['firstlevel_url'] = item_1['firstlevel_url']
                    
                    item['district'] = titles
                    item['district_url'] = url
                    items.append(item)
                for item in items:
            #对列表遍历，回调parse_item的函数 请求的是每个cate_url meta将这一层的数据传递到下一层
                    yield scrapy.Request(url=item['district_url'],meta={'item_city':item}, callback=self.open_des,dont_filter=True)  
              
        

    def parse_url_next(self, response): 
        item_1= response.meta['item_2']
        print("二级分类item",item_1)
        #再次定义空列表，用来保存上一层的数据和本层的数据
        items=[]
        
        #下载三级类目的链接，如果没有就下载城市内区的链接
        pages =  response.xpath("//html")

        
        for i in pages:
            
            page_url_last  = i.xpath("//*/div[@class='district-list']/a/span/span[@class='item-num']/../../@href").extract()
            title_last = i.xpath("//*/div[@class='district-list']/a/span/span[@class='item-num']/preceding-sibling::em/text()").extract()

            for pages,titles in zip(page_url_last, title_last): 
                item = ToolItem()
                url = response.urljoin(pages)
                    
                    

                    
                item['word'] = item_1['word']
                item['city_url'] = item_1['city_url']
                item['city_code'] = item_1['city_code']
                item['city_name'] = item_1['city_name']
                item['city_name_province'] = item_1['city_name_province']
 
                item['firstlevel_title'] = item_1['firstlevel_title']
                item['firstlevel_url'] = item_1['firstlevel_url']
            
                item['twolevel'] = item_1['twolevel']
                item['twolevel_url'] = item_1['twolevel_url']
                    
                item['district'] = titles
                item['district_url'] = url
                   
                items.append(item)
                    
            for item in items:
                return scrapy.Request(url=item['district_url'],meta={'item_city':item}, callback=self.open_des,dont_filter=True)  
                        
                  
            #对列表遍历，回调parse_item的函数 请求的是每个cate_url meta将这一层的数据传递到下一层
                    
                
    
    
                
                
    def open_des(self, response): 
        #先爬第一页，按照分页数量爬取
        print('开始拼接url')
        item = ToolItem()
        item= response.meta['item_city']
        url = response.url
        urla = url.split("?")
        print('urla++++++++++++++++',urla)
        res = parse.parse_qs(urla[1])
#         print(res)
#         print('catid===',res["catid"][0])
#         print('获取到的url+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++',response.url)
#         print('获取到的url参数+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++',res)
        
        wp='1'
        a = random.randint(0,999)
        b = a-1
        b = str(b)
        a = str(a)
        _ksTS='1515549364328_'+b
        callback='jsonp143'
        stype='1'
        catid=res["catid"][0]
        divisionId=res["divisionId"][0]
        st_trust='1'

        ist='1'
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \
                      Safari/537.36 SE 2.X MetaSr 1.0'
        headers = {'User-Agent': user_agent }
        start_urls='https://s.2.taobao.com/list/waterfall/waterfall.htm?wp='+wp+'&_ksTS='+_ksTS+'&stype='+stype+'&catid='+catid+'&divisionId='+divisionId+'&st_trust='+st_trust+'&q='+q+'&ist='+ist
        
        item['final_url'] = start_urls
        #return scrapy.Request(url=start_urls, headers=headers,meta={}, method='GET', callback=self.parse)
        yield scrapy.Request(url=start_urls, headers=headers,meta={'data':item}, method='GET', callback=self.parse_json)
        print('somethingops')
    def parse_json(self, response): 
        print('开始拉取json')
        item = ToolItem()
        item= response.meta['data']
        a = response.body_as_unicode()
        a = re.sub('[\r\n\t]', '', a)
        a=a.rstrip(")")
        a=a.lstrip("jsonp143(")
        jo = json.loads(a)
        print(jo.keys)
        print(a)
        print(a)
        
        
        
        
        
        
        
        
        