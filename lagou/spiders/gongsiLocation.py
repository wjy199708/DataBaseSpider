# -*- coding: utf-8 -*-
import scrapy



class GongsilocationSpider(scrapy.Spider):
    name = 'gongsiLocation'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/gongsi']

    def parse(self, response):
        # item = GongsiLocationItem()
        gongsiNames = []
        # gongsiName = response.xpath(
        #     "//div[@class='has-more workcity']//div[@class='city-wrapper clearfix']/a[@data-lg-tj-id='7z00']/text()").getall()
        # gongsiNames.append(gongsiName)
        gongsiName2 = response.xpath(
            "//div[@class='has-more workcity']//div[@class='more more-positions']//li[@class='hot']//a[@data-lg-tj-id='7A00']/text()").getall()
        gongsiNames.append(gongsiName2)
        gongsiName3 = response.xpath(
            "//div[@class='has-more workcity']//div[@class='more more-positions']//li[@class='other']//a[@data-lg-tj-id='7B00']/text()").getall()
        gongsiNames.append(gongsiName3)
        # print(len(gongsiName))
        # print(dict(gongsiName))
        # print(gongsiNames)
        # 匹配到        的公司的名称
        # for i in range(gongsiNames):

        for name in gongsiNames:
            print("name" * 20, name)
            for city in name:
                if city!='全国':
                    item['locationName'] = city
                    yield item
