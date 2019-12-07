# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from lxml import etree
import json
import redis


# 爬取拉钩网的  招聘的职位的分类

class PositioncategorySpider(scrapy.Spider):
    name = 'positionCategory'
    allowed_domains = ['lagou.com']
    start_urls = ['http://www.lagou.com/']

    def parse(self, response):
        # loader = ItemLoader(item=PosCategoryItem(), response=response)
        # item = PosCategoryItem()

        # print()
        # print(len(boxs))
        boxs = response.xpath("//div[@class='menu_box']").getall()
        for i in range(len(boxs)):
            box = boxs[i]
            box = etree.HTML(box)
            nameCategory = box.xpath(
                "//div[@class='menu_main job_hopping']//div[@class='category-list']/h2/text()")
            # print("size of namecate",len(nameCategory))
            # print("==" * 80, nameCategory)
            names = box.xpath(
                "//div[@class='menu_main job_hopping']//div[@class='category-list']//a/h3/text()")
            print("==" * 80, names)

            nameCategory = nameCategory[0].replace('\n', '').replace(' ', '')
            for name in names:
                print(nameCategory)
                item['nameCategory'] = nameCategory
                item['name'] = name
                # cols = []
                # cols.append(dict(item))

                # print(dict(item))

                client = redis.Redis(host='192.168.65.119', encoding='utf-8')
                client.set('lagou:{0}:{1}'.format(nameCategory, name),
                           str(dict(item)))
                yield item  # 使用yield产生爬取到的数据，不会像return那样，返回一个数据之后就会结束这个函数的运行了。
        # print("size of clos", len(cols))
