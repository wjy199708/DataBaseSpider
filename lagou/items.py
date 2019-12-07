# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    co_name = scrapy.Field()
    area = scrapy.Field()
    salary = scrapy.Field()
    exp = scrapy.Field()
    edu = scrapy.Field()
    num = scrapy.Field()
    time = scrapy.Field()
    welfare = scrapy.Field()
    info = scrapy.Field()
    local = scrapy.Field()
    co_url = scrapy.Field()
    co_type = scrapy.Field()
    spider_name = scrapy.Field()


class JobItem(scrapy.Item):
    pipelineType = scrapy.Field()
    keyword = scrapy.Field()
    jobData = scrapy.Field()


class GongsiItem(scrapy.Item):
    pipelineType = scrapy.Field()
    gongsiData = scrapy.Field()
