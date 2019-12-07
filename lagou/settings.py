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
    'Cookie': 'LGUID=20171011200319-2bee2600-ae7c-11e7-94b3-5254005c3644; user_trace_token=20171011200323-11be00ff-f82b-4fc7-904e-0165469ba3eb; index_location_city=%E5%8C%97%E4%BA%AC; SEARCH_ID=6db5d2eba4d342faba6fab5b7ee00773; JSESSIONID=ABAAABAABEEAAJA89E72E802C2942257D0BB634F77BDB43; ab_test_random_num=0; X_HTTP_TOKEN=870c4f1f69dc047fd39768b32ecd275b; _ga=GA1.2.1147005544.1507723387; _gid=GA1.2.863770894.1508487710; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508143069,1508487709,1508564738,1508639203; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508641049; LGSID=20171022102652-775b1499-b6d0-11e7-95f4-5254005c3644; LGRID=20171022105729-bdf3bdb7-b6d4-11e7-95f4-5254005c3644; _putrc=6D41DA4A03DDBD36; login=true; unick=%E7%8E%8B%E8%B6%85%E5%87%A1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0'
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
#     # 'lagou.middlewares.MyUserAgentMiddleware': 543,
#     # 'lagou.middlewares.CheckUA': 600,
#     # 'lagou.middlewares.ProxyIPMIddleware': 600,
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
    # 'lagou.pipelines.PosCategoryPipeline': 100,
    'lagou.pipelines.JavaPostionPipeline': 3,
    # 'lagou.pipelines.PHPPostionPipeline': 4,
    # 'lagou.pipelines.CppPostionPipeline': 5,
    # 'lagou.pipelines.UIshejishiPipeLine': 200,
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


MONGO_URI = "192.168.65.119"
MONGO_DATABASE = "spider"

COOKIES = '_ga=GA1.2.418244780.1573962429; user_trace_token=20191117114708-ee07ce47-08ec-11ea-a5c3-525400f775ce; LGUID=20191117114708-ee07d187-08ec-11ea-a5c3-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e7778f0b8726-09ebddc0be3456-51402e1a-2073600-16e7778f0b9698%22%2C%22%24device_id%22%3A%2216e7778f0b8726-09ebddc0be3456-51402e1a-2073600-16e7778f0b9698%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; gate_login_token=c49e478bed34efeee1cd98dc445ebda62c77babd300d12c7ab96012ca375b98d; LG_HAS_LOGIN=1; hasDeliver=0; privacyPolicyPopup=false; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; JSESSIONID=ABAAABAAAFCAAEG19F1754D0ACF6A69A64BF4A3DBEA1747; WEBTJ-ID=20191123103650-16e961e7ba367b-01ab2329b9aefa-376b4502-2073600-16e961e7ba4671; _putrc=296FB451539B45F8123F89F2B170EADC; _gid=GA1.2.1853984345.1574476611; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574060058,1574164224,1574236449,1574476611; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B71240; TG-TRACK-CODE=search_code; LGSID=20191123143337-2e6d09a3-0dbb-11ea-a674-5254005c3644; _gat=1; X_HTTP_TOKEN=9b53c27d765922065753944751f4dd06c197b4dd3e; LGRID=20191123151935-9a36f784-0dc1-11ea-a87d-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574493576; SEARCH_ID=52f4a1a898f3489aace8b35c83399763'
