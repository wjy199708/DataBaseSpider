# -*- coding: utf-8 -*-
import scrapy
import re
import json
from lagou.items import JobItem
import time
from DataProcess.Mongodb import StorageData


class LagospiderSpider(scrapy.Spider):
    name = 'job'
    # allowed_domains = ['www.lagou.com']

    count = 1

    def start_requests(self):
        url = 'https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput='

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

        yield scrapy.FormRequest(
            url=url,
            headers=headers,
            callback=self.get_listJob,
            dont_filter=True
        )

    def get_listJob(self, response):
        # 获取总页数
        # totalNum = int(re.findall(r'<span class="span totalNum">(.*?)</span>', response.text, re.S)[0])
        totalNum = int(response.xpath("//span[@class='span totalNum']/text()").get())
        print("totalNum::::{0}".format(totalNum))
        jobDataUrl = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

        # 获取每一页岗位的json数据
        for i in range(1, totalNum + 1):
            data = {
                'first': 'false',
                'pn': str(i),
                'kd': '',
                # 'sid': '16c6a03fbc0c4db48dbb3eecff390220'
            }
            # sid = '16c6a03fbc0c4db48dbb3eecff390220'

            yield scrapy.FormRequest(
                url=jobDataUrl,
                headers=headers,
                formdata=data,
                # meta={'sid': sid},
                dont_filter=True,
                callback=self.getJobInfo
            )
            # time.sleep(2)
            # break
        print("count num of :{0}".format(self.count))

    def getJobInfo(self, response):
        # sid = response.meta['sid']
        jsonJobData = json.loads(response.text)

        hrInfo = jsonJobData['content']['hrInfoMap']
        result = jsonJobData['content']['positionResult']['result']

        # 发送需要的job信息
        for job in result:
            positionId = job['positionId']
            url = 'https://www.lagou.com/jobs/{}.html?show=79a9491071e94813ae6e954c7e7ea77e'.format(positionId)
            keyword = jsonJobData['content']['positionResult']['queryAnalysisInfo']['positionName']
            yield scrapy.FormRequest(
                url=url,
                meta={
                    'keyword': keyword,
                    'job': job,
                    'hrInfo': hrInfo
                },
                dont_filter=True,
                callback=self.parse
            )

    # 将获取的信息发送给pipeline
    def parse(self, response):
        keyword = response.meta['keyword']
        item = JobItem()

        job = response.meta['job']
        hrInfo = response.meta['hrInfo']

        # 将hr的信息存入mongodb的hr集合
        StorageData('hrInfo', dict(hrInfo))

        jobData = {}
        jobData["positionId"] = job["positionId"]
        jobData["positionName"] = job["positionName"]
        jobData["companyId"] = job["companyId"]
        jobData["companyFullName"] = job["companyFullName"]
        jobData["companyShortName"] = job["companyShortName"]
        jobData["companyLogo"] = job["companyLogo"]
        jobData["companySize"] = job["companySize"]
        jobData["industryField"] = job["industryField"]
        jobData["financeStage"] = job["financeStage"]
        jobData["companyLabelList"] = job["companyLabelList"]
        jobData["firstType"] = job["firstType"]
        jobData["secondType"] = job["secondType"]
        jobData["thirdType"] = job["thirdType"]
        jobData["skillLables"] = job["skillLables"]
        jobData["positionLables"] = job["positionLables"]
        jobData["industryLables"] = job["industryLables"]
        jobData["createTime"] = job["createTime"]
        jobData["formatCreateTime"] = job["formatCreateTime"]
        jobData["city"] = job["city"]
        jobData["district"] = job["district"]
        jobData["businessZones"] = job["businessZones"]
        jobData["salary"] = job["salary"]
        jobData["workYear"] = job["workYear"]
        jobData["jobNature"] = job["jobNature"]
        jobData["education"] = job["education"]
        jobData["positionAdvantage"] = job["positionAdvantage"]
        jobData["imState"] = job["imState"]
        jobData["lastLogin"] = job["lastLogin"]
        jobData["publisherId"] = job["publisherId"]
        jobData["approve"] = job["approve"]
        jobData["subwayline"] = job["subwayline"]
        jobData["stationname"] = job["stationname"]
        jobData["linestaion"] = job["linestaion"]
        jobData["latitude"] = job["latitude"]
        jobData["longitude"] = job["longitude"]
        jobData["hitags"] = job["hitags"]
        jobData["resumeProcessRate"] = job["resumeProcessRate"]
        jobData["resumeProcessDay"] = job["resumeProcessDay"]
        jobData["score"] = job["score"]
        jobData["explain"] = job["explain"]
        jobData["isSchoolJob"] = job["isSchoolJob"]
        jobData["adWord"] = job["adWord"]
        jobData["plus"] = job["plus"]
        jobData["pcShow"] = job["pcShow"]
        jobData["appShow"] = job["appShow"]
        jobData["deliver"] = job["deliver"]
        jobData["gradeDescription"] = job["gradeDescription"]
        jobData["promotionScoreExplain"] = job["promotionScoreExplain"]
        jobData["isHotHire"] = job["isHotHire"]

        item['keyword'] = keyword
        item['jobData'] = jobData

        # 设置需要保存在哪里
        item['pipelineType'] = 'json'

        # 将item信息根据keyword保存到对应的mongo集合
        StorageData(keyword, dict(item))
        self.count += 1
        yield item
