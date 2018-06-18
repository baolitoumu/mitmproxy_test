import scrapy
import json
import re
from urllib.parse import quote
import re
class example(scrapy.Spider):
    
    
    
    
    
    name = "xianyutest"
    allowed_domains = ["taobao.com"]
    
    def start_requests(self):
        

        
        
        
        wp='1'
        _ksTS=''
        callback='jsonp143'
        stype='1'
        catid='57198002'
        divisionId='110105'
        st_trust='1'
        q='代购'
        q = quote(q.encode("gbk"))
        ist='1'
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \
                      Safari/537.36 SE 2.X MetaSr 1.0'
        headers = {'User-Agent': user_agent }
        start_urls='https://s.2.taobao.com/list/waterfall/waterfall.htm?wp='+wp+'&_ksTS='+_ksTS+'&stype='+stype+'&catid='+catid+'&divisionId='+divisionId+'&st_trust='+st_trust+'&q='+q+'&ist='+ist
        #headers = {'User-Agent': user_agent}
        userurl = start_urls
        #return scrapy.Request(url=start_urls, headers=headers,meta={}, method='GET', callback=self.parse)
        yield scrapy.Request(url=start_urls, headers=headers,meta={}, method='GET', callback=self.parse)
        
    def parse(self, response): 
        
        
        a = response.body_as_unicode()
        a = re.sub('[\r\n\t]', '', a)
        a=a.rstrip(")")
        a=a.lstrip("(")
        jo = json.loads(a)
        print (jo.keys())
        
        #print(b)
#         sites = json.loads(response.body_as_unicode()) 
        
#          #jsonresponse = json.loads(response.body_as_unicode())

#         item = MyItem()
#         item["firstName"] = sites["firstName"]             
#         return item
#         #for site in sites:  
       # print(site)