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


# 筛选1200以上的工况段为 单个文件
def time_series():
    input_file = r'F:/HistoryData/09.csv'
    output_path = r'F:/HistoryData/09时间对/'
    if (not os.path.exists(output_path)):
        os.mkdir(output_path)
    # 数据读取,dataframe格式
    df2 = pd.read_csv(input_file, header=0)

    # 选取满足条件的时间序列, 功率+-8
    # 划分对应的时间工况段
    date = df2['date']
    print(df2.columns.values.tolist())

    if (len(date) > 0):
        begin = [date[0]]
        end = []
        print('合并前', len(date))  # 时间项,不包括标题
        for i in range(0, len(date) - 1):
            if pd.Timestamp(date[i + 1]) - pd.Timestamp(date[i]) != dt.timedelta(seconds=1):
                begin.append(date[i + 1])
                end.append(date[i])
        end.append(date[len(date) - 1])
        print('原始段数', len(begin), len(end))

        # 划分完毕的时间对列表
        segment_sequence = list(zip(begin, end))
        print(segment_sequence)

        # 创建一个空的dataframe,用来存储数据
        df_data = pd.DataFrame(columns=["begin", "end"])

        # 找到每段开始索引和结束索引
        count = 0  # 记录不满足的个数
        time_all = 0

        for seg in segment_sequence:
            # begin_time = seg[0]
            begin_index = df2[df2['date'] == seg[0]].index.tolist()[0]
            # end_time = seg[1]
            end_index = df2[df2['date'] == seg[1]].index.tolist()[0]
            periods = end_index - begin_index + 1
            if periods >= 1200:
                df_data.loc[count, 'begin'] = df2.at[begin_index, 'date']
                df_data.loc[count, 'end'] = df2.at[end_index, 'date']
                count += 1
                time_all += periods
                for i in range(begin_index, end_index + 1):
                    df2.loc[i, 'deviation'] = 1
                df2[df2['deviation'] == 1].to_csv(r'F:/HistoryData/09时间对/{:0>3d}.csv'.format(count), index=False)
                df2.drop(['deviation'], inplace=True, axis=1)
        print('1200的段数: ', count, time_all, time_all / 3600)
        # df_data.to_csv(r'F:/HistoryData/09newprocess_300_370/时间对_9月.csv', index=False)  # 筛选数据后导出到源文件


# 筛选工况段
def filtering_1200():
    input_file = r'F:/HistoryData/all09.csv'
    output_file = r'F:/HistoryData/all09_1200.csv'

    df2 = pd.read_csv(input_file, header=0)

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

    # 划分完毕的时间对列表
    segment_sequence = list(zip(begin, end))
    print(segment_sequence)

    # 找到每段开始索引和结束索引
    count = 0  # 记录不满足的个数
    k_count = 0
    for seg in segment_sequence:

        print(k_count + 1, segment_sequence[k_count])
        k_count += 1

        # begin_time = seg[0]
        begin_index = df2[df2['date'] == seg[0]].index.tolist()[0]
        # print(begin_index)
        # end_time = seg[1]
        end_index = df2[df2['date'] == seg[1]].index.tolist()[0]

        periods = end_index - begin_index + 1
        # print(periods)
        if periods >= 1200:
            for i in range(begin_index, end_index + 1):
                df2.loc[i, 'deviation'] = 1
            count += 1
            print(count)

    df2 = df2[df2['deviation'] == 1]
    df2.drop(['deviation'], inplace=True, axis=1)
    # print(count)
    df2.to_csv(output_file, index=False)

if __name__ == '__main__':
    path = r'F:\HistoryData\08new'
    output_file = r'D:/all08_.csv'
    # path = r'F:\HistoryData\09new'
    # output_file = r'D:/all09_.csv'
    # 第一步, 处理csv 文件表头和 数据合并, 相关数据计算, 差值计算, 算一遍即可
    # data_preprocessing(path, output_file)

    # 第二步, 空白值填充, 观察返回的填充后空白值数量, 一次即可
    df2 = pd.read_csv(output_file, header=0)
    df2 = blank_filling(df2)

    # 第三步 数据筛选, 选择筛选条件
    # df2 = data_filtering(df2)

    # 第四步 选择
    df2.to_csv(output_file, index=False)
    # df2.to_csv(output_file[:-4] + r'selected.csv', index=False)
    end = clock()
    print('time: {:.8f}s'.format(end - start))
