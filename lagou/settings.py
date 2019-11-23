# -*- coding: utf-8 -*-

# Scrapy settings for lagou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagou'

SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'lagou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Cookie': 'LGUID=20171011200319-2bee2600-ae7c-11e7-94b3-5254005c3644; user_trace_token=20171011200323-11be00ff-f82b-4fc7-904e-0165469ba3eb; index_location_city=%E5%8C%97%E4%BA%AC; SEARCH_ID=6db5d2eba4d342faba6fab5b7ee00773; JSESSIONID=ABAAABAABEEAAJA89E72E802C2942257D0BB634F77BDB43; ab_test_random_num=0; X_HTTP_TOKEN=870c4f1f69dc047fd39768b32ecd275b; _ga=GA1.2.1147005544.1507723387; _gid=GA1.2.863770894.1508487710; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508143069,1508487709,1508564738,1508639203; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508641049; LGSID=20171022102652-775b1499-b6d0-11e7-95f4-5254005c3644; LGRID=20171022105729-bdf3bdb7-b6d4-11e7-95f4-5254005c3644; _putrc=6D41DA4A03DDBD36; login=true; unick=%E7%8E%8B%E8%B6%85%E5%87%A1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0',
}

# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'lagou.middlewares.LagouSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'lagou.middlewares.LagouDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# Activating an Item Pipeline component   必须要激活这个处理item的管道/通道才可以使用这条通道处理数据，
#                                       下面的pipeline的作用就是把item数据存储到mongodb数据库中
ITEM_PIPELINES = {
    # 'lagou.pipelines.LagouPipeline': 1,
    'lagou.pipelines.PosCategoryPipeline': 100,
    # 'lagou.pipelines.JavaPostionPipeline': 3,
    # 'lagou.pipelines.PHPPostionPipeline': 4,
    # 'lagou.pipelines.CppPostionPipeline': 5,
    'lagou.pipelines.UIshejishiPipeLine': 2,
    # 'lagou.pipelines.GongsiLocationPipeLine': 100
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 配置每天网站上更新的可以使用的代理网站IP
# PROXIES = ['https://1.198.72.68:9999', 'https://123.57.84.116:8118', 'https://113.195.224.111:9999',
#            'https://125.124.19.124:8088', 'https://125.124.19.124:8088', 'https://47.107.133.109:8000']
# mongodb 数据库连接配置
MONGO_URI = "192.168.65.119"
MONGO_DATABASE = "spider"

# # 设置IP池
# IPPOOL = [
#     {"ipaddr": "221.230.72.165:80"},
#     {"ipaddr": "175.154.50.162:8118"},
#     {"ipaddr": "111.155.116.212:8123"}
# ]

# 设置用户代理池
# UPPOOL = [
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
# ]

# 配置下载中间件的连接信息
# DOWNLOADER_MIDDLEWARES = {
#     # 'scrapy.contrib.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
#     # 'modetest.middlewares.IPPOOlS' : 125,
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 2,
#     'lagou.uamid.Uamid': 1
# }
