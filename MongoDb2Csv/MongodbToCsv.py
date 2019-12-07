# coding:utf-8

from MongoDb2Csv.MongoBaseDao import MongoBaseDao
import pandas as pd


class MongodbToCsv:
    """
    将MongoDB中的数据按照一定的条件取出，删除部分后再存为Csv格式
    """

    def __init__(self):
        """
        实例化一个操作mongo的对象
        """
        self.__mongo = MongoBaseDao('192.168.65.119', 27017, 'spider')

    def read_delete_by_time_save_to_csv(self, col_name):
        """
        根据时间读取表中所有数据
        :param col_name: 在哪个collection中查找
        :param datetime: date_time列格式化为datetime对象数组
        :param key_time: 要根据什么字段查找
        :return:
        """
        self.__mongo.change_collection(col_name)
        # 按照时间取多条数据
        collection = self.__mongo.find_multi_info(filter_dict={}, return_dict=None)
        tmp_data_taken_out = pd.DataFrame(list(collection))  # 转换成DataFrame格式
        # self.__mongo.delete_info(list(collection))         #按照时间删除
        # print(TmpData_taken_out)
        filepath = "H:\\Spider\\美术设计师2d3d.csv"
        tmp_data_taken_out.to_csv(filepath, sep=',')  # 将DataFrame存储为csv,index表示是否显示行名，default=True

    @staticmethod
    def main():
        a = MongodbToCsv()
        a.read_delete_by_time_save_to_csv('美术设计师2d3d')


MongodbToCsv.main()
