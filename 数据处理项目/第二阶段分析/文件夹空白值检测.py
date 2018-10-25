# @Time    : 2018/10/25 16:03
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 文件夹空白值检测.py


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
    input_path = r'F:/HistoryData/08data1025'
    for info in os.listdir(input_path):
        domain = os.path.abspath(input_path)  # 获取文件夹的路径
        path_file = os.path.join(domain, info)  # 将路径与文件名结合起来就是每个文件的完整路径

        df2 = pd.read_csv(path_file, header=0, encoding='gbk')
        # df2.fillna(method='bfill', inplace=True)
        # df2.fillna(method='ffill', inplace=True)
        # df2.fillna(method='bfill', inplace=True)
        # df2.fillna(method='ffill', inplace=True)

        df2.fillna(method='ffill', inplace=True)
        while (blank_detect(df2)):
            df2.fillna(method='bfill', inplace=True)
            df2.fillna(method='ffill', inplace=True)


        if blank_detect(df2) != 0:
            print(path_file)
            # exit()




        # output_path = r'F:/HistoryData/08data1025/'
        # output_path_file = os.path.join(output_path, info)
        df2.to_csv(path_file, index=False)