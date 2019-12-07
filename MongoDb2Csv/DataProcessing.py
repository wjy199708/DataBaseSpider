import pandas as pd
import csv


class DataProcessing:
    '''
    csv数据处理
    '''

    def fill_missing_value(self, filename):
        '''
        对csv文件中的缺失值填充0
        :param filename:str 文件路径+文件名
        :return:返回填充好的dataframe数据
        '''
        deal_data = pd.read_csv(filename)
        # 对缺失值填充0
        deal_data = deal_data.fillna(0)
        return deal_data

    def delete_missing_value(self, filename):
        '''
        删除缺失值对应的行
        :param filename:  str 文件路径+文件名
        :return:返回填充好的dataframe数据
        '''
        deal_data = pd.read_csv(filename)
        # 对缺失值填充0
        deal_data = deal_data.dropna(inplace=False)
        return deal_data
