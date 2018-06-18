
    
from urllib import parse
from scrapy.http import HtmlResponse
import json
import pdb   

import random
#from tool.items import ToolItem 
from urllib.parse import quote
def xian_url(wp,catid,divisionId):
        
        q='sony'
        q = quote(q.encode("gbk"))
        wp = str(wp)
        catid = str(catid)
        divisionId = str(divisionId)
        
        
        
        a = random.randint(0,999) 
        b = a-1
        b = str(b)
        
        _ksTS='1515549364328_'+b
        callback=''
        stype='1'
        
        st_trust='1'
        
        ist='1'
         
        start_urls='https://s.2.taobao.com/list/waterfall/waterfall.htm?wp='+wp+'&_ksTS='+_ksTS+'&stype='+stype+'&catid='+catid+'&divisionId='+divisionId+'&st_trust='+st_trust+'&q='+q+'&ist='+ist
        
        
        
        return(start_urls)
