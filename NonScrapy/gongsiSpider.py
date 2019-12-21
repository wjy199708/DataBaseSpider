import requests
import json, time
from DataProcess.Mongodb import StorageData
from NonScrapy.hotPositionSpider import getNowFormatTime


def gongsi_info(url):  # 定义获取公司信息的函数
    # 定义写入的文件，并用csv进行写
    storage_file = open('./gongsi.txt', 'w', encoding='utf-8')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.lagou.com/gongsi/',
        'User-Agent': randomlyGetUserAgent()
    }

    for pn in range(2, 15):
        if pn % 2 == 0:
            headers['User-Agent'] = randomlyGetUserAgent()
            print("请求头中的User-Agent为：header['User-Agent']:::", headers['User-Agent'], "请求头为：headers:::", headers)
        params = {
            'first': 'false',
            'pn': str(pn),
            'sortField': '0',
            'havemark': '0',
            'showId': 'e135bd5a1eee4e2b94e83de5c5852146'
        }  # post请求参数

        try:
            with open('./html.txt', 'r', )as f:  # 如果存在该文件，就打开并读取内容，否则就创建该文件
                t = f.readlines()
            if str(pn) + '\n' in t:
                print('第' + str(pn) + '页已经爬取过了')
            else:
                # 每次都将重新请求一下这个页面从而获得新的cookie进行请求
                urls = 'https://www.lagou.com/gongsi/'
                s = requests.Session()
                s.get(urls, headers=headers, timeout=3)  # 请求首页获取cookies
                cookie = s.cookies  # 为此次获取的cookies
                print(cookie)

                # 拿到新获取到的cookie数据再对页面进行post请求
                response = s.post(url, data=params, headers=headers, cookies=cookie, timeout=5)  # 获取此次文本
                #                time.sleep(3)

                # response.encoding = response.apparent_encoding
                # print(response.text)

                json_data = json.loads(response.text)
                # print("json_data:::()".format(json_data))

                # 获取数据
                # print(json_data['totalCount'])
                #                 try:
                results = json_data['result']
                #                 except requests.exceptions.HTTPError:
                #                     continue
                #
                #                 print("results:::", results, '\n', "resluts_len:::", len(results))
                #
                #                 # 设置新的数据格式
                for result in results:
                    infos = {
                        'approve': result['approve'],
                        'city': result['city'],
                        'cityScore': result['cityScore'],
                        'companyCombineScore': result['companyCombineScore'],
                        'companyFeatures': result['companyFeatures'],
                        'companyFullName': result['companyFullName'],
                        'companyId': result['companyId'],
                        'companyLogo': result['companyLogo'],
                        'companyShortName': result['companyShortName'],
                        'companySize': result['companySize'],
                        'countryScore': result['countryScore'],
                        'financeStage': result['financeStage'],
                        'industryField': result['industryField'],
                        'interviewRemarkNum': result['interviewRemarkNum'],
                        'isHasValidPosition': result['isHasValidPosition'],
                        'matchPositionCount': result['matchPositionCount'],
                        'matchScore': result['matchScore'],
                        'otherLabel': result['otherLabel'],
                        'positionNum': result['positionNum'],
                        'processRate': result['processRate'],
                        'updateTime': result['updateTime'],
                    }
                    print("infos::::", infos)
                    storage_file.write(str(infos) + '\n')
                    StorageData('gongsi', dict({'info': infos, 'dataType': 'json', 'time': getNowFormatTime()}))
                ti = 10 + random.random()  # 设置间隔时间，防止被服务器屏蔽
                print("本次防止访问过快让网站屏蔽的延时请求为(0)秒(/s)".format(ti))
                time.sleep(ti)
        except requests.exceptions.ConnectionError:
            continue


import NonScrapy.setting as setting
import random


# 随机获取请求头
def randomlyGetUserAgent():
    # 设定请求头
    userAgent = random.choice(setting.userAgent)
    return userAgent


if __name__ == '__main__':
    url = 'https://www.lagou.com/gongsi/0-0-0-0.json'
    gongsi_info(url)
    print('finished!!')
