# -*- coding: utf-8 -*-

# Scrapy settings for huaban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tool'


SPIDER_MODULES = ['tool.spiders']
NEWSPIDER_MODULE = 'tool.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'huaban (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


DOWNLOADER_MIDDLEWARES = {    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,  
'one.middlewares.ProxyMiddleware': 100,}



ITEM_PIPELINES = {
    'tool.pipelines.xianyuminiPipeline': 300,
}
