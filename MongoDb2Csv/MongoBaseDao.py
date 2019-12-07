"""
mongo操作工具
"""
import pandas as pd
import numpy as np
from pymongo import MongoClient
from MongoDb2Csv.DataProcessing import DataProcessing

MONGO_HOST, MONGO_PORT, MONGO_DB, MONGO_TABLE = '127.0.0.1', 27017, 'stock', 'tb_ds_quotation'


class MongoBaseDao:
    """
    链接mongoDB，进行各种操作
    """

    def __init__(self, host=MONGO_HOST, port=MONGO_PORT, db_name=MONGO_DB):
        """
        初始化对象，链接数据库
        :param host: mongo数据库所在服务器地址
        :param port: mongo数据库端口
        :param db_name: 数据库的名称
        :return: 无返回值
        """
        try:
            self.client = None
            self.client = MongoClient(host, port)
            self.database = self.client.get_database(db_name)
            self.collection = None
            print("连接成功！")
        except Exception as e:
            self.close_conn()
            print('初始化mongodb失败: %s' % e)

    def change_collection(self, table_name=MONGO_TABLE):
        """切换表"""
        self.collection = self.database.get_collection(table_name)

    def count_info(self, table_name=MONGO_TABLE, filter_dict=None):
        """
        查找表记录条数，默认返回0
        :param table_name: str 表名
        :param filter_dict: dict 过滤条件
        :return: int 表记录条数
        """
        tab_size = 0
        try:
            self.collection = self.database.get_collection(table_name)
            tab_size = self.collection.find(filter_dict).count()
            return tab_size
        except Exception as e:
            print('get table size failed: %s' % e)
        finally:
            return tab_size

    def update_info(self, filter_dict, update_dict, insert=False, multi=False):
        """
        更新表记录，默认返回false
        :param filter_dict: dict 过滤条件，如{'campaignId':{'$in':[1,2,3]}}
        :param update_dict: dict 更新的字段，如{'$set':{status_key:0，'campaign.status':1},{'$unset':'campaign.name':'test_camp'}}
        :param insert: bool 如果需要更新的记录不存在是否插入
        :param multi: bool 是否更新所有符合条件的记录， False则只更新一条，True则更新所有
        :return: bool 是否更新成功
        """
        result = False
        try:
            self.collection.update(filter_dict, update_dict, insert, multi)
            result = True
            print("[INFO] update success!")
        except Exception as e:
            print('update failed: %s' % e)
        finally:
            return result

    def insert_many_info(self, insert_date):
        """
        插入多条记录
        :param insert_date: list 插入的数据，如[
  { "_id": 1, "name": "RUNOOB", "cn_name": "教程"},
  { "_id": 2, "name": "Google", "address": "Google 搜索"},
  { "_id": 3, "name": "Facebook", "address": "脸书"},
  { "_id": 4, "name": "Taobao", "address": "淘宝"},
  { "_id": 5, "name": "Zhihu", "address": "知乎"}
]
        :return:bool 是否成功
        """
        result = False
        try:
            self.collection.insert_many(insert_date)
            result = True
            print("insert success!")
        except Exception as e:
            print('insert failed: %s' % e)
        finally:
            return result

    def insert_one_info(self, insert_date):
        '''
        插入一条信息
        :param insert_date: dic 数据例如{ item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" }
        :return:是否成功
        '''
        result = False
        try:
            self.collection.insert_one(insert_date)
            result = True
            print("insert success!")
        except Exception as e:
            print('insert failed: %s' % e)
        finally:
            return result

    def delete_info(self, filter_date):
        """
        更新表记录，默认返回false
        :param filter_date: dict 删除数据的条件，如{'campaignId':{'$in':[1,2,3]}}
        :return: bool 是否更新成功
        """
        result = False
        try:
            self.collection.remove(filter_date)
            result = True
            print("remove success!")
        except Exception as e:
            print('remove failed: %s' % e)
        finally:
            return result

    def find_one_info(self, filter_dict):
        """
        查找一条表记录，默认返回空字典
        :param filter_dict: dict 过滤条件如{'campaignId':123}
        :return: dict 查找到的数据
        """
        result = {}
        try:
            result = self.collection.find_one(filter_dict)
        except Exception as e:
            print('find data failed: %s' % e)
        finally:
            return result

    def find_multi_info(self, filter_dict, return_dict, limit_size=0, skip_index=0):
        """
        查找多条表记录，默认返回空数组
        :param filter_dict: dict filter_dict: 过滤条件如{'campaignId':123}
        :param return_dict: dict 返回的字段如{'campaign.status':1,'updated':1,'_id':0}
        :param limit_size: int 限定返回的数据条数
        :param skip_index: int 游标位移
        :return: list 查询到的记录组成的列表，每个元素是一个字典
        """
        result = []
        try:
            if not limit_size:
                if not skip_index:
                    result = self.collection.find(filter_dict, return_dict)
                else:
                    result = self.collection.find(filter_dict, return_dict).skip(skip_index)
            else:
                if not skip_index:
                    result = self.collection.find(filter_dict, return_dict).limit(limit_size)
                else:
                    result = self.collection.find(filter_dict, return_dict).skip(skip_index).limit(limit_size)
        except Exception as e:
            print('find data failed: %s' % e)
        finally:
            return result

    def find_All_info(self):
        """
        查找所有记录，默认查询的所有数据
        """
        result = []
        try:
            result = self.collection.find()
        except Exception as e:
            print('find data failed: %s' % e)
        finally:
            return result

    def close_conn(self):
        """
        关闭数据库链接
        :return: 无返回值
        """
        if self.client:
            self.client.close()
