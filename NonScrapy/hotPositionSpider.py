import requests
from lxml import etree
import json, time
import bs4
from DataProcess.Mongodb import StorageData
import random, datetime

from NonScrapy import setting


# 随机获取请求头
def randomlyGetUserAgent():
    # 设定请求头
    userAgent = random.choice(setting.userAgent)
    return userAgent


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.lagou.com/gongsi/',
    'User-Agent': randomlyGetUserAgent()
}


def getHotPositionId(url):
    response = requests.get(url=url)
    # print(response.text)
    soup = bs4.BeautifulSoup(response.text, features='lxml')
    spans = soup.find("section", attrs={"class": "jobs-container"}).find_all("span", {"class": "tab-item"})
    # print(spans)
    categoryId = []
    for span in spans:
        res = span.get("data-lg-tj-cid")
        print(res)
        categoryId.append(res)
    return categoryId


def reRequestUrl_To_GetHotPostionDatas(categoryId):
    for id in categoryId:
        ti = 2 + random.random()
        time.sleep(ti)
        response = requests.get(
            'https://xiaoyuan.lagou.com/api/promotion/getPromotionPosition.json?categoryId={0}'.format(id),
            headers=headers)
        jsonDatas = json.loads(response.text)
        positionPromotionList = jsonDatas['content']['data']['positionPromotionList']
        for position in jsonDatas['content']['data']['positionPromotionList']:
            StorageData("hotrecommendationPosition",
                        {'hotPosition': position, 'dataType': 'json',
                         'time': getNowFormatTime()})
        print(dict({'positionPromotionList': positionPromotionList, 'dataType': 'json', 'time': getNowFormatTime()}))


def getNowFormatTime():
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return now


reRequestUrl_To_GetHotPostionDatas(getHotPositionId("https://xiaoyuan.lagou.com/"))
