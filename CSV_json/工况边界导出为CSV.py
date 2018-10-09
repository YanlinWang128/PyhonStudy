# @Time    : 2018/10/9 15:15
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 工况边界导出为CSV.py

import pandas as pd
import datetime as dt

input_file = r'D:/rawData201608.csv'
deviation = 0.35  # 偏差设定值
# 数据读取,dataframe格式
df2 = pd.read_csv(input_file, encoding='gbk', header=0)

# 选取满足条件的时间序列, 功率+-8
# 划分对应的时间工况段
date = df2['时间']
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
    print(len(begin), len(end))

    # 划分完毕的时间对列表
    segment_sequence = list(zip(begin, end))
    print(segment_sequence)

    # 创建一个空的dataframe,用来存储数据
    df_data = pd.DataFrame(columns=["begin", "end"])

    # 找到每段开始索引和结束索引
    count = 0  # 记录不满足的个数
    for seg in segment_sequence:
        # begin_time = seg[0]
        begin_index = df2[df2['时间'] == seg[0]].index.tolist()[0]
        # end_time = seg[1]
        end_index = df2[df2['时间'] == seg[1]].index.tolist()[0]
        if end_index - begin_index >= 1800:
            df_data.loc[count, 'begin'] = df2.at[begin_index, '时间']
            df_data.loc[count, 'end'] = df2.at[end_index, '时间']
            count += 1
            # df2.loc[i, 'deviation'] = 1

            # df2 = df2[df2['deviation'] != 1]
    print(count)
    df_data.to_csv('D:/时间对.csv', index=False, encoding='gbk')  # 筛选数据后导出到源文件

    # a = data[data.time == '2016-09-01 00:38:00'].index.tolist()
    # 对划分的每一段求均值

    # 创建一个空的dataframe 用来存储数据
