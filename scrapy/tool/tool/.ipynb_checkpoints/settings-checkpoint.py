# -*- coding: utf-8 -*-

# Scrapy settings for tool project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent
BOT_NAME = 'tool'
DEPTH_LIMIT=4
SPIDER_MODULES = ['tool.spiders']
NEWSPIDER_MODULE = 'tool.spiders'








# 
ITEM_PIPELINES = {
    'tool.pipelines.MySQLPipeline': 400,
}


CONCURRENT_REQUESTS_PER_IP = 3
COOKIES_DEBUG =True

DOWNLOADER_MIDDLEWARES = {
   #'tool.mymiddle.xianyumiddle.ProxyMiddleware': 100,
    'tool.middlewares.ToolDownloaderMiddleware':100,
 #  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}
COOKIES_ENABLES =False


# and the best one, random via real world browser usage statistic
#ua.random


ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1


#Mysql数据库的配置信息
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy_db'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改 
MYSQL_PASSWD = 'shashuai'         #数据库密码，请修改

MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用
