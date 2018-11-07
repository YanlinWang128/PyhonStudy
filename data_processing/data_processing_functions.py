# @Time    : 2018/11/6 10:21
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : data_processing_functions.py

from time import clock
import pandas as pd
import numpy as np
from glob import glob
import os
import datetime as dt

# 合并csv文件
def dir_csv_file_merge(path=r'D:/data/', parttern=r'*.csv', output_file=r'D:/data_processing/all.csv'):
    """
    合并文件夹下所有指定类型 csv文件, 少数文件适用, 多文件用追加那个文件合并
    :param parttern: 文件目录
    :param output_file: 
    :return: 
    """
    if (not os.path.exists(os.path.dirname(output_file))):
        os.mkdir(os.path.dirname(output_file))
    result = pd.concat([pd.read_csv(f, encoding='gbk') for f in glob(path + parttern)], ignore_index=True)
    result.to_csv(output_file, index=False)

# 检测是否有空白值,返回统计空白值
def blank_detect(df2):
    """
    检测是否有空白值,并统计空白值
    :param df2: 传入参数为 pandas dataframe 格式
    :return blank_numbers:  返回空白值的数目 (int类型)
    """
    blank_numbers = int(df2.isnull().any().sum())
    # print("No blank" if (blank_numbers == 0) else "All is {} blank".format(blank_numbers))
    return blank_numbers

# 计算dateframe 的输入列差值
def add_difference(df2):
    # 计算差值
    df2['u1_difference'] = (df2["LAECF411"] - (df2["LAECF411"].shift(1))).shift(-1)
    df2['u2_difference'] = (df2["u2"] - (df2["u2"].shift(1))).shift(-1)
    df2['u3_difference'] = (df2["u3"] - (df2["u3"].shift(1))).shift(-1)
    df2['u4_difference'] = (df2["TOTFUELF"] - (df2["TOTFUELF"].shift(1))).shift(-1)

    return df2

def segment_sequences(df2):
    # 划分对应的时间工况段
    date = df2['date']
    print(df2.columns.values.tolist())
    begin = [date[0]]
    end = []
    print('合并前', len(date))  # 时间项,不包括标题
    for i in range(0, len(date) - 1):
        if pd.Timestamp(date[i + 1]) - pd.Timestamp(date[i]) != dt.timedelta(seconds=1):
            begin.append(date[i + 1])
            end.append(date[i])
    end.append(date[len(date) - 1])
    print(len(begin), len(end))
    segment_sequence = list(zip(begin, end))
    print(segment_sequence)
    return segment_sequence


def deviation_filtering(df2, deviation):
    """
    筛选出与均值偏差 不超过 deviation的数据 
    :param df2:  输入的 pandas dataframe
    :param deviation: 偏差值
    :return: 处理完毕的dataframe
    """

    segment_sequence = segment_sequences(df2)
    # 找到每段开始索引和结束索引
    count = 0  # 记录不满足的个数
    for seg in segment_sequence:
        begin_index = df2[df2['date'] == seg[0]].index.tolist()[0]
        end_index = df2[df2['date'] == seg[1]].index.tolist()[0]

        # 找到数据起始和结束的索引,选中 求均值
        sequence_mean = round(df2['THRPRESS'][begin_index:end_index + 1].mean(), 4)
        print(sequence_mean)

        # 标记偏差小于0.35的值,为deviation列值为0,符合要求,供下一步筛选用
        for i in range(begin_index, end_index + 1):
            if (abs(df2['THRPRESS'][i] - sequence_mean) > deviation):
                df2.loc[i, 'deviation'] = 1
                count += 1
    df2 = df2[df2['deviation'] != 1]
    df2 = df2.drop(['deviation'], axis=1)
    print(count)

    return df2

if __name__ == '__main__':
    start = clock()
    dir_csv_file_merge()
    end = clock()
    print('time: {:.8f}s'.format(end - start))
