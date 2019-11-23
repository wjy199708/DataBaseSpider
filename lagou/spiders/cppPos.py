# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lagou.items import JavaPositionItem
from lxml import etree
class CppposSpider(CrawlSpider):
    name = 'cppPos'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/zhaopin/C++/1']

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/C\+\+/\d.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # l = ItemLoader(item=LagouItem(), response=response)
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = JavaPositionItem()
        htmls = response.body
        # 公司名称
        # lis=response.xpath("//ul[@class='item_con_list']/li")
        lis = response.xpath("//ul[@class='item_con_list']/li").getall()
        print("lis" * 20, len(lis))
        for i in range(len(lis)):
            html = etree.HTML(lis[i])
            co_name = html.xpath("//div[@class='company']/div[@class='company_name']/a/text()")
            # 职位名称
            name = html.xpath(
                "//li[@class='con_list_item default_list']//div[@class='p_top']//h3/text()")
            # 薪资
            salary = html.xpath(
                "//div[@class='postion']//div[@class='p_bot']//span[@class='money']/text()")
            # 区域
            area = html.xpath(
                "//div[@class='postion']//div[@class='p_bot']//span[@class='add']/em/text()")
            # 工作年限
            exp = html.xpath(
                "//div[@class='postion']//div[@class='p_bot']//div[@class='li_b_l']/text()")
            # 学历
            edu = html.xpath(
                "//div[@class='postion']//div[@class='p_bot']//div[@class='li_b_l']/text()")
            # 发布时间
            time = html.xpath("//div[@class='p_top']//span[@class='format-time']/text()")
            time = self.getVal(time)
            # 职位描述
            info_query = \
            "//li[@data-positionname='{0}']//div[@class='list_item_bot']/div[@class='li_b_l']/span/text()".format(name)[
                0]
            print(str(info_query[0]))
            info = html.xpath(str(info_query))
            info = ";".join(info)
            print("info" * 20, info)
            # info = self.getVal(info)
            # if info != '':
            #     info = '\n'.join(info).encode('utf-8')

            # 工作地点
            local = html.xpath(
                "//div[@class='postion']//div[@class='p_bot']//span[@class='add']//em/text()")
            # 公司福利
            welfare = html.xpath("//div[@class='list_item_bot']//div[@class='li_b_r']/text()")
            # 公司网址
            co_url = ""
            # 招聘人数
            num = '0'
            # 公司类别
            co_type = html.xpath('//dl[@class="industry"]/text()')
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
            print(dict(item))
            yield item

    def getVal(self, data):
        return data if data else ''

