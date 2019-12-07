# -*- coding: utf-8 -*-
import scrapy
import re
import json
from lagou.items import GongsiItem
import time
import requests


class LagospiderSpider(scrapy.Spider):
    name = 'gongsi'

    # allowed_domains = ['www.lagou.com']

    count = 1
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '79',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.lagou.com/gongsi/',
    }

    def start_requests(self):
        url = 'https://www.lagou.com/gongsi/0-0-0-0.json'
        # url = 'https://www.lagou.com/gongsi/0-0-0-0.json'
        cookie = self.getNerCookie()

        yield scrapy.FormRequest(
            url=url,
            headers=self.headers,
            callback=self.get_listGongsi,
            dont_filter=True,
            cookies=cookie
        )

    def get_listGongsi(self, response):
        # 获取总页数
        # totalNum = int(re.findall(r'<span class="span totalNum">(.*?)</span>', response.text, re.S)[0])
        # totalNum = int(response.xpath("//div[@class='pager_container']/span[last()-1]/text()").get())

        totalNum = 20
        print("totalNum::::{0}".format(totalNum))
        gongsiDataUrl = 'https://www.lagou.com/gongsi/0-0-0-0.json'

        # 获取每一页岗位的json数据
        for i in range(1, totalNum + 1):
            data = {
                'first': 'false',
                'pn': str(i),
                'sortField': '0',
                'havemark': '0',
                # 'showId': 'a1be1ee54bb14901bf321d014881f6b8'
                # 'sid': '16c6a03fbc0c4db48dbb3eecff390220'
            }
            # sid = '16c6a03fbc0c4db48dbb3eecff390220'

            cookie = self.getNerCookie()

            yield scrapy.FormRequest(
                url=gongsiDataUrl,
                headers=self.headers,
                formdata=data,
                # meta={'sid': sid},
                dont_filter=True,
                callback=self.getJobInfo,
                cookies=cookie
            )
            # time.sleep(1)
            # break
        print("count num of :{0}".format(self.count))

    def getJobInfo(self, response):
        # sid = response.meta['sid']
        jsonJobData = json.loads(response.text)  # 将文档读取为python对象
        result = jsonJobData['result']['pageSize']['showId']['totalCount']

        # 发送需要的job信息
        for job in result:
            totalCount = job['totalCount']
            url = 'https://www.lagou.com/gongsi/0-0-0-0.json'
            yield scrapy.FormRequest(
                url=url,
                dont_filter=True,
                meta={
                    'job': job
                },
                callback=self.parse
            )

    # 将获取的信息发送给pipeline
    def parse(self, response):
        item = GongsiItem()

        # job = response.meta['job']
        # gongsi = json.loads(response.text)

        # job = gongsi
        print(response.text)

        # 设置需要保存在哪里
        # item['pipelineType'] = 'json'
        # gongsidata = {}
        # gongsidata["approve"] = job["approve"]
        # gongsidata["city":] = job["city":]
        # gongsidata["cityScore"] = job["cityScore"]
        # gongsidata["companyCombineScore"] = job["companyCombineScore"]
        # gongsidata["companyFeatures"] = job["companyFeatures"]
        # gongsidata["companyFullName"] = job["companyFullName"]
        # gongsidata["companyId"] = job["companyId"]
        # gongsidata["companyLogo"] = job["companyLogo"]
        # gongsidata["companyShortName"] = job["companyShortName"]
        # gongsidata["companySize"] = job["companySize"]
        # gongsidata["countryScore"] = job["countryScore"]
        # gongsidata["financeStage"] = job["financeStage"]
        # gongsidata["industryField"] = job["industryField"]
        # gongsidata["interviewRemarkNum"] = job["interviewRemarkNum"]
        # gongsidata["isHasValidPosition"] = job["isHasValidPosition"]
        # gongsidata["matchPositionCount"] = job["matchPositionCount"]
        # gongsidata["matchScore"] = job["matchScore"]
        # gongsidata["otherLabel"] = job["otherLabel"]
        # gongsidata["positionNum"] = job["positionNum"]
        # gongsidata["processRate"] = job["processRate"]
        # gongsidata["updateTime"] = job["updateTime"]
        # item['gongsiData'] = gongsidata
        # print(dict(gongsidata))
        self.count += 1
        yield item

    def getNerCookie(self):
        # 防止反爬，在每次进行请求的时候，都需要重新获取cookie
        urls = 'https://www.lagou.com/gongsi/'
        session = requests.Session()
        session.get(url=urls, headers=self.headers, timeout=3)
        cookie = session.cookies  # 获取新的cookie
        return cookie
