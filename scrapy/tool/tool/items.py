# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToolItem(scrapy.Item):
    
    word = scrapy.Field()
    city_url = scrapy.Field()
    city_code = scrapy.Field()
    city_name = scrapy.Field()
    city_name_province = scrapy.Field()
    firstlevel_title = scrapy.Field()
    firstlevel_url = scrapy.Field()       
    twolevel = scrapy.Field()
    twolevel_url = scrapy.Field()       
    threelevel = scrapy.Field()
    threelevel_url = scrapy.Field()
    district = scrapy.Field()
    district_url = scrapy.Field()
    final_url =  scrapy.Field()
    
    numFound = scrapy.Field()
    currPage = scrapy.Field()
    totalPage = scrapy.Field()
    ershouCount = scrapy.Field()
    idleCount = scrapy.Field()
    ershou = scrapy.Field()
    
    user_Icon = scrapy.Field()
    user_Nick = scrapy.Field()
    user_vipLevel = scrapy.Field()
    user_TypeId = scrapy.Field()
    user_isTaobaoWomen = scrapy.Field()
    user_taobaoWomenUrl = scrapy.Field()
    user_CreditUrl = scrapy.Field()
    user_ItemsUrl = scrapy.Field()
    user_isSinaV = scrapy.Field()
    user_yellowSeller = scrapy.Field()
    item_imageUrl = scrapy.Field()
    item_imageHeight = scrapy.Field()
    item_imageWidth = scrapy.Field()
    item_Url = scrapy.Field()
    item_isBrandNew = scrapy.Field()
    item_price = scrapy.Field()
    item_orgPrice = scrapy.Field()
    item_provcity = scrapy.Field()
    item_describe = scrapy.Field()
    item_publishTime = scrapy.Field()
    item_From = scrapy.Field()
    item_FromDesc = scrapy.Field()
    item_FromTarget = scrapy.Field()
    item_commentCount = scrapy.Field()
    item_commentUrl = scrapy.Field()
    item_collectCount = scrapy.Field()
    item_title = scrapy.Field()
    
    pass
