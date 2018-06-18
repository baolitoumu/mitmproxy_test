# -*- coding: utf-8 -*-

# Scrapy settings for xianyu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xianyu'

SPIDER_MODULES = ['xianyu.spiders']
NEWSPIDER_MODULE = 'xianyu.spiders'
#REDIRECT_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xianyu (+http://proxy.baibianip.com:8000)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:

#CONCURRENT_REQUESTS_PER_IP = 6

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
COOKIES_DEBUG = False
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

DOWNLOADER_MIDDLEWARES = {
   'xianyu.middlewares.ChromeDownloaderMiddleware': 543,
}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xianyu.middlewares.XianyuSpiderMiddleware': 543,
#}
#LOG_FILE = "error.log" #默认: None，在当前目录里创建logging输出文件的文件名
#LOG_LEVEL = "ERROR" #'DEBUG'，log的最低级别
#LOG_ENABLED = True #默认: True，启用logging
#LOG_ENCODING = 'utf-8' #默认: 'utf-8'，logging使用的编码
#LOG_STDOUT = False #默认: False 如果为 True，进程所有的标准输出(及错误)将会被重定向到log中。例如，执行 print "hello" ，其将会在Scrapy log中显示


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
#RETRY_ENABLED = True
#RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408,302]
#RETRY_TIMES = 10

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'xianyu.pipelines.XianyuPipeline': 500,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#Mysql数据库的配置信息
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy_db'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改 
MYSQL_PASSWD = 'shashuai'         #数据库密码，请修改

MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用