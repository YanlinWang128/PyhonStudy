# @Time    : 2018/10/25 16:00
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 单文件空白值检测.py

import pandas as pd
import numpy as py
import os


def blank_detect(df2):
    """
    检测是否有空白值,并统计空白值
    :param df2: 传入参数为 pandas dataframe 格式
    :return blank_numbers:  返回空白值的数目 (int类型)
    """
    blank_numbers = int(df2.isnull().any().sum())
    print("No blank" if (blank_numbers == 0) else "All is {} blank".format(blank_numbers))
    return blank_numbers


if __name__ == '__main__':
    path_file = r'C:/Users/Frank/Desktop/try1025'

    df2 = pd.read_csv(path_file, header=0, encoding='gbk')
    # df2.fillna(method='bfill', inplace=True)
    # while (blank_detect(df2)):
    #     df2.fillna(method='ffill', inplace=True)

    blank_detect(df2)

    #
    # output_path = r'F:/HistoryData/08data1025/'
    # output_path_file = os.path.join(output_path, info)
    # dfnew.to_csv(output_path_file, index=False)