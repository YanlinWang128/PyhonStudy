# @Time    : 2018/10/11 14:20
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 筛选每个工况数据为单个文件.py


import pandas as pd
import datetime as dt
import os

input_file = r'F:/HistoryData/all09_1200.csv'
output_path = r'F:/HistoryData/只按功率筛选09_300_up时间对/'
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
            df2[df2['deviation'] == 1].to_csv(r'F:/HistoryData/只按功率筛选09_300_up时间对/{:0>3d}.csv'.format(count), index=False)
            df2.drop(['deviation'], inplace=True, axis=1)
    print('1200的段数: ', count, time_all, time_all / 3600)
    # df_data.to_csv(r'F:/HistoryData/09newprocess_300_370/时间对_9月.csv', index=False)  # 筛选数据后导出到源文件

