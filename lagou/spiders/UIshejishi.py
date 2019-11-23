# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lagou.items import UIshejishiItem
from lxml import etree


class UishejishiSpider(CrawlSpider):
    name = 'UIshejishi'
    allowed_domains = ['lagou.com']
    start_urls = ['https://lagou.com/zhaopin/UIshejishi/1/']

    rules = (
        Rule(LinkExtractor(allow='zhaopin/UIshejishi/\d.*'), callback='parse_item', follow=True),
    )

    # def start_requests(self):
    #     COOKIE = {"Cookie":"_ga=GA1.2.418244780.1573962429; user_trace_token=20191117114708-ee07ce47-08ec-11ea-a5c3-525400f775ce; LGUID=20191117114708-ee07d187-08ec-11ea-a5c3-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e7778f0b8726-09ebddc0be3456-51402e1a-2073600-16e7778f0b9698%22%2C%22%24device_id%22%3A%2216e7778f0b8726-09ebddc0be3456-51402e1a-2073600-16e7778f0b9698%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAAAGFABEF71C47B803A870DC18A07A0CB7EC3F698; WEBTJ-ID=20191119195024-16e837fd8944c-091293e02c591d-51402e1a-2073600-16e837fd895715; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574038048,1574038307,1574060058,1574164224; _gid=GA1.2.213128990.1574164225; TG-TRACK-CODE=index_navigation; X_MIDDLE_TOKEN=14b0b5b6045ff6ff429d7b451336168e; LGSID=20191119205541-e49c6754-0acb-11ea-a66f-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; SEARCH_ID=78278774df8e42c4b7d3f063ef4f421a; gate_login_token=c49e478bed34efeee1cd98dc445ebda62c77babd300d12c7ab96012ca375b98d; LG_HAS_LOGIN=1; _putrc=296FB451539B45F8123F89F2B170EADC; login=true; hasDeliver=0; privacyPolicyPopup=false; _gat=1; unick=%E7%8E%8B%E4%BF%8A%E5%8D%B0; X_HTTP_TOKEN=9b53c27d765922065439614751f4dd06c197b4dd3e; LGRID=20191119211546-b265dedb-0ace-11ea-a670-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574169348"}
    #     yield scrapy.Request(self.start_urls[0], cookies=COOKIE)

    def parse_item(self, response):
        # l = ItemLoader(item=LagouItem(), response=response)
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = UIshejishiItem()
        # htmls = response.body
        # print(htmls)
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
                "//li[@data-positionname='{0}']//div[@class='list_item_bot']/div[@class='li_b_l']/span/text()".format(
                    name)[
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
