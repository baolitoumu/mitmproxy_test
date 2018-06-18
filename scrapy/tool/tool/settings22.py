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
HTTPERROR_ALLOWED_CODES = [403]

SPIDER_MODULES = ['tool.spiders']
NEWSPIDER_MODULE = 'tool.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'huaban (+http://www.yourdomain.com)'

# Obey robots.txt rules

ROBOTSTXT_OBEY = False
HTTPERROR_ALLOWED_CODES = [404]

HTTPERROR_ALLOWED_CODES = [402]
DOWNLOADER_MIDDLEWARES = {
   'tool.mymiddle.xianyumiddle.ProxyMiddleware': 100,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}



ITEM_PIPELINES = {
    'tool.pipelines.xianyuminiPipeline': 300,
}
