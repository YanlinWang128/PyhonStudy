# @Time    : 2018/11/6 10:23
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : data_processing.py

from time import clock
from data_processing_functions import *
import pandas as pd
import numpy as np
import os
import sys
from glob import glob
import re

start = clock()
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# 第一步, 数据预处理: 处理csv 文件表头和 数据合并, 相关数据计算, 差值计算
# 第一步只需要一次,生成最终 整月的数据
def data_preprocessing(path=r'F:\HistoryData\08new', output_file=r'D:/all08_.csv', pattern=r'\*_p*.csv'):
    """
    
    :param path:  原始文件所在文件夹, 用window默认形式, 反斜杠, pattern以反斜杠开头
    :return: 
    """
    columns_we_need = ['时间', 'UNIT2:LAECF411', 'UNIT2:T12A041A', 'UNIT2:JT66801A', 'UNIT2:THRPRESS', 'UNIT2:AIRFLOW',
                       'UNIT2:TOTFUELF', 'UNIT2:MSTMFLOW', 'UNIT2:T10A042A', 'UNIT2:TOTFWFLW', 'UNIT2:FWFLOWD', 'u2',
                       'u3', 'LYTFW', 'UNIT2:HHL517CG']
    columns_new = ['date'] + [x[6:] if x.startswith('UNIT2:') else x for x in columns_we_need[1:]]

    files = sorted(glob(path + pattern), key=lambda items: int(re.findall(r'p(\d+).csv', items)[0]))

    file_counts = len(files)
    for i in range(file_counts):
        print(files[i])
        df2 = pd.read_csv(os.path.join(path, files[i]), encoding='gbk')
        df2['u2'] = (
            (df2['UNIT2:HAG10T01'] + df2['UNIT2:HAG10T02'] + df2['UNIT2:HAG10T03'] + df2['UNIT2:HAG10T04'] +
             df2['UNIT2:HAG10T05'] + df2['UNIT2:HAG10T06'] + df2['UNIT2:HAG10T13'] + df2['UNIT2:HAG10T14'] +
             df2['UNIT2:HAG10T15'] + df2['UNIT2:HAG10T16'] + df2['UNIT2:HAG10T17'] + df2['UNIT2:HAG10T18']) / 12)

        df2['u3'] = (df2['UNIT2:HBKCT101'] + df2['UNIT2:HBKCT201']) / 2
        df2['LYTFW'] = (df2['UNIT2:LABCT301'] + df2['UNIT2:LABCT302']) / 2
        df2 = df2[columns_we_need]
        df2.columns = columns_new
        # 计算dataframe 输入 difference差值
        df2 = add_difference(df2)
        if i is 0:
            df2.to_csv(output_file, index=False)
        else:
            df2.to_csv(output_file, index=False, header=False, mode='a+')


# 第二步, 空白值填充, 观察返回的填充后空白值数量
def blank_filling(df2):
    print('blank is', blank_detect(df2))
    df2.fillna(method='bfill', inplace=True)
    df2.fillna(method='ffill', inplace=True)
    print('blank is', blank_detect(df2))
    df2.fillna(method='bfill', inplace=True)
    df2.fillna(method='ffill', inplace=True)
    print('blank is', blank_detect(df2))
    return df2


# 第三步 数据筛选, 选择筛选条件
def data_filtering(df2):
    # 功率筛选
    ## 功率300以上, 或者功率 330正负 8
    df2 = df2[(df2['JT66801A'] >= 300)]

    # 燃烧器摆角筛选, 注意连续筛选需要重设索引 reset_index(drop=True)
    df2 = df2[(df2['HHL517CG'] < 10) & (df2['HHL517CG'] > -10)].reset_index(drop=True)

    # 主汽压 每一小连续段 偏差值小于 0.35, 不满足的不要
    df2 = deviation_filtering(df2, 0.35)


    #
    return df2


if __name__ == '__main__':
    path = r'F:\HistoryData\08new'
    output_file = r'D:/all08_.csv'
    # path = r'F:\HistoryData\09new'
    # output_file = r'D:/all09_.csv'
    # 第一步, 处理csv 文件表头和 数据合并, 相关数据计算, 差值计算, 算一遍即可
    # data_preprocessing(path, output_file)

    # 第二步, 空白值填充, 观察返回的填充后空白值数量, 一次即可
    df2 = pd.read_csv(output_file, header=0)
    # df2 = blank_filling(df2)

    # 第三步 数据筛选, 选择筛选条件
    df2 = data_filtering(df2)

    # 第四步 选择

    df2.to_csv(output_file[:-4] + r'selected.csv', index=False)
    end = clock()
    print('time: {:.8f}s'.format(end - start))
