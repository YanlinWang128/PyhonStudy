# @Time    : 2018/10/10 15:41
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 保留长度为1200s以上的段.py

import pandas as pd
import datetime as dt
import os

# input_file = r'F:/HistoryData/08newdeviation/08new_after_deviation.csv'
# output_file = r'F:/HistoryData/08newdeviation/08new_after_deviation1200.csv'
# input_file = r'F:/HistoryData/09newprocess_300_370/all09_300_370.csv'
# output_file = r'F:/HistoryData/09newprocess_300_370/09_300_370.csv'
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

    print(k_count+1,segment_sequence[k_count])
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
