# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
import json

from lagou.items import LagouItem


class LagouspiderSpider(CrawlSpider):
    name = 'lagouSpider'
    name = 'lagou'
    redis_key = 'lagou:start_urls'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com']

    rules = (
        # Rule(LinkExtractor(allow=("zhaopin/.*",), callback='parse_item'),
        #      Rule(LinkExtractor(allow=("gongsi/j\d+.html",), callback='parse_item')
        #           # Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_item', follow=True),
        #           )
        #      )
        Rule(LinkExtractor(allow=r'zhaopin/.*'), callback='parse_item', follow=True),
        # Rule(link_extractor=LinkExtractor(allow='gongsi/j\d+.html'), callback='parse_item')
    )

    def parse_item(self, response):
        # l = ItemLoader(item=LagouItem(), response=response)
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = LagouItem()
        htmls = response.body
        # 公司名称
        co_name = response.xpath("//div[@class='company']/div[@class='company_name']/a/text()").get()
        # 职位名称
        name = response.xpath(
            "//li[@class='con_list_item default_list']//div[@class='p_top']//h3/text()").get()
        # 薪资
        salary = response.xpath(
            "//div[@class='postion']//div[@class='p_bot']//span[@class='money']/text()").get()
        # 区域
        area = response.xpath(
            "//div[@class='postion']//div[@class='p_bot']//span[@class='add']/em/text()").get()
        # 工作年限
        exp = response.xpath(
            "//div[@class='postion']//div[@class='p_bot']//div[@class='li_b_l']/text()").get()
        # 学历
        edu = response.xpath(
            "//div[@class='postion']//div[@class='p_bot']//div[@class='li_b_l']/text()").get()
        # 发布时间
        time = response.xpath("//div[@class='p_top']//span[@class='format-time']/text()").get()
        time = self.getVal(time)
        # 职位描述
        info = response.xpath(
            "//li[@data-positionname=$val]//div[@class='list_item_bot']/div[@class='li_b_l']/span/text()",
            val=name).getall()
        info = ";".join(info)
        print("info" * 20, info)
        # info = self.getVal(info)
        # if info != '':
        #     info = '\n'.join(info).encode('utf-8')

        # 工作地点
        local = response.xpath(
            "//div[@class='postion']//div[@class='p_bot']//span[@class='add']//em/text()").get()
        # 公司福利
        welfare = response.xpath("//div[@class='list_item_bot']//div[@class='li_b_r']/text()").get()
        # 公司网址
        co_url = ""
        # 招聘人数
        num = '0'
        # 公司类别
        co_type = response.xpath('//dl[@class="industry"]/text()').get()
        # print("++" * 80)
        # print(name, co_name, area, salary, exp, edu, num, time, welfare, info, local, co_url, co_type)
        item['name'] = name
        item['co_name'] = co_name
        item['area'] = area
        item['salary'] = salary
        item['exp'] = exp
        item['edu'] = edu
        item['num'] = num
        item['time'] = time
        item['welfare'] = welfare
        item['info'] = str(info)
        item['local'] = local
        item['co_url'] = co_url
        item['co_type'] = co_type

        # print('+====' * 80, item)
        # itemJson = json.dumps(item, default=obj2json)
        # print(itemJson)
        yield item

    def getVal(self, data):
        return data if data else ''


def obj2json(obje):
    if (isinstance(object, LagouItem)):
        return {
            'name': LagouItem.name,
            'co_name': LagouItem.co_name,
            'area': LagouItem.area,
            '-salary': LagouItem.salary,
            'exp': LagouItem.exp,
            'edu': LagouItem.edu,
            'num': LagouItem.num,
            'time': LagouItem.time,
            'welfare': LagouItem.welfare,
            'info': LagouItem.info,
            'local': LagouItem.local,
            'co_url': LagouItem.co_url,
            'co_type': LagouItem.co_type
        }
