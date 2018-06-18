import scrapy
from scrapy import Selector
from urllib import parse
from scrapy.http import HtmlResponse
import json
import pdb

import random
from xianyu.items import XianyuItem 
from urllib.parse import quote
import re
import sys
sys.path.append(r"/opt/jupyter/scrapy/xianyu/xianyu/spiders/")
from xianyuclass import xian




class example(scrapy.Spider):
   #下载城市链接
    name = "xianyu"
    
    def start_requests(self):
        
        items = []
        f = open("city.txt")  
        sj = json.load(f)
        sj = sj["city"]
        
            
            
        
        for i in sj:
            item = XianyuItem()
            q = 'sony'
            
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
        print('循环＋＋＋＋')
        
        #print("城市分类item",item_1)
        #先定义一个空列表
        items=[]
        #解析返回的网页数据
        #一级分类的url 
        page_url = response.xpath("//*[@class='sub-category']/@href").extract()
        #一级分类的名称
        titles = response.xpath("//*[@class='sub-category']/em/text()").extract()
        item_1 = response.meta['item_0']
        for page,title in zip(page_url, titles): 
            item = XianyuItem()
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
        #print("一级分类item",item_1)
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
                    item = XianyuItem()
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
                #print("没有下级目录++++++++++++++++++++++++++++++++")
                #print("开始爬当前区url++++++++++++++++++++++++++++++++")
                page_url_last  = i.xpath("//*/div[@class='district-list']/a/span/span[@class='item-num']/../../@href").extract()
                title_last = i.xpath("//*/div[@class='district-list']/a/span/span[@class='item-num']/preceding-sibling::em/text()").extract()
                #print('城市目录名称+++',title_last)
                #print("开始爬当前城市区url++++",page_url_last)
                
                for pages,titles in zip(page_url_last, title_last): 
                    item = XianyuItem()
                    url = response.urljoin(pages)
                    
                    item['word'] = item_1['word']
                    item['city_url'] = item_1['city_url']
                    item['city_code'] = item_1['city_code']
                    item['city_name'] = item_1['city_name']
                    item['city_name_province'] = item_1['city_name_province']
                    
                    item['firstlevel_title'] = item_1['firstlevel_title']
                    item['firstlevel_url'] = item_1['firstlevel_url']
                    
                    item['twolevel'] = 0
                    item['twolevel_url'] = 0
      
        
                    
                    item['threelevel'] = 0
                    item['threelevel_url'] = 0
                    
                    
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
#         print('二级 ',pages)
        
        for i in pages:
            title = i.xpath("//*/div[@class='category-list J_HiddenArea']/ul/li/a/text()").extract()
            page_url = i.xpath("//*/div[@class='category-list J_HiddenArea']/ul/li/a/@href").extract()
            
            if page_url :
#                 print('title爬取第三级类目+++',title)
#                 print("page_url++++",page_url)
                
                
                for pages,titles in zip(page_url, title): 
                    item = XianyuItem()
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
                    
                    item['threelevel'] = titles
                    item['threelevel_url'] = url
                    items.append(item)
                    
                    
                    
                    
                    
                for item in items:
            #对列表遍历，回调parse_item的函数 请求的是每个cate_url meta将这一层的数据传递到下一层
                    yield scrapy.Request(url=item['threelevel_url'],meta={'item_3':item}, callback=self.parse_url_next2,dont_filter=True)  
                
                
            else:
#                 print("没有下级目录++++++++++++++++++++++++++++++++")
#                 print("开始爬当前城市区url++++++++++++++++++++++++++++++++")
                page_url_last  = i.xpath("//*/div[@class='district-list']/a/span/span[@class='item-num']/../../@href").extract()
                title_last = i.xpath("//*/div[@class='district-list']/a/span/span[@class='item-num']/preceding-sibling::em/text()").extract()
#                 print('城市目录名称+++',title_last)
#                 print("开始爬当前城市区url++++",page_url_last)
                
                for pages,titles in zip(page_url_last, title_last): 
                    item = XianyuItem()
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
                    
                    item['threelevel'] = 0
                    item['threelevel_url'] = 0
                    
                    item['district'] = titles
                    item['district_url'] = url
                    
                    items.append(item)
                    
                for item in items:
            #对列表遍历，回调parse_item的函数 请求的是每个cate_url meta将这一层的数据传递到下一层
                    yield scrapy.Request(url=item['district_url'],meta={'item_city':item}, callback=self.open_des)  
                
    
    def parse_url_next2(self, response): 
        #下载三级类目的链接，如果没有就下载城市内区的链接
        item_1= response.meta['item_3']
        #print("三级分类item",item_1)
        #再次定义空列表，用来保存上一层的数据和本层的数据
        items=[]
        pages =  response.xpath("//html")
        
        for i in pages:
            
            page_url_last  = i.xpath("//*/div[@class='district-list']/a/span/span[@class='item-num']/../../@href").extract()
            title_last = i.xpath("//*/div[@class='district-list']/a/span/span[@class='item-num']/preceding-sibling::em/text()").extract()
            
            for pages,titles in zip(page_url_last, title_last): 
                    item = XianyuItem()
                    
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
                    
                    item['threelevel'] = item_1['threelevel']
                    item['threelevel_url'] = item_1['threelevel_url']
                    
                    item['district'] = titles
                    item['district_url'] = url
                    
                    items.append(item)
                    
            for item in items:
            #对列表遍历，回调parse_item的函数 请求的是每个cate_url meta将这一层的数据传递到下一层
                yield scrapy.Request(url=item['district_url'],meta={'item_city':item}, callback=self.open_des)  
                
                
    def open_des(self, response): 
        #先爬第一页，按照分页数量爬取
        #print('开始拼接url')
        #接受上个item传过来的内容
        item_1= response.meta['item_city']
        item = XianyuItem()
        
        #print('item+keyskeys+keys+++++keys+',item.keys)
        #print('接收到的item',item)
        url = response.url
        urla = url.split("?")
        #print('urla++++++++++++++++',urla)
        res = parse.parse_qs(urla[1])
#         print(res)
#         print('catid===',res["catid"][0])
#         print('获取到的url+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++',response.url)
#         print('获取到的url参数+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++',res)
        
        wp='1'
        
        catid=res["catid"][0]
        divisionId=res["divisionId"][0]
        q = item_1['word']
        #print('catid',catid)
        #print('divisionId',divisionId)
        start_urls=xian.xian_url(wp,catid,divisionId)
        
        item['word'] = item_1['word']
        item['city_url'] = item_1['city_url']
        item['city_code'] = item_1['city_code']
        item['city_name'] = item_1['city_name']
        item['city_name_province'] = item_1['city_name_province']
        item['firstlevel_title'] = item_1['firstlevel_title']
        item['firstlevel_url'] = item_1['firstlevel_url']
        
        item['twolevel'] = item_1['twolevel']
        item['twolevel_url'] = item_1['twolevel_url']
      
        
                    
        item['threelevel'] = item_1['threelevel']
        item['threelevel_url'] = item_1['threelevel_url']
                    
        item['district'] = item_1['district']
        item['district_url'] = item_1['district_url']
                    
        item['final_url'] = start_urls
        #print('最终url+++++++++',start_urls)
        #item.append(item)
        #return scrapy.Request(url=start_urls, headers=headers,meta={}, method='GET', callback=self.parse)
        yield scrapy.Request(url=start_urls,meta={'proxy': 'proxy.baibianip.com:8000','item_lasturl':item,'catid':catid,'divisionId':divisionId}, method='GET', callback=self.parse_json)
        
    def parse_json(self, response): 
        # url = response.url   
        # urla = url.split("?")
        # print('urla++++++++++++++++',urla)
        # res = parse.parse_qs(urla[1])
        
        item_1= response.meta['item_lasturl']
        item = XianyuItem()
        
        item['word'] = item_1['word']
        item['city_url'] = item_1['city_url']
        item['city_code'] = item_1['city_code']
        item['city_name'] = item_1['city_name']
        item['city_name_province'] = item_1['city_name_province']
        item['firstlevel_title'] = item_1['firstlevel_title']
        item['firstlevel_url'] = item_1['firstlevel_url']
        
        item['twolevel'] = item_1['twolevel']
        item['twolevel_url'] = item_1['twolevel_url']
      

        item['threelevel'] = item_1['threelevel']
        item['threelevel_url'] = item_1['threelevel_url']
                    
        item['district'] = item_1['district']
        item['district_url'] = item_1['district_url']
                    
        item['final_url'] =  item_1['final_url']
        
        a = re.sub('[\r\n\t]', '', response.body_as_unicode())
        a=a.rstrip(")")
        a=a.lstrip("(")
        #jop = json.loads(a.lstrip("jsonp143("))
        jop = json.loads(a)
        jo_keys = jop.keys()
        #print('jo_keys',jo_keys)
        json_pages = jop['totalPage']
        #print('json_pages',json_pages)
        
        
        
        
        
        #print('开始拉取json')
        if json_pages == 1:
            
            info = jop['idle']
            
            item['numFound'] = jop['numFound']
            item['currPage'] = jop['currPage']
            item['totalPage'] = jop['totalPage']
            item['ershouCount'] = jop['ershouCount']
            item['idleCount'] = jop['idleCount']
            item['ershou'] = jop['ershou']
    
            item['user_Icon'] = jop['idle'][0]['user']['userIcon']
            item['user_Nick'] = jop['idle'][0]['user']['userNick']
            item['user_vipLevel'] = jop['idle'][0]['user']['vipLevel']
            item['user_TypeId'] = jop['idle'][0]['user']['userTypeId']
            item['user_isTaobaoWomen'] = jop['idle'][0]['user']['isTaobaoWomen']
            item['user_taobaoWomenUrl'] = jop['idle'][0]['user']['taobaoWomenUrl']
            item['user_CreditUrl'] = jop['idle'][0]['user']['userCreditUrl']
            item['user_ItemsUrl'] = jop['idle'][0]['user']['userItemsUrl']
            item['user_isSinaV'] =jop['idle'][0]['user']['isSinaV']
            item['user_yellowSeller'] = jop['idle'][0]['user']['yellowSeller']
            
            item['item_imageUrl'] = jop['idle'][0]['item']['imageUrl']
            item['item_imageHeight'] = jop['idle'][0]['item']['imageHeight']
            item['item_imageWidth'] = jop['idle'][0]['item']['imageWidth']
            item['item_Url'] = jop['idle'][0]['item']['itemUrl']
            item['item_isBrandNew'] = jop['idle'][0]['item']['isBrandNew']
            item['item_price'] = jop['idle'][0]['item']['price']
            item['item_orgPrice'] = jop['idle'][0]['item']['orgPrice']
            item['item_provcity'] = jop['idle'][0]['item']['provcity']
            item['item_describe'] = jop['idle'][0]['item']['describe']
            item['item_publishTime'] = jop['idle'][0]['item']['publishTime']
            item['item_From'] = jop['idle'][0]['item']['itemFrom']
            item['item_FromDesc'] = jop['idle'][0]['item']['itemFromDesc']
            item['item_FromTarget'] = jop['idle'][0]['item']['itemFromTarget']
            item['item_commentCount'] = jop['idle'][0]['item']['commentCount']
            item['item_commentUrl'] = jop['idle'][0]['item']['commentUrl']
            item['item_collectCount'] = jop['idle'][0]['item']['collectCount']
            item['item_title'] = jop['idle'][0]['item']['title'] 
            #print('itemitemitemitem',item)
            
            yield item
        else:
            
            for json_page in range(json_pages):
                if json_page == 101:
                    break
                else:
                    
                    catid= response.meta['catid']
                    divisionId= response.meta['divisionId']
                    q =  item['word'] 
                    wp = json_page
                    start_urls=xian.xian_url(wp,catid,divisionId)
                    #print('最终url+++++++++',start_urls)
                    yield scrapy.Request(url=start_urls,meta={'proxy': 'proxy.baibianip.com:8000','data':item}, method='GET', callback=self.parse_json_end)
            
            

        
        
    def parse_json_end(self, response):
        
        item_1= response.meta['data']
        item = XianyuItem()
        
        item['word'] = item_1['word']
        item['city_url'] = item_1['city_url']
        item['city_code'] = item_1['city_code']
        item['city_name'] = item_1['city_name']
        item['city_name_province'] = item_1['city_name_province']
        item['firstlevel_title'] = item_1['firstlevel_title']
        item['firstlevel_url'] = item_1['firstlevel_url']
        
        item['twolevel'] = item_1['twolevel']
        item['twolevel_url'] = item_1['twolevel_url']
      
        
                    
        item['threelevel'] = item_1['threelevel']
        item['threelevel_url'] = item_1['threelevel_url']
                    
        item['district'] = item_1['district']
        item['district_url'] = item_1['district_url']
                    
        item['final_url'] =  item_1['final_url']
        
        a = re.sub('[\r\n\t]', '', response.body_as_unicode())
        a=a.rstrip(")")
        a=a.lstrip("(")
        #jop = json.loads(a.lstrip("jsonp143("))
        jop = json.loads(a)
        
        json_pages = jop['totalPage']
        #print('json_pages',json_pages)
        if json_pages > 20:
            json_pages = 20
            
        
        for i in range(json_pages):
            
            info = jop['idle']
            
            item['numFound'] = jop['numFound']
            item['currPage'] = jop['currPage']
            item['totalPage'] = jop['totalPage']
            item['ershouCount'] = jop['ershouCount']
            item['idleCount'] = jop['idleCount']
            item['ershou'] = jop['ershou']
    
            item['user_Icon'] = jop['idle'][i]['user']['userIcon']
            item['user_Nick'] = jop['idle'][i]['user']['userNick']
            item['user_vipLevel'] = jop['idle'][i]['user']['vipLevel']
            item['user_TypeId'] = jop['idle'][i]['user']['userTypeId']
            item['user_isTaobaoWomen'] = jop['idle'][i]['user']['isTaobaoWomen']
            item['user_taobaoWomenUrl'] = jop['idle'][i]['user']['taobaoWomenUrl']
            item['user_CreditUrl'] = jop['idle'][i]['user']['userCreditUrl']
            item['user_ItemsUrl'] = jop['idle'][i]['user']['userItemsUrl']
            item['user_isSinaV'] =jop['idle'][i]['user']['isSinaV']
            item['user_yellowSeller'] = jop['idle'][i]['user']['yellowSeller']
            
            item['item_imageUrl'] = jop['idle'][i]['item']['imageUrl']
            item['item_imageHeight'] = jop['idle'][i]['item']['imageHeight']
            item['item_imageWidth'] = jop['idle'][i]['item']['imageWidth']
            item['item_Url'] = jop['idle'][i]['item']['itemUrl']
            item['item_isBrandNew'] = jop['idle'][i]['item']['isBrandNew']
            item['item_price'] = jop['idle'][i]['item']['price']
            item['item_orgPrice'] = jop['idle'][i]['item']['orgPrice']
            item['item_provcity'] = jop['idle'][i]['item']['provcity']
            item['item_describe'] = jop['idle'][i]['item']['describe']
            item['item_publishTime'] = jop['idle'][i]['item']['publishTime']
            item['item_From'] = jop['idle'][i]['item']['itemFrom']
            item['item_FromDesc'] = jop['idle'][i]['item']['itemFromDesc']
            item['item_FromTarget'] = jop['idle'][i]['item']['itemFromTarget']
            item['item_commentCount'] = jop['idle'][i]['item']['commentCount']
            item['item_commentUrl'] = jop['idle'][i]['item']['commentUrl']
            item['item_collectCount'] = jop['idle'][i]['item']['collectCount']
            item['item_title'] = jop['idle'][i]['item']['title'] 
            #print('开始返回内容。。。。。。。。。')
            #print(item)
            
            yield item    
        
        
        
        
        
        
         